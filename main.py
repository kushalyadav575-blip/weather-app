from entry import JournalEntry
from storage import save_entries, load_entries, see_entries
from weather import get_weather
import sys
import datetime
while True:
    action=input("what do you want to do search date from existing entrie or make a new one?(enter search or new or exit)")
    if action=="search":
        date=input("enter a date to search from existing journal")
        existing_date=load_entries("journal.json")
        matches=see_entries(date, existing_date)
        for item in matches:
            print(item.date, item.note, item.mood)
    elif action=="new":
        today=str(datetime.date.today())
        weather= None
        while weather is None:
            city = input("enter the city name: ")
            if city == "exit":
                sys.exit()
            weather = get_weather(city)
            if weather is not None:
                print(f"the weather in {city} is {weather['current_temp']} {weather['temp_unit']}")
        note=input("enter a note")
        mood=input("hows your mood")
        existing_data=load_entries("journal.json")
        journalentry1=JournalEntry(today, note, mood, weather)
        existing_data.append(journalentry1)
        save_entries(existing_data,"journal.json")

    elif action=="exit":
        break
    else:
        print("invalid action try again")