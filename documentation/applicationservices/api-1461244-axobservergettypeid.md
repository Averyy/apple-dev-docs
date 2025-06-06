# AXObserverGetTypeID()

**Framework**: Application Services  
**Kind**: func

Returns the unique type identifier for the AXObserverRef type.

**Availability**:
- macOS 10.2+

## Declaration

```swift
func AXObserverGetTypeID() -> CFTypeID
```

#### Return_value

Returns the CFTypeID of the AXObserverRef type.

## See Also

- [func AXObserverAddNotification(AXObserver, AXUIElement, CFString, UnsafeMutableRawPointer?) -> AXError](1462089-axobserveraddnotification.md)
  Registers the specified observer to receive notifications from the specified accessibility object.
- [func AXObserverCreate(pid_t, AXObserverCallback, UnsafeMutablePointer<AXObserver?>) -> AXError](1460133-axobservercreate.md)
  Creates a new observer that can receive notifications from the specified application.
- [func AXObserverCreateWithInfoCallback(pid_t, AXObserverCallbackWithInfo, UnsafeMutablePointer<AXObserver?>) -> AXError](1460610-axobservercreatewithinfocallback.md)
  Creates a new observer that can receive notifications with an information dictionary from the specified application.
- [func AXObserverGetRunLoopSource(AXObserver) -> CFRunLoopSource](1459139-axobservergetrunloopsource.md)
  Returns the observer's run loop source.
- [func AXObserverRemoveNotification(AXObserver, AXUIElement, CFString) -> AXError](1462066-axobserverremovenotification.md)
  Removes the specified notification from the list of notifications the observer wants to receive from the accessibility object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applicationservices/1461244-axobservergettypeid)*