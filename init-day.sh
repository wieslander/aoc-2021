#!/bin/sh
#
# init-day.sh - set up boilerplate for today's solution
#
# USAGE
#     ./init-day.sh [DAY]
#
#   Copy the solution template file to src/aoc/solutions/DAY.py and use
#   the `aoc' command to download the input file for the given day to
#   inputs/DAY.txt.
#
#   If DAY is omitted, use today's date.
#
# DEPENDENCIES
#   Uses the `aoc' command from https://github.com/scarvalhojr/aoc-cli
#   to download input files.

if [ -n "$1" ]; then
  day=`date '+%d'`
else
  day="$1"
fi

# Copy template to solution file and update date in docstring
day="$1"
day_padded=`printf %02d $day`
solution_filename="src/aoc/solutions/${day_padded}.py"
sed "s/<DAY>/${day}/g" src/template.py > "$solution_filename"

# Download today's input file
aoc -y 2021 -d "$day" -f "inputs/${day_padded}.txt" download
