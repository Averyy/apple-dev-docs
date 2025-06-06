# AXObserverCallbackWithInfo

**Framework**: Application Services  
**Kind**: tdef

**Availability**:
- macOS 10.9+

## Declaration

```swift
typealias AXObserverCallbackWithInfo = (AXObserver, AXUIElement, CFString, CFDictionary, UnsafeMutableRawPointer?) -> Void
```

## Parameters

- `observer`: An AXObserverRef object to observe the notifications.
- `element`: The accessibility object.
- `notification`: The name of the notification to observe.
- `info`: The coresponding notification information.
- `refcon`: Application-defined data specified when registering the observer for notification

## See Also

- [typealias AXObserverCallback](axobservercallback.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/applicationservices/axobservercallbackwithinfo)*