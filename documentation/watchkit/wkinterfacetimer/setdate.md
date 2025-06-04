# setDate(_:)

**Framework**: Watchkit  
**Kind**: method

Changes the start time for the timer.

**Availability**:
- watchOS 2.0+

## Declaration

```swift
func setDate(_ date: Date)
```

## Overview

This method updates the target value but does not automatically update the timer display. You must call the timer’s [`start()`](https://developer.apple.com/documentation/watchkit/wkinterfacetimer/start()) method to begin updating the text it displays. When you do, the timer text is updated based on the time you set using this method.

## Parameters

- `date`: The new starting time for the timer. Specifying the current date or a date in the past causes the timer to count upward from that time. Specifying a date in the future causes the timer to count down to the specified time.

## See Also

- [App Programming Guide for watchOS](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/General/Conceptual/WatchKitProgrammingGuide/index.html#//apple_ref/doc/uid/TP40014969)
- [func start()](start().md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfacetimer/start()))
- [func setTextColor(UIColor?)](settextcolor(_:).md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfacetimer/settextcolor(_:)))


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkinterfacetimer/setdate(_:))*