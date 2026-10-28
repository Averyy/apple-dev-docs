# CMDateTime

**Framework**: Application Services  
**Kind**: struct  
**Role**: Structure

Contains data that specifies a date and time in year, month, day of the month, hours, minutes, and seconds

**Availability**:
- macOS 10.0+ - Deprecated in 10.6

## Declaration

```c
typedef struct CMDateTime {
    ...
} CMDateTime;
```

## Overview

The ColorSync Manager defines the `CMDateTime` data structure to specify a date and time in year, month, day of the month, hours, minutes, and seconds. Other ColorSync structures use the `CMDateTime` structure to specify information such as the creation date or calibration date for a color space profile.

The `CMDateTime` structure is similar to the Macintosh Toolbox structure `DateTimeRec`, and like it, is intended to hold date and time values only for a Gregorian calendar.

The `CMDateTime` structure is platform independent. However, when used with Macintosh Toolbox routines such as `SecondsToDate` and `DateToSeconds`, which use seconds to designate years, the range of years that can be represented is limited. 

## Topics

### Instance Properties
- [dayOfTheMonth](./cmdatetime/api-1560620-dayofthemonth.md)
  The day of the month, ranging from 1 to 31.
- [hours](./cmdatetime/api-1560584-hours.md)
  The hour of the day, ranging from 0 to 23, where 0 represents midnight and 23 represents 11:00 P.M.
- [minutes](./cmdatetime/api-1560534-minutes.md)
  The minutes of the hour, ranging from 0 to 59.
- [month](./cmdatetime/api-1560099-month.md)
  The month of the year, where 1 represents January, and 12 represents December.
- [seconds](./cmdatetime/api-1560220-seconds.md)
  The seconds of the minute, ranging from 0 to 59.
- [year](./cmdatetime/api-1560351-year.md)
  The year. Note that to indicate the year 1984, this field would store the integer 1984, not just 84.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applicationservices/cmdatetime)*