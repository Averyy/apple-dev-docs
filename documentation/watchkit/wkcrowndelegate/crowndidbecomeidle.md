# crownDidBecomeIdle(_:)

**Framework**: Watchkit  
**Kind**: method

Called when the user stops rotating the crown.

**Availability**:
- watchOS 3.0+

## Declaration

```swift
optional func crownDidBecomeIdle(_ crownSequencer: WKCrownSequencer?)
```

## Overview

The crown sequencer calls this method when the crown finally comes to rest. The sequencer calls this method only after one or more calls to the [`crownDidRotate(_:rotationalDelta:)`](https://developer.apple.com/documentation/watchkit/wkcrowndelegate/crowndidrotate(_:rotationaldelta:)) method.

## Parameters

- `crownSequencer`: The crown sequencer object reporting the change.

## See Also

- [var isIdle: Bool](isidle.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkcrownsequencer/isidle))
- [func crownDidRotate(WKCrownSequencer?, rotationalDelta: Double)](crowndidrotate(_:rotationaldelta:).md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkcrowndelegate/crowndidrotate(_:rotationaldelta:)))


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkcrowndelegate/crowndidbecomeidle(_:))*