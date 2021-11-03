import csv
import json


def write_to_csv(results, filename):
    """Write an iterable of `CloseApproach` objects to a CSV file."""
    fieldnames = ('datetime_utc', 'distance_au', 'velocity_km_s', 'designation', 'name', 'diameter_km',
                  'potentially_hazardous')

    with open(f'outputs/{filename}', 'w') as csv_dct_writer:
        writer = csv.DictWriter(csv_dct_writer, fieldnames=fieldnames)
        writer.writeheader()
        for row in results:
            writer.writerow({'datetime_utc': row.time,
                             'distance_au': row.distance,
                             'velocity_km_s': row.velocity,
                             'designation': row._designation,
                             'name': row.neo.name if row.neo.name else '',
                             'diameter_km': row.neo.diameter if row.neo.diameter else 'nan',
                             'potentially_hazardous': str(row.neo.hazardous)
                             })


def write_to_json(results, filename):
    """Write an iterable of `CloseApproach` objects to a JSON file."""
    with open(f'outputs/{filename}', 'w') as json_outputs:
        outputs = []
        for row in results:
            outputs.append(
                {
                    "datetime_utc": row.time_str,
                    "distance_au": row.distance,
                    "velocity_km_s": row.velocity,
                    "neo": {
                      "designation": row._designation,
                      "name": row.neo.name if row.neo.name else "",
                      "diameter_km": row.neo.diameter,
                      "potentially_hazardous": row.neo.hazardous}
                }
            )
        json.dump(outputs, json_outputs)
