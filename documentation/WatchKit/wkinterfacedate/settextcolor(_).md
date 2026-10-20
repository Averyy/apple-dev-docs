# setTextColor(_:)

**Framework**: WatchKit  
**Kind**: method  
**Role**: Instance Method

Sets the color of the date and time text.

**Availability**:
- watchOS 2.0+

## Declaration

```swift
func setTextColor(_ color: UIColor?)
```

```objc
- (void) setTextColor:(UIColor *) color;
```

## Parameters

- `color`: The custom color to be applied to the time string. Specifying `nil` removes the custom color and returns the text to the color specified in the storyboard file. The default text color is white.

## See Also

### Related Documentation
- [App Programming Guide for watchOS](https://developer.apple.com/library/archive/documentation/General/Conceptual/WatchKitProgrammingGuide/index.html#//apple_ref/doc/uid/TP40014969)
### Configuring the Date and Time Display
- [func setTimeZone(TimeZone?)](./settimezone%28_%29.md)
  Sets the time zone to use when displaying time information.
- [func setCalendar(Calendar?)](./setcalendar%28_%29.md)
  Sets the calendar to use when formatting date information.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkinterfacedate/settextcolor(_:))*