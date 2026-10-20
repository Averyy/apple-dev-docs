# AXObserverGetTypeID()

**Framework**: Application Services  
**Kind**: func  
**Role**: Function

Returns the unique type identifier for the AXObserverRef type.

**Availability**:
- macOS 10.2+

## Declaration

```swift
func AXObserverGetTypeID() -> CFTypeID
```

```c
CFTypeID AXObserverGetTypeID(void);
```

#### Return Value

Returns the CFTypeID of the AXObserverRef type.

## See Also

### Notification API
- [func AXObserverAddNotification(AXObserver, AXUIElement, CFString, UnsafeMutableRawPointer?) -> AXError](./api-1462089-axobserveraddnotification.md)
  Registers the specified observer to receive notifications from the specified accessibility object.
- [func AXObserverCreate(pid_t, AXObserverCallback, UnsafeMutablePointer<AXObserver?>) -> AXError](./api-1460133-axobservercreate.md)
  Creates a new observer that can receive notifications from the specified application.
- [func AXObserverCreateWithInfoCallback(pid_t, AXObserverCallbackWithInfo, UnsafeMutablePointer<AXObserver?>) -> AXError](./api-1460610-axobservercreatewithinfocallback.md)
  Creates a new observer that can receive notifications with an information dictionary from the specified application.
- [func AXObserverGetRunLoopSource(AXObserver) -> CFRunLoopSource](./api-1459139-axobservergetrunloopsource.md)
  Returns the observer's run loop source.
- [func AXObserverRemoveNotification(AXObserver, AXUIElement, CFString) -> AXError](./api-1462066-axobserverremovenotification.md)
  Removes the specified notification from the list of notifications the observer wants to receive from the accessibility object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applicationservices/1461244-axobservergettypeid)*