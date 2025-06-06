# AXObserverAddNotification(_:_:_:_:)

**Framework**: Application Services  
**Kind**: func

Registers the specified observer to receive notifications from the specified accessibility object.

**Availability**:
- macOS 10.2+

## Declaration

```swift
func AXObserverAddNotification(_ observer: AXObserver, _ element: AXUIElement, _ notification: CFString, _ refcon: UnsafeMutableRawPointer?) -> AXError
```

#### Return_value

If unsuccessful, `AXObserverAddNotification` may return one of the following error codes, among others:

## Parameters

- `observer`: The observer object created from a call to  .
- `element`: The accessibility object for which to observe notifications.
- `notification`: The name of the notification to observe.
- `refcon`: Application-defined data passed to the callback when it is called.

## See Also

- [func AXObserverCreate(pid_t, AXObserverCallback, UnsafeMutablePointer<AXObserver?>) -> AXError](1460133-axobservercreate.md)
  Creates a new observer that can receive notifications from the specified application.
- [func AXObserverCreateWithInfoCallback(pid_t, AXObserverCallbackWithInfo, UnsafeMutablePointer<AXObserver?>) -> AXError](1460610-axobservercreatewithinfocallback.md)
  Creates a new observer that can receive notifications with an information dictionary from the specified application.
- [func AXObserverGetRunLoopSource(AXObserver) -> CFRunLoopSource](1459139-axobservergetrunloopsource.md)
  Returns the observer's run loop source.
- [func AXObserverGetTypeID() -> CFTypeID](1461244-axobservergettypeid.md)
  Returns the unique type identifier for the AXObserverRef type.
- [func AXObserverRemoveNotification(AXObserver, AXUIElement, CFString) -> AXError](1462066-axobserverremovenotification.md)
  Removes the specified notification from the list of notifications the observer wants to receive from the accessibility object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applicationservices/1462089-axobserveraddnotification)*