"""Read and validate weather-station temperature observations."""

from datetime import datetime
import math
import os
import sys
import tempfile
import unittest


DATE_FORMAT = "%I:%M:%S %p %m/%d/%Y"


def read_observations(filename):
    """Return (observations, errors) read from *filename*.

    ``observations`` maps a station name to sorted ``(date, temperature)``
    tuples.  Dates remain strings in the returned data; ``datetime`` objects
    are used only to place them in chronological order.
    """
    observations = {}
    errors = []
    seen = set()

    with open(filename, "r", encoding="utf-8-sig") as input_file:
        for line_number, line in enumerate(input_file, start=1):
            fields = [field.strip() for field in line.rstrip("\n\r").split(",")]

            if len(fields) != 3 or any(field == "" for field in fields):
                errors.append((line_number, "malformed line"))
                continue

            station, date, temperature_text = fields

            try:
                date_value = datetime.strptime(date, DATE_FORMAT)
            except ValueError:
                errors.append((line_number, "malformed date"))
                continue

            try:
                temperature = float(temperature_text)
            except ValueError:
                errors.append((line_number, "invalid temperature"))
                continue

            if not math.isfinite(temperature) or not -100.0 <= temperature <= 150.0:
                errors.append((line_number, "temperature out of range"))
                continue

            key = (station, date)
            if key in seen:
                errors.append((line_number, "duplicate station/date combination"))
                continue

            seen.add(key)
            observations.setdefault(station, []).append((date, temperature))

    for station in observations:
        observations[station].sort(
            key=lambda observation: datetime.strptime(observation[0], DATE_FORMAT)
        )

    return observations, errors


def station_statistics(observations):
    """Return {station: (minimum, maximum, mean)} temperature summaries."""
    statistics = {}

    for station, station_observations in observations.items():
        temperatures = [temperature for _, temperature in station_observations]
        statistics[station] = (
            min(temperatures),
            max(temperatures),
            sum(temperatures) / len(temperatures),
        )

    return statistics


def station_outliers(observations):
    """Return stations whose latest temperature is above their mean."""
    statistics = station_statistics(observations)

    return {
        station: (station_observations[-1][0],
                  station_observations[-1][1],
                  statistics[station][2])
        for station, station_observations in observations.items()
        if station_observations
        and station_observations[-1][1] > statistics[station][2]
    }


def write_statistics(filename, statistics):
    """Write sorted station statistics as CSV rows.

    Each row has the form ``station,minimum,maximum,mean``.  The values in
    ``statistics`` are the ``(minimum, maximum, mean)`` tuples returned by
    :func:`station_statistics`.
    """
    with open(filename, "w", encoding="utf-8", newline="") as output_file:
        for station in sorted(statistics):
            minimum, maximum, mean = statistics[station]
            output_file.write(
                f"{station},{minimum:.1f},{maximum:.1f},{mean:.1f}\n"
            )


def main():
    """Read observations, display results, and write station statistics.

    Usage: ``python p5_Liers_Daniel.py input_file output_file``
    """
    if len(sys.argv) != 3:
        print(
            "Usage: python p5_Liers_Daniel.py input_file output_file",
            file=sys.stderr,
        )
        return 1

    input_filename = sys.argv[1]
    output_filename = sys.argv[2]

    try:
        observations, errors = read_observations(input_filename)
    except OSError as error:
        print(f"Could not read '{input_filename}': {error}", file=sys.stderr)
        return 1

    for line_number, message in errors:
        print(f"Line {line_number}: {message}", file=sys.stderr)

    statistics = station_statistics(observations)
    outliers = station_outliers(observations)

    print("Statistics:")
    for station in sorted(statistics):
        minimum, maximum, mean = statistics[station]
        print(f"{station}: min={minimum:.1f}, max={maximum:.1f}, mean={mean:.1f}")

    print("Outliers:")
    for station in sorted(outliers):
        date, temperature, mean = outliers[station]
        print(f"{station}: {date}, {temperature:.1f}, mean={mean:.1f}")

    try:
        write_statistics(output_filename, statistics)
    except OSError as error:
        print(f"Could not write '{output_filename}': {error}", file=sys.stderr)
        return 1

    return 0


class WeatherObservationTests(unittest.TestCase):
    def make_input_file(self, contents):
        """Create an input file for a test and return its filename."""
        with tempfile.NamedTemporaryFile(
            mode="w", encoding="utf-8", delete=False, newline=""
        ) as input_file:
            input_file.write(contents)
            return input_file.name

    def test_reads_several_stations_and_sorts_dates(self):
        filename = self.make_input_file(
            "north,10:00:00 AM 04/20/2026,10.0\n"
            "south,09:00:00 AM 04/20/2026,20.0\n"
            "north,08:00:00 AM 04/20/2026,5.0\n"
        )
        try:
            observations, errors = read_observations(filename)
        finally:
            os.remove(filename)

        self.assertEqual(errors, [])
        self.assertEqual(
            observations["north"],
            [("08:00:00 AM 04/20/2026", 5.0),
             ("10:00:00 AM 04/20/2026", 10.0)],
        )
        self.assertEqual(observations["south"], [("09:00:00 AM 04/20/2026", 20.0)])

    def test_accepts_negative_temperature(self):
        filename = self.make_input_file("north,09:00:00 AM 04/20/2026,-5.5\n")
        try:
            observations, errors = read_observations(filename)
        finally:
            os.remove(filename)

        self.assertEqual(errors, [])
        self.assertEqual(observations["north"][0][1], -5.5)

    def test_rejects_duplicate_station_and_date(self):
        filename = self.make_input_file(
            "north,09:00:00 AM 04/20/2026,5.0\n"
            "north,09:00:00 AM 04/20/2026,10.0\n"
        )
        try:
            observations, errors = read_observations(filename)
        finally:
            os.remove(filename)

        self.assertEqual(observations["north"], [("09:00:00 AM 04/20/2026", 5.0)])
        self.assertEqual(errors, [(2, "duplicate station/date combination")])

    def test_rejects_temperatures_outside_valid_range(self):
        filename = self.make_input_file(
            "north,09:00:00 AM 04/20/2026,-100.1\n"
            "south,09:00:00 AM 04/20/2026,150.1\n"
        )
        try:
            observations, errors = read_observations(filename)
        finally:
            os.remove(filename)

        self.assertEqual(observations, {})
        self.assertEqual(
            errors,
            [(1, "temperature out of range"), (2, "temperature out of range")],
        )

    def test_calculates_station_statistics(self):
        observations = {
            "north": [("one", -5.0), ("two", 10.0), ("three", 20.0)],
            "south": [("one", 3.0)],
        }

        self.assertEqual(
            station_statistics(observations),
            {"north": (-5.0, 20.0, 25.0 / 3.0), "south": (3.0, 3.0, 3.0)},
        )

    def test_writes_statistics_in_sorted_order(self):
        with tempfile.NamedTemporaryFile(delete=False) as output_file:
            filename = output_file.name
        try:
            write_statistics(
                filename,
                {"zeta": (-2.0, 5.0, 1.5), "alpha": (1.0, 3.0, 2.0)},
            )
            with open(filename, encoding="utf-8") as output_file:
                rows = output_file.read().splitlines()
        finally:
            os.remove(filename)

        self.assertEqual(rows, ["alpha,1.0,3.0,2.0", "zeta,-2.0,5.0,1.5"])

    def test_missing_file_raises_file_not_found_error(self):
        with self.assertRaises(FileNotFoundError):
            read_observations("file_that_does_not_exist.csv")


if __name__ == "__main__":
    sys.exit(main())
