from helpers import cd_to_datetime, datetime_to_str
# from workspace.helpers import cd_to_datetime, datetime_to_str


class NearEarthObject:
    """A near-Earth object (NEO).

    An NEO encapsulates semantic and physical parameters about the object, such
    as its primary designation (required, unique), IAU name (optional), diameter
    in kilometers (optional - sometimes unknown), and whether it's marked as
    potentially hazardous to Earth.

    A `NearEarthObject` also maintains a collection of its close approaches -
    initialized to an empty collection, but eventually populated in the
    `NEODatabase` constructor.
    """
    def __init__(self, designation='', name=None, diameter=float('nan'), hazardous=False):
        self.designation = designation
        self.name = name if name != '' else None
        self.diameter = float(diameter) if diameter != '' else float('nan')
        self.hazardous = False if hazardous == '' or hazardous == "N" else True

        # Create an empty initial collection of linked approaches.
        self.approaches = []

    @property
    def fullname(self):
        """Return a representation of the full name of this NEO."""
        if self.name:
            return f'{self.designation} {self.name}'
        else:
            return f'{self.designation}'

    def __str__(self):
        return f"A NearEarthObject {self.fullname} with diameter of {self.diameter} classified as {'hazardous' if self.hazardous == True else 'not hazardous'}"

    def serialize(self):
        return {
            'designation': self.designation,
            'name': self.name,
            'diameter_km': self.diameter,
            'potentially_hazardous': self.hazardous
        }


class CloseApproach:
    """A close approach to Earth by an NEO.

    A `CloseApproach` encapsulates information about the NEO's close approach to
    Earth, such as the date and time (in UTC) of closest approach, the nominal
    approach distance in astronomical units, and the relative approach velocity
    in kilometers per second.

    A `CloseApproach` also maintains a reference to its `NearEarthObject` -
    initally, this information (the NEO's primary designation) is saved in a
    private attribute, but the referenced NEO is eventually replaced in the
    `NEODatabase` constructor.
    """
    def __init__(self, designation='', time=None, distance=0.0, velocity=0.0):
        self._designation = designation
        self.time = cd_to_datetime(time)  # TODO: Use the cd_to_datetime function for this attribute.
        self.distance = float(distance)
        self.velocity = float(velocity)

        self.neo = None

    @property
    def time_str(self):
        """Return a formatted representation of this `CloseApproach`'s approach time."""
        return f'{datetime_to_str(self.time)}'

    def __str__(self):
        return f"A CloseApproach of {self.neo.fullname} at {self.time} in {self.distance} au with velocity of {self.velocity} km"

    def __repr__(self):
        return f"{self.neo.fullname}"
