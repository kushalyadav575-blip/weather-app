from entry import JournalEntry
import json
def save_entries(entries, filepath):
    entries_as_dicts = [item.to_dict() for item in entries]
    with open(filepath, "w") as file:
        json.dump(entries_as_dicts, file)

def load_entries(filepath):
    try:
        with open(filepath, "r") as reader:
            file_data=json.load(reader)
            journal_entries = [JournalEntry.from_dict(item) for item in file_data]
            return journal_entries
    except (FileNotFoundError,json.JSONDecodeError):
        print("no existing journal data found, starting fresh")
        return []

def see_entries(date, entries):
    matches = [item for item in entries if item.date == date]
    return matches