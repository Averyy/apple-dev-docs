# setDate(_:)

**Framework**: WatchKit  
**Kind**: method

Changes the start time for the timer.

**Availability**:
- watchOS 2.0+

## Declaration

```swift
func setDate(_ date: Date)
```

#### Discussion

This method updates the target value but does not automatically update the timer display. You must call the timer’s [`start()`](wkinterfacetimer/start().md) method to begin updating the text it displays. When you do, the timer text is updated based on the time you set using this method.

## Parameters

- `date`: The new starting time for the timer. Specifying the current date or a date in the past causes the timer to count upward from that time. Specifying a date in the future causes the timer to count down to the specified time.

## See Also

- [App Programming Guide for watchOS](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/General/Conceptual/WatchKitProgrammingGuide/index.html#//apple_ref/doc/uid/TP40014969)
- [func start()](wkinterfacetimer/start.md)
  Begins updates to the timer’s display.
- [func setTextColor(UIColor?)](wkinterfacetimer/settextcolor(_:).md)
  Sets the color of the timer’s text.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkinterfacetimer/setdate(_:))*