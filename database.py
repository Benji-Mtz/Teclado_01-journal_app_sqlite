entries = [
    {"content": "Today I started learning programing.", "date": "01-01-2020"},
    {"content": "I created my first SQLite database!", "date": "02-01-2020"},
    {"content": "I finished writing my programming diary application.", "date": "03-01-2020"},
    {"content": "Today I'm going to continue learning programming!", "date": "04-01-2020"},
]

def add_entry():
    entry_content = input("What have you learned today? ")
    entry_date = input("Enter the date: ")
    
    entries.append({"content": entry_content, "date": entry_date})


def view_entries():
    for entry in entries:
        print(f"{entry['date']}\n{entry['content']}\n\n")