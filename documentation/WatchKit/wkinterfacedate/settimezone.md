# setTimeZone(_:)

**Framework**: WatchKit  
**Kind**: method

Sets the time zone to use when displaying time information.

**Availability**:
- watchOS 2.0+

## Declaration

```swift
func setTimeZone(_ timeZone: TimeZone?)
```

#### Discussion

Use this method to configure the time zone to one that is different from the user’s current time zone. For example, a world clock app might use this method to configure the time display information.

## Parameters

- `timeZone`: The time zone to be used. Specifying   removes the time zone information and causes Apple Watch to use the current time zone based on the user’s settings.

## See Also

- [func setTextColor(UIColor?)](wkinterfacedate/settextcolor(_:).md)
  Sets the color of the date and time text.
- [func setCalendar(Calendar?)](wkinterfacedate/setcalendar(_:).md)
  Sets the calendar to use when formatting date information.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkinterfacedate/settimezone(_:))*