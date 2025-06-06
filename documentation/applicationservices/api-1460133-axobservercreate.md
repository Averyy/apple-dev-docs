# AXObserverCreate(_:_:_:)

**Framework**: Application Services  
**Kind**: func

Creates a new observer that can receive notifications from the specified application.

**Availability**:
- macOS 10.2+

## Declaration

```swift
func AXObserverCreate(_ application: pid_t, _ callback: AXObserverCallback, _ outObserver: UnsafeMutablePointer<AXObserver?>) -> AXError
```

#### Return_value

If unsuccessful, `AXObserverCreate` may return one of the following error codes, among others:

#### Discussion

When an observed notification is received, it is passed to [`AXObserverCallback`](axobservercallback.md).

## Parameters

- `application`: The process ID of the application.
- `callback`: The callback function.
- `outObserver`: On return, an AXObserverRef representing the observer object.

## See Also

- [func AXObserverAddNotification(AXObserver, AXUIElement, CFString, UnsafeMutableRawPointer?) -> AXError](1462089-axobserveraddnotification.md)
  Registers the specified observer to receive notifications from the specified accessibility object.
- [func AXObserverCreateWithInfoCallback(pid_t, AXObserverCallbackWithInfo, UnsafeMutablePointer<AXObserver?>) -> AXError](1460610-axobservercreatewithinfocallback.md)
  Creates a new observer that can receive notifications with an information dictionary from the specified application.
- [func AXObserverGetRunLoopSource(AXObserver) -> CFRunLoopSource](1459139-axobservergetrunloopsource.md)
  Returns the observer's run loop source.
- [func AXObserverGetTypeID() -> CFTypeID](1461244-axobservergettypeid.md)
  Returns the unique type identifier for the AXObserverRef type.
- [func AXObserverRemoveNotification(AXObserver, AXUIElement, CFString) -> AXError](1462066-axobserverremovenotification.md)
  Removes the specified notification from the list of notifications the observer wants to receive from the accessibility object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applicationservices/1460133-axobservercreate)*