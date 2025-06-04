# WKCrownDelegate

**Framework**: Watchkit  
**Kind**: protocol

A collection of methods you can implement to track the user’s interaction with the digital crown, receiving notifications when the user rotates the crown or when rotation stops.

**Availability**:
- watchOS 3.0+

## Declaration

```swift
protocol WKCrownDelegate : NSObjectProtocol
```

## Topics

### Receiving Crown Events
- [func crownDidRotate(WKCrownSequencer?, rotationalDelta: Double)](crowndidrotate(_:rotationaldelta:).md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkcrowndelegate/crowndidrotate(_:rotationaldelta:)))
  Called when the user rotates the crown.
- [func crownDidBecomeIdle(WKCrownSequencer?)](crowndidbecomeidle(_:).md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkcrowndelegate/crowndidbecomeidle(_:)))
  Called when the user stops rotating the crown.

## Relationships

### Inherits From
- NSObjectProtocol ([Apple Docs](https://developer.apple.com/documentation/ObjectiveC/NSObjectProtocol))

## See Also

- [class WKCrownSequencer](wkcrownsequencer.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkcrownsequencer))
- [class WKGestureRecognizer](wkgesturerecognizer.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkgesturerecognizer))
- [class WKLongPressGestureRecognizer](wklongpressgesturerecognizer.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wklongpressgesturerecognizer))
- [class WKPanGestureRecognizer](wkpangesturerecognizer.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkpangesturerecognizer))
- [class WKSwipeGestureRecognizer](wkswipegesturerecognizer.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkswipegesturerecognizer))
- [class WKTapGestureRecognizer](wktapgesturerecognizer.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wktapgesturerecognizer))


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkcrowndelegate)*