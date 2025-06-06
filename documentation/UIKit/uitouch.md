# UITouch

**Framework**: UIKit  
**Kind**: class

An object representing the location, size, movement, and force of a touch occurring on the screen.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
class UITouch
```

## Mentions

- [Using responders and the responder chain to handle events](using-responders-and-the-responder-chain-to-handle-events.md)
- [Implementing a Continuous Gesture Recognizer](implementing-a-continuous-gesture-recognizer.md)
- [Implementing a Discrete Gesture Recognizer](implementing-a-discrete-gesture-recognizer.md)
- [Implementing a Multi-Touch app](implementing-a-multi-touch-app.md)
- [Computing the perpendicular force of Apple Pencil](computing-the-perpendicular-force-of-apple-pencil.md)

#### Overview

You access touch objects through [`UIEvent`](uievent.md) objects passed into responder objects for event handling. A touch object includes accessors for:

- The view or window in which the touch occurred
- The location of the touch within the view or window
- The approximate radius of the touch
- The force of the touch (on devices that support 3D Touch or Apple Pencil)

A touch object also contains a timestamp indicating when the touch occurred, an integer representing the number of times the user tapped the screen, and the phase of the touch in the form of a constant that describes whether the touch began, moved, or ended, or whether the system canceled the touch.

To learn how to work with swipes, read [`Handling Swipe and Drag Gestures`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/EventHandling/Conceptual/EventHandlingiPhoneOS/multitouch_background/multitouch_background.html#//apple_ref/doc/uid/TP40009541-CH5-SW21) in [`Event Handling Guide for UIKit Apps`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/EventHandling/Conceptual/EventHandlingiPhoneOS/index.html#//apple_ref/doc/uid/TP40009541).

A touch object persists throughout a multi-touch sequence. You may store a reference to a touch while handling a multi-touch sequence, as long as you release that reference when the sequence ends. If you need to store information about a touch outside of a multi-touch sequence, copy that information from the touch.

The [`gestureRecognizers`](uitouch/gesturerecognizers.md) property of a touch contains the gesture recognizers currently handling the touch. Each gesture recognizer is an instance of a concrete subclass of [`UIGestureRecognizer`](uigesturerecognizer.md).

## Topics

### Getting the location of a touch
- [func location(in: UIView?) -> CGPoint](uitouch/location(in:)-8rd36.md)
  Returns the current location of the touch in the coordinate system of the given view.
- [func previousLocation(in: UIView?) -> CGPoint](uitouch/previouslocation(in:)-22sws.md)
  Returns the previous location of the touch in the coordinate system of the given view.
- [var view: UIView?](uitouch/view.md)
  The view to which touches are being delivered, if any.
- [var window: UIWindow?](uitouch/window.md)
  The window in which the touch initially occurred.
- [var majorRadius: CGFloat](uitouch/majorradius.md)
  The radius (in points) of the touch.
- [var majorRadiusTolerance: CGFloat](uitouch/majorradiustolerance.md)
  The tolerance (in points) of the touch’s radius.
- [func preciseLocation(in: UIView?) -> CGPoint](uitouch/preciselocation(in:).md)
  Returns a precise location for the touch, when available.
- [func precisePreviousLocation(in: UIView?) -> CGPoint](uitouch/precisepreviouslocation(in:).md)
  Returns a precise previous location for the touch, when available.
### Getting touch attributes
- [var tapCount: Int](uitouch/tapcount.md)
  The number of times the finger was tapped for this given touch.
- [var timestamp: TimeInterval](uitouch/timestamp.md)
  The time when the touch occurred or when it was last mutated.
- [var type: UITouch.TouchType](uitouch/type.md)
  The type of the touch.
- [UITouch.TouchType](uitouch/touchtype.md)
  The type of touch received.
- [var phase: UITouch.Phase](uitouch/phase-swift.property.md)
  The phase of the touch.
- [UITouch.Phase](uitouch/phase-swift.enum.md)
  The phase of a touch event.
- [var force: CGFloat](uitouch/force.md)
  The force of the touch, where a value of `1.0` represents the force of an average touch (predetermined by the system, not user-specific).
- [var maximumPossibleForce: CGFloat](uitouch/maximumpossibleforce.md)
  The maximum possible force for a touch.
- [var altitudeAngle: CGFloat](uitouch/altitudeangle.md)
  The altitude (in radians) of the stylus.
- [func azimuthAngle(in: UIView?) -> CGFloat](uitouch/azimuthangle(in:).md)
  Returns the azimuth angle (in radians) of the stylus.
- [func azimuthUnitVector(in: UIView?) -> CGVector](uitouch/azimuthunitvector(in:).md)
  Returns a unit vector that points in the direction of the azimuth of the stylus.
- [var rollAngle: CGFloat](uitouch/rollangle.md)
  A value that represents the current barrel-roll angle of Apple Pencil.
### Managing estimated touch attributes
- [var estimatedProperties: UITouch.Properties](uitouch/estimatedproperties.md)
  A set of touch properties whose values contain only estimates.
- [var estimatedPropertiesExpectingUpdates: UITouch.Properties](uitouch/estimatedpropertiesexpectingupdates.md)
  The set of touch properties for which updated values are expected in the future.
- [UITouch.Properties](uitouch/properties.md)
  A bit mask of touch properties that may get updated.
- [var estimationUpdateIndex: NSNumber?](uitouch/estimationupdateindex.md)
  An index number that lets you correlate an updated touch with the original touch.
### Getting a touch object’s gesture recognizers
- [var gestureRecognizers: [UIGestureRecognizer]?](uitouch/gesturerecognizers.md)
  The gesture recognizers that are receiving the touch object.
### Working with touch events in SpriteKit
- [func location(in: SKNode) -> CGPoint](uitouch/location(in:)-44h4k.md)
  Returns the current location of the touch in the coordinate system of the given node.
- [func previousLocation(in: SKNode) -> CGPoint](uitouch/previouslocation(in:)-ea29.md)
  Returns the previous location of the touch in the coordinate system of the given node.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [Handling touches in your view](handling-touches-in-your-view.md)
  Use touch events directly on a view subclass if touch handling is intricately linked to the view’s content.
- [Handling input from Apple Pencil](handling-input-from-apple-pencil.md)
  Learn how to detect and respond to touches from Apple Pencil.
- [Tracking the force of 3D Touch events](tracking-the-force-of-3d-touch-events.md)
  Manipulate your content based on the force of touches.
- [Illustrating the force, altitude, and azimuth properties of touch input](illustrating-the-force-altitude-and-azimuth-properties-of-touch-input.md)
  Capture Apple Pencil and touch input in views.
- [Leveraging touch input for drawing apps](leveraging-touch-input-for-drawing-apps.md)
  Capture touches as a series of strokes and render them efficiently on a drawing canvas.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitouch)*