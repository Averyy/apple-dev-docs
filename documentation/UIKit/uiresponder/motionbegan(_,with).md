# motionBegan(_:with:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Tells the responder that a motion event has begun.

**Availability**:
- iOS 3.0+
- iPadOS 3.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
func motionBegan(_ motion: UIEvent.EventSubtype, with event: UIEvent?)
```

```objc
- (void) motionBegan:(UIEventSubtype) motion withEvent:(UIEvent *) event;
```

## Discussion

UIKit informs the responder only when a motion event starts and ends. It doesn’t report intermediate shakes. Motion events are delivered initially to the first responder and are forwarded up the responder chain as appropriate.

The default implementation of this method forwards the message up the responder chain.

## Parameters

- `motion`: An event-subtype constant indicating the kind of motion. A common motion is shaking, which is indicated by [`UIEvent.EventSubtype.motionShake`](../uievent/eventsubtype/motionshake.md).
- `event`: An object representing the event associated with the motion.

## See Also

### Responding to motion events
- [func motionEnded(UIEvent.EventSubtype, with: UIEvent?)](./motionended%28_,with%29.md)
  Tells the responder that a motion event has ended.
- [func motionCancelled(UIEvent.EventSubtype, with: UIEvent?)](./motioncancelled%28_,with%29.md)
  Tells the responder that a motion event has been canceled.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiresponder/motionbegan(_:with:))*