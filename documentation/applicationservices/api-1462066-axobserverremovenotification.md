# AXObserverRemoveNotification(_:_:_:)

**Framework**: Application Services  
**Kind**: func

Removes the specified notification from the list of notifications the observer wants to receive from the accessibility object.

**Availability**:
- macOS 10.2+

## Declaration

```swift
func AXObserverRemoveNotification(_ observer: AXObserver, _ element: AXUIElement, _ notification: CFString) -> AXError
```

#### Return_value

If unsuccessful, `AXObserverRemoveNotification` may return one of the following error codes, among others:

## Parameters

- `observer`: The observer object created from a call to  .
- `element`: The accessibility object for which this observer observes notifications.
- `notification`: The name of the notification to remove from the list of observed notifications.

## See Also

- [func AXObserverAddNotification(AXObserver, AXUIElement, CFString, UnsafeMutableRawPointer?) -> AXError](1462089-axobserveraddnotification.md)
  Registers the specified observer to receive notifications from the specified accessibility object.
- [func AXObserverCreate(pid_t, AXObserverCallback, UnsafeMutablePointer<AXObserver?>) -> AXError](1460133-axobservercreate.md)
  Creates a new observer that can receive notifications from the specified application.
- [func AXObserverCreateWithInfoCallback(pid_t, AXObserverCallbackWithInfo, UnsafeMutablePointer<AXObserver?>) -> AXError](1460610-axobservercreatewithinfocallback.md)
  Creates a new observer that can receive notifications with an information dictionary from the specified application.
- [func AXObserverGetRunLoopSource(AXObserver) -> CFRunLoopSource](1459139-axobservergetrunloopsource.md)
  Returns the observer's run loop source.
- [func AXObserverGetTypeID() -> CFTypeID](1461244-axobservergettypeid.md)
  Returns the unique type identifier for the AXObserverRef type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applicationservices/1462066-axobserverremovenotification)*