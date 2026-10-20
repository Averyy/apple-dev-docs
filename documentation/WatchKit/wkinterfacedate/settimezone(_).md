# setTimeZone(_:)

**Framework**: WatchKit  
**Kind**: method  
**Role**: Instance Method

Sets the time zone to use when displaying time information.

**Availability**:
- watchOS 2.0+

## Declaration

```swift
func setTimeZone(_ timeZone: TimeZone?)
```

```objc
- (void) setTimeZone:(NSTimeZone *) timeZone;
```

#### Discussion

Use this method to configure the time zone to one that is different from the user’s current time zone. For example, a world clock app might use this method to configure the time display information.

## Parameters

- `timeZone`: The time zone to be used. Specifying `nil` removes the time zone information and causes Apple Watch to use the current time zone based on the user’s settings.

## See Also

### Configuring the Date and Time Display
- [func setTextColor(UIColor?)](./settextcolor%28_%29.md)
  Sets the color of the date and time text.
- [func setCalendar(Calendar?)](./setcalendar%28_%29.md)
  Sets the calendar to use when formatting date information.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkinterfacedate/settimezone(_:))*