# Date Format Cheatsheet

<style>
.markdown-body{ padding: 0 45px; }
section.level2 { display: flex; border-bottom: 1px solid rgba(0, 0, 0, 0.1); }
section.level2 h2 { width: 20%; align-self: flex-end; margin: 0; border: 0; }
section.level2 ul { align-self: center; margin: 0; }
</style>

Use `man strftime` for more details

## Seconds

- `%s`: the number of seconds singe the Unix Epoch, 1970-01-01
- `%S`: seconds as a decimal number, `00`-`59`

## Minutes

- `%M`: The minute as a decimal number, `00`-`59`

## Hours

- `%H`: 24 hour clock with a leading 0, `00`-`23`
- `%I`: 12 hour clock with a leading 0, `01`-`12`
- `%k`: 24 hour clock without a leading 0, `0`-`23`
- `%l`: 12 hour clock without a leading 0, `1-12`
- `%p`: "AM" or "PM"; noon is "PM", midnight is "AM"
- `%P`: like `%p`, but lowercase

## Days

- `%a`: abbreviated weekday name, `Sun`
- `%A`: full weekday name, `Sunday`
- `%d`: day of the month with a leading 0, `01`-`31`
- `%e`: day of the month with a leading space, ` 1`-`31`
- `%j`: day of the year, `001`-`366`
- `%u`: day of the week, monday is 1, `1`-`7`
- `%w`: day of the week, sunday is 0, `0`-`6`

## Weeks

- `%U`: week of the year; weeks start on Sunday, `00`-`53`
- `%W`: week of the year; weeks start on Monday, `00`-`53`

## Months

- `%b`: abbreviated month name, `Jul`
- `%B`: full month name, `July`
- `%m`: month of the year, `01`-`12`

## Years

- `%y`: year without century, `00`-`99`
- `%Y`: year including century

## Timezones

- `%z`: offset from UTC, `+hhmm` or `-hhmm`
- `%Z`: timezone name or abbreviation

## Shortcuts

- `%D`: `%M/%D/%Y`
- `%T`: `%H:%M:%S`
- `%F`: ISO 8601 format
- `%x`: localized date without time
- `%X`: localized time without date
