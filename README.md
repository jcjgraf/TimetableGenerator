# ICS Timetable Generator
> Create a pdf (/latex) timetable from an ics calendar

## Introduction
Create a 5 days timetables of repeated events (e.g. lectures) automatically from a `.ics` calendar.\
The style is based on [this](http://texample.net/tikz/examples/timetable/) latex example. So go there to see how the final pdf looks like.

## Prerequisites
The script requires the following python 3 packages, which may be installed via `pip`:
- `icalendar`
- `jinja2`

Furthermore, a working latex installation is required.

## Get Started
Run the script with `python3 main.py -c <pathToIcsCalendar> -t timetable.tpl`
Generate a PDF from the Tex with e.g. `pdflatex timetable.tex`

## Credits
This project is heavily based on [this Stackexchange answer](https://tex.stackexchange.com/a/270143). 
