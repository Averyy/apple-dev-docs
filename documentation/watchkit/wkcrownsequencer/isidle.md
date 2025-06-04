# isIdle

**Framework**: Watchkit  
**Kind**: property

A Boolean value indicating whether the crown is at rest.

**Availability**:
- watchOS 3.0+

## Declaration

```swift
var isIdle: Bool { get }
```

## Overview

The value of this property is [`true`](https://developer.apple.com/documentation/swift/true) when the user is not rotating the crown and [`false`](https://developer.apple.com/documentation/swift/false) when the user is rotating the crown.

## See Also

- [func crownDidBecomeIdle(WKCrownSequencer?)](crowndidbecomeidle(_:).md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkcrowndelegate/crowndidbecomeidle(_:)))
- [var rotationsPerSecond: Double](rotationspersecond.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkcrownsequencer/rotationspersecond))


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkcrownsequencer/isidle)*