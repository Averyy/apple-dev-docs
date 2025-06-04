# delegate

**Framework**: Watchkit  
**Kind**: property

A delegate object for monitoring the session and responding to state changes and errors.

**Availability**:
- watchOS 6.0+

## Declaration

```swift
weak var delegate: (any WKExtendedRuntimeSessionDelegate)? { get set }
```

## Overview

To receive all the delegate calls, always assign a value to this property before calling the session’s [`start()`](https://developer.apple.com/documentation/watchkit/wkextendedruntimesession/start()) or [`start(at:)`](https://developer.apple.com/documentation/watchkit/wkextendedruntimesession/start(at:)) methods.

## See Also

- [protocol WKExtendedRuntimeSessionDelegate](wkextendedruntimesessiondelegate.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkextendedruntimesessiondelegate))


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkextendedruntimesession/delegate)*