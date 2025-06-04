# WKAlertActionHandler

**Framework**: Watchkit  
**Kind**: typealias

A block to perform in response to an action.

**Availability**:
- watchOS ?+

## Declaration

```swift
typealias WKAlertActionHandler = () -> Void
```

## Overview

This block takes no parameters and returns no value. You use this type of block to perform a task when one of your actions is selected by the user. Your block does not need to dismiss the alert or action sheet itself. WatchKit automatically dismisses the sheet when the user taps in any of your action buttons.

## See Also

- [enum WKAlertActionStyle](wkalertactionstyle.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkalertactionstyle))


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkalertactionhandler)*