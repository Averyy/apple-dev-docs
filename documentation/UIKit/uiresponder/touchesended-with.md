# touchesEnded(_:with:)

**Framework**: Uikit  
**Kind**: method

Tells the responder when one or more fingers are raised from a view or window.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func touchesEnded(_ touches: Set<UITouch>, with event: UIEvent?)
```

## Mentions

- [Implementing a Multi-Touch app](implementing-a-multi-touch-app.md)
- [Implementing a Discrete Gesture Recognizer](implementing-a-discrete-gesture-recognizer.md)
- [Implementing coalesced touch support in an app](implementing-coalesced-touch-support-in-an-app.md)
- [Implementing a Continuous Gesture Recognizer](implementing-a-continuous-gesture-recognizer.md)

#### Discussion

UIKit calls this method when a finger or Apple Pencil is no longer touching the screen. Many UIKit classes override this method and use it to clean up state involved in the handling of the corresponding touch events. The default implementation of this method forwards the message up the responder chain. When creating your own subclasses, call `super` to forward any events that you don’t handle yourself, like in the following code.

If you override this method without calling super (a common use pattern), you must also override the other methods for handling touch events, even if your implementations do nothing.

> **Note**:  In iOS 17, Messages allows you to interactively resize iMessage apps with a vertical pan gesture. Messages handles any conflicts between resize gestures and your custom gestures. If your app uses manual touch handling, override those methods in your app’s [`UIView`](uiview.md). You can either change your manual touch handling code to use a gesture recognizer instead, or your [`UIView`](uiview.md) can override [`gestureRecognizerShouldBegin(_:)`](uigesturerecognizerdelegate/gesturerecognizershouldbegin(_:).md) and return NO when your iMessage app doesn’t own the gesture.

## Parameters

- `touches`: A set of   instances that represent the touches for the ending phase of the event represented by  . For touches in a view, this set contains only one touch by default. To receive multiple touches, you must set the view’s   property to  .
- `event`: The event to which the touches belong.

## See Also

- [func touchesBegan(Set<UITouch>, with: UIEvent?)](uiresponder/touchesbegan(_:with:).md)
  Tells this object that one or more new touches occurred in a view or window.
- [func touchesMoved(Set<UITouch>, with: UIEvent?)](uiresponder/touchesmoved(_:with:).md)
  Tells the responder when one or more touches associated with an event changed.
- [func touchesCancelled(Set<UITouch>, with: UIEvent?)](uiresponder/touchescancelled(_:with:).md)
  Tells the responder when a system event (such as a system alert) cancels a touch sequence.
- [func touchesEstimatedPropertiesUpdated(Set<UITouch>)](uiresponder/touchesestimatedpropertiesupdated(_:).md)
  Tells the responder that updated values were received for previously estimated properties or that an update is no longer expected.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiresponder/touchesended(_:with:))*