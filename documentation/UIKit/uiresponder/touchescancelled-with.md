# touchesCancelled(_:with:)

**Framework**: UIKit  
**Kind**: method

Tells the responder when a system event (such as a system alert) cancels a touch sequence.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func touchesCancelled(_ touches: Set<UITouch>, with event: UIEvent?)
```

## Mentions

- [Implementing a Multi-Touch app](implementing-a-multi-touch-app.md)
- [Implementing coalesced touch support in an app](implementing-coalesced-touch-support-in-an-app.md)
- [Implementing a Discrete Gesture Recognizer](implementing-a-discrete-gesture-recognizer.md)
- [About the Gesture Recognizer State Machine](about-the-gesture-recognizer-state-machine.md)
- [Implementing a Continuous Gesture Recognizer](implementing-a-continuous-gesture-recognizer.md)

#### Discussion

UIKit calls this method when it receives a system interruption requiring cancellation of the touch sequence. An interruption is anything that causes the application to become inactive or causes the view handling the touch events to be removed from its window. Your implementation of this method should clean up any state associated with handling the touch sequence. The default implementation of this method forwards the message up the responder chain. When creating your own subclasses, call `super` to forward any events that you don’t handle yourself, like in the following code.

If you override this method without calling `super` (a common use pattern), you must also override the other methods for handling touch events, if only as stub (empty) implementations.

## Parameters

- `touches`: A set of   instances that represent the touches for the ending phase of the event represented by  . For touches in a view, this set contains only one touch by default. To receive multiple touches, you must set the view’s   property to  .
- `event`: The event to which the touches belong.

## See Also

- [func touchesBegan(Set<UITouch>, with: UIEvent?)](uiresponder/touchesbegan(_:with:).md)
  Tells this object that one or more new touches occurred in a view or window.
- [func touchesMoved(Set<UITouch>, with: UIEvent?)](uiresponder/touchesmoved(_:with:).md)
  Tells the responder when one or more touches associated with an event changed.
- [func touchesEnded(Set<UITouch>, with: UIEvent?)](uiresponder/touchesended(_:with:).md)
  Tells the responder when one or more fingers are raised from a view or window.
- [func touchesEstimatedPropertiesUpdated(Set<UITouch>)](uiresponder/touchesestimatedpropertiesupdated(_:).md)
  Tells the responder that updated values were received for previously estimated properties or that an update is no longer expected.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiresponder/touchescancelled(_:with:))*