# motionEnded(_:with:)

**Framework**: UIKit  
**Kind**: method

Tells the responder that a motion event has ended.

**Availability**:
- iOS 3.0+
- iPadOS 3.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func motionEnded(_ motion: UIEvent.EventSubtype, with event: UIEvent?)
```

#### Discussion

UIKit informs the responder only when a motion event starts and ends. It doesn’t report intermediate shakes. Motion events are delivered initially to the first responder and are forwarded up the responder chain as appropriate

The default implementation of this method forwards the message up the responder chain.

## Parameters

- `motion`: An event-subtype constant indicating the kind of motion. A common motion is shaking, which is indicated by  .
- `event`: An object representing the event associated with the motion.

## See Also

- [func motionBegan(UIEvent.EventSubtype, with: UIEvent?)](uiresponder/motionbegan(_:with:).md)
  Tells the responder that a motion event has begun.
- [func motionCancelled(UIEvent.EventSubtype, with: UIEvent?)](uiresponder/motioncancelled(_:with:).md)
  Tells the responder that a motion event has been canceled.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiresponder/motionended(_:with:))*