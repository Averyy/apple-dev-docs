# WKSwipeGestureRecognizer

**Framework**: WatchKit  
**Kind**: class

A gesture recognizer that interprets swiping gestures in one or more directions.

**Availability**:
- watchOS 3.0+

## Declaration

```swift
class WKSwipeGestureRecognizer
```

#### Overview

A swipe is a discrete gesture; the associated action message is sent only once per gesture.

You do not create instances of this class programmatically. Instead, add a swipe gesture recognizer to your Watch app’s storyboard file, dropping it onto a specific interface object. Touches occurring within the bounds of that interface object are tracked by the gesture recognizer and reported to an action method you define on the parent interface controller. For information on defining your action method and connecting it to your gesture recognizer, see [`WKGestureRecognizer`](wkgesturerecognizer.md).

##### State Changes for a Swipe Gesture

A swipe gesture recognizer tracks discrete events, and therefore has a limited number of state changes. The swipe gesture is recognized when a single touch has moved mostly in an allowable direction far enough to be considered a swipe. Swipes can be slow or fast. A slow swipe requires high directional precision but a small distance; a fast swipe requires low directional precision but a large distance.

![Possible state is Recognized or Failed](https://docs-assets.developer.apple.com/published/cb3692b76f000fb3b3a265280f7fdb70/media-3591360%402x.png)

The gesture recognizer calls its action method when it enters the [`WKGestureRecognizerState.recognized`](wkgesturerecognizerstate/recognized.md) state. You may determine the location where a swipe began by calling its [`locationInObject()`](wkgesturerecognizer/locationinobject().md) method. For more information on implementing discrete gesture recognizers, see [`WKGestureRecognizer`](wkgesturerecognizer.md).

##### Interface Builder Attributes

Xcode lets you configure information about your gesture recognizer in your storyboard file. The following table lists the attributes you can configure in your storyboard and their meaning.

| Attribute | Description |
| --- | --- |
| Swipe | The direction of the swipe. The swipe must occur in this direction for the gesture to be recognized. You can set this value programmatically using the [`direction`](wkswipegesturerecognizer/direction.md) property. |

The [`WKGestureRecognizer`](wkgesturerecognizer.md) parent class also defines attributes that you can configure for your gesture recognizer. For information about those attributes, see [`WKGestureRecognizer`](wkgesturerecognizer.md).

## Topics

### Configuring the Gesture Recognizer
- [var direction: WKSwipeGestureRecognizerDirection](wkswipegesturerecognizer/direction.md)
  The permitted directions of the swipe.
### Constants
- [struct WKSwipeGestureRecognizerDirection](wkswipegesturerecognizerdirection.md)
  Constants indicating the direction of a swipe.

## Relationships

### Inherits From
- [WKGestureRecognizer](wkgesturerecognizer.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class WKCrownSequencer](wkcrownsequencer.md)
  An object that reports the current state of the digital crown, including its rotational speed when it is in motion.
- [protocol WKCrownDelegate](wkcrowndelegate.md)
  A collection of methods you can implement to track the user’s interaction with the digital crown, receiving notifications when the user rotates the crown or when rotation stops.
- [class WKGestureRecognizer](wkgesturerecognizer.md)
  The base class for all other gesture recognizer classes.
- [class WKLongPressGestureRecognizer](wklongpressgesturerecognizer.md)
  A gesture recognizer that interprets a touch event that occurs in the same relative area for an extended period of time.
- [class WKPanGestureRecognizer](wkpangesturerecognizer.md)
  A gesture recognizer that interprets a touch event that moves around the screen.
- [class WKTapGestureRecognizer](wktapgesturerecognizer.md)
  A gesture recognizer that interprets a touch event occurring and ending in approximately the same area on the screen.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkswipegesturerecognizer)*