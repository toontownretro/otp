
class TelemetryLimited:
    Sng = SerialNumGen()

    def __init__(self):
        # Gives an object a unique ID using SerialNumGen
        self._telemetryLimiterId = next(self.Sng)
        self._limits = set()

    def getTelemetryLimiterId(self):
        # Fetches the object's ID
        return self._telemetryLimiterId

    def addTelemetryLimit(self, limit):
        # Adds the limit to an object
        self._limits.add(limit)

    def removeTelemetryLimit(self, limit):
        # Removes the limit of an object
        if limit in self._limits:
            self._limits.remove(limit)

    def enforceTelemetryLimits(self):
        # This enforces limits on objects
        # i.e RotationLimitToH
        for limit in self._limits:
            limit(self)
