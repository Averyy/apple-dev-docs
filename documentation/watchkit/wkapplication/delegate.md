# delegate

**Framework**: Watchkit  
**Kind**: property

The delegate of the WatchKit app object.

**Availability**:
- watchOS 7.0+

## Declaration

```swift
@MainActor weak var delegate: (any WKApplicationDelegate)? { get }
```

## Overview

The delegate object is an object that conforms to the [`WKApplicationDelegate`](https://developer.apple.com/documentation/watchkit/wkapplicationdelegate) protocol. You provide the delegate object and use it to manage lifecycle events in your extension. Providing a delegate object is required if your extension supports actionable notifications or Handoff behaviors.

For more information about the methods of the delegate object, see [`WKApplicationDelegate`](https://developer.apple.com/documentation/watchkit/wkapplicationdelegate).

## See Also

- [protocol WKApplicationDelegate](wkapplicationdelegate.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkapplicationdelegate))


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkapplication/delegate)*