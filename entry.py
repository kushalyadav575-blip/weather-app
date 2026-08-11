class JournalEntry:

    def __init__(self, date, note , mood, weather_data):
        self.date = date
        self.note = note
        self.mood = mood
        self.weather_data = weather_data

    def to_dict(self):
        return {
            "date": self.date,
            "note": self.note,
            "mood": self.mood,
            "weather_data": self.weather_data
        }

    @classmethod
    def from_dict(cls, data):
        return cls(data["date"], data["note"], data["mood"], data["weather_data"]) 
