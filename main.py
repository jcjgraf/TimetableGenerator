import sys
import os
import getopt
from icalendar import Calendar, Event
from jinja2 import Environment, FileSystemLoader
from collections import Counter
from datetime import datetime

from event import *

def readFromIcs(calendarPath):
    """
        Extract the event information from the calendarPath ics file and store the data in a days array
    """
    
    days = [dict() for i in range(5)]

    # Read data from .ics calendar
    with open(calendarPath, "rb") as f:
        
        calendar = Calendar.from_ical(f.read())
        
        for component in calendar.walk():
            if component.name == "VEVENT":
                event = Event(component.get('summary'),
                                component.get('description'),
                                component.get('dtstart').dt,
                                component.get('dtend').dt,
                                component.get('location'))

                days[event.start.weekday()][event.start.hour] = event
                event.description = ""      # Ignore description

    return days    

def writeToTemplate(templatePath, days):
    """
        Take the events in the days array and write the data to the template file
    """

    env = Environment(loader=FileSystemLoader('.'))
    template = env.get_template(templatePath)
    
    colors = ['red', 'green', 'blue', 'orange', 'purple', 'brown', 'gray', 'cyan']

    names = Counter(event.title for day in days for event in day.values() )
    names = [x[0] for x in names.most_common()]

    # Write events to template file
    texPath = os.path.splitext(templatePath)[0] + ".tex"
    print(texPath)
    with open(texPath, "w") as f:
        f.write(template.render(
            days=days, names=zip(names, colors)
        ))


if __name__ == "__main__":
    calendarPath = ""
    templatePath = ""

    usage = "Usage: \n-c, --calendar <calendar>\n-t, --template <template>"
    
    try:
        opts, args = getopt.getopt(sys.argv[1:], "hc:t:", ["calendarpath=", "templatepath="])
    except getopt.GetoptError:
        print(usage)
        sys.exit(2)

    for opt, arg in opts:
        
        if opt == "-h":
            print(usage)
            sys.exit()
    
        elif opt in ("-c", "--calendarpath"):
            calendarPath = arg
        
        elif opt in ("-t", "--templatepath"):
            templatePath = arg

    if (calendarPath == "" or templatePath == ""):
        print("Please provide calendarpath and templatepath")
        print(usage)
        sys.exit(2)
                
    print("Generating timetable")
    days = readFromIcs(calendarPath)
    
    writeToTemplate(templatePath, days)
