# AXObserverGetRunLoopSource(_:)

**Framework**: Application Services  
**Kind**: func

Returns the observer's run loop source.

**Availability**:
- macOS 10.2+

## Declaration

```swift
func AXObserverGetRunLoopSource(_ observer: AXObserver) -> CFRunLoopSource
```

#### Return_value

Returns the CFRunLoopSourceRef of the observer; NIL if you pass NIL in `observer`.

#### Discussion

The observer must be added to a run loop before it can receive notifications. Note that releasing the AXObserverRef automatically removes the run loop source from the run loop (you can also do this explicitly by calling [`CFRunLoopRemoveSource(_:_:_:)`](https://developer.apple.com/documentation/corefoundation/cfrunloopremovesource(_:_:_:))).

`AXObserverGetRunLoopSource` might be used in code in this way:

```occ
 
 CFRunLoopAddSource(CFRunLoopGetCurrent(), AXObserverGetRunLoopSource(observer), kCFRunLoopDefaultMode);
 
```

## Parameters

- `observer`: The observer object (created from a call to  ) for which to get the run loop source.

## See Also

- [func AXObserverAddNotification(AXObserver, AXUIElement, CFString, UnsafeMutableRawPointer?) -> AXError](1462089-axobserveraddnotification.md)
  Registers the specified observer to receive notifications from the specified accessibility object.
- [func AXObserverCreate(pid_t, AXObserverCallback, UnsafeMutablePointer<AXObserver?>) -> AXError](1460133-axobservercreate.md)
  Creates a new observer that can receive notifications from the specified application.
- [func AXObserverCreateWithInfoCallback(pid_t, AXObserverCallbackWithInfo, UnsafeMutablePointer<AXObserver?>) -> AXError](1460610-axobservercreatewithinfocallback.md)
  Creates a new observer that can receive notifications with an information dictionary from the specified application.
- [func AXObserverGetTypeID() -> CFTypeID](1461244-axobservergettypeid.md)
  Returns the unique type identifier for the AXObserverRef type.
- [func AXObserverRemoveNotification(AXObserver, AXUIElement, CFString) -> AXError](1462066-axobserverremovenotification.md)
  Removes the specified notification from the list of notifications the observer wants to receive from the accessibility object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applicationservices/1459139-axobservergetrunloopsource)*