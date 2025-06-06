# motionCancelled(_:with:)

**Framework**: UIKit  
**Kind**: method

Tells the responder that a motion event has been canceled.

**Availability**:
- iOS 3.0+
- iPadOS 3.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func motionCancelled(_ motion: UIEvent.EventSubtype, with event: UIEvent?)
```

#### Discussion

UIKit calls this method when it receives an interruption requiring cancellation of the motion event. An interruption is anything that causes the application to become inactive or causes the view handling the motion events to be removed from its window. UIKit might also call this method if the shaking goes on too long. All responders that handle motion events should implement this method. In your implementation, clean up any state information associated with handling the motion events.

The default implementation of this method forwards the message up the responder chain.

## Parameters

- `motion`: An event-subtype constant indicating the kind of motion associated with  . A common motion is shaking, which is indicated by  .
- `event`: An object representing the event associated with the motion.

## See Also

- [func motionBegan(UIEvent.EventSubtype, with: UIEvent?)](uiresponder/motionbegan(_:with:).md)
  Tells the responder that a motion event has begun.
- [func motionEnded(UIEvent.EventSubtype, with: UIEvent?)](uiresponder/motionended(_:with:).md)
  Tells the responder that a motion event has ended.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiresponder/motioncancelled(_:with:))*