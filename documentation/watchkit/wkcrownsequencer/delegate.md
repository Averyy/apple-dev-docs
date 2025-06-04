# delegate

**Framework**: WatchKit  
**Kind**: property

The object you use to monitor changes to the crown state.

**Availability**:
- watchOS 3.0+

## Declaration

```swift
weak var delegate: (any WKCrownDelegate)? { get set }
```

#### Discussion

Assign a delegate object to receive notifications about crown rotation events. For more information about receiving crown-related data, see [`WKCrownDelegate`](https://developer.apple.com/documentation/watchkit/wkcrowndelegate).


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkcrownsequencer/delegate)*