# motionCancelled(_:with:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Tells the responder that a motion event has been canceled.

**Availability**:
- iOS 3.0+
- iPadOS 3.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
func motionCancelled(_ motion: UIEvent.EventSubtype, with event: UIEvent?)
```

```objc
- (void) motionCancelled:(UIEventSubtype) motion withEvent:(UIEvent *) event;
```

#### Discussion

UIKit calls this method when it receives an interruption requiring cancellation of the motion event. An interruption is anything that causes the application to become inactive or causes the view handling the motion events to be removed from its window. UIKit might also call this method if the shaking goes on too long. All responders that handle motion events should implement this method. In your implementation, clean up any state information associated with handling the motion events.

The default implementation of this method forwards the message up the responder chain.

## Parameters

- `motion`: An event-subtype constant indicating the kind of motion associated with `event`. A common motion is shaking, which is indicated by [`UIEvent.EventSubtype.motionShake`](../uievent/eventsubtype/motionshake.md).
- `event`: An object representing the event associated with the motion.

## See Also

### Responding to motion events
- [func motionBegan(UIEvent.EventSubtype, with: UIEvent?)](./motionbegan%28_,with%29.md)
  Tells the responder that a motion event has begun.
- [func motionEnded(UIEvent.EventSubtype, with: UIEvent?)](./motionended%28_,with%29.md)
  Tells the responder that a motion event has ended.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiresponder/motioncancelled(_:with:))*