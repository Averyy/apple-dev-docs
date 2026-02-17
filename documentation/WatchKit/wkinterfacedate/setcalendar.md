# setCalendar(_:)

**Framework**: WatchKit  
**Kind**: method

Sets the calendar to use when formatting date information.

**Availability**:
- watchOS 2.0+

## Declaration

```swift
func setCalendar(_ calendar: Calendar?)
```

#### Discussion

Use this method to configure the calendar to one that is different from the user’s current calendar. You might change the calendar to format dates differently based on your app’s needs. For example, a financial reporting app might use a calendar that breaks the year into fiscal quarters rather than months.

## Parameters

- `calendar`: The calendar to be used. Specifying nil removes the calendar information and causes Apple Watch to use the default calendar based on the user’s settings.

## See Also

- [func setTextColor(UIColor?)](wkinterfacedate/settextcolor(_:).md)
  Sets the color of the date and time text.
- [func setTimeZone(TimeZone?)](wkinterfacedate/settimezone(_:).md)
  Sets the time zone to use when displaying time information.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkinterfacedate/setcalendar(_:))*