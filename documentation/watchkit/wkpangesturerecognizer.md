# WKPanGestureRecognizer

**Framework**: Watchkit  
**Kind**: class

A gesture recognizer that interprets a touch event that moves around the screen.

**Availability**:
- watchOS 3.0+

## Declaration

```swift
class WKPanGestureRecognizer
```

#### Overview

In watchOS, a pan gesture must track exactly one touch event, but that touch event may move freely. Pan gestures are often used to drag content around a given area.

You do not create instances of this class programmatically. Instead, add a pan gesture recognizer to your Watch app’s storyboard file, dropping it onto a specific interface object. Touches occurring within the bounds of that interface object are tracked by the gesture recognizer and reported to an action method you define on the parent interface controller. For information on defining your action method and connecting it to your gesture recognizer, see [`WKGestureRecognizer`](wkgesturerecognizer.md).

##### State Changes for a Pan Gesture

![None](https://docs-assets.developer.apple.com/published/eadbf2c2039e5658266f0bc849dbbbdc/media-2557623%402x.png)

A pan gesture recognizer tracks touch events continuously, and therefore has many potential state changes. A pan gesture does not transition to the Began state until after the touch event starts moving. After that, it may transition to the Changed state, to the Ended, state, to the Failed state, or to the Cancelled state. The two most common state transition sequences are as follows:

- Possible —> Began —> [Changed…] —> Ended
- Possible —> Began —> [Changed…] —> Failed

The Changed state is optional and may occur multiple times before the Ended, Failed, or Cancelled state is reached. The gesture recognizer calls its action method at each state transition. For more information on implementing continuous gesture recognizers, see [`WKGestureRecognizer`](wkgesturerecognizer.md).

##### Interface Builder Attributes

Xcode lets you configure information about your gesture recognizer in your storyboard file. A pan gesture recognizer defines no attributes of its own, but you can configure attributes of the [`WKGestureRecognizer`](wkgesturerecognizer.md) parent class. For information about those attributes, see [`WKGestureRecognizer`](wkgesturerecognizer.md).

## Topics

### Tracking the Location and Velocity of the Gesture
- [func translationInObject() -> CGPoint](wkpangesturerecognizer/translationinobject.md)
  The amount of translation for the pan gesture in the current object.
- [func velocityInObject() -> CGPoint](wkpangesturerecognizer/velocityinobject.md)
  The velocity of the pan gesture in the current object.

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
- [class WKSwipeGestureRecognizer](wkswipegesturerecognizer.md)
  A gesture recognizer that interprets swiping gestures in one or more directions.
- [class WKTapGestureRecognizer](wktapgesturerecognizer.md)
  A gesture recognizer that interprets a touch event occurring and ending in approximately the same area on the screen.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkpangesturerecognizer)*