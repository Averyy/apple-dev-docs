# AXObserverCallback

**Framework**: Application Services  
**Kind**: tdef  
**Role**: Type Alias

**Availability**:
- macOS 10.2+

## Declaration

```swift
typealias AXObserverCallback = (AXObserver, AXUIElement, CFString, UnsafeMutableRawPointer?) -> Void
```

```c
typedef void (*AXObserverCallback)(AXObserverRef observer, AXUIElementRef element, CFStringRef notification, void *refcon);
```

## Parameters

- `observer`: An AXObserverRef object to observe the notifications.
- `element`: The accessibility object.
- `notification`: The name of the notification to observe.
- `refcon`: Application-defined data specified when registering the observer for notification

## See Also

### Callbacks
- [typealias AXObserverCallbackWithInfo](./axobservercallbackwithinfo.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/applicationservices/axobservercallback)*