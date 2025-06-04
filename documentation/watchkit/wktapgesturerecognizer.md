# WKTapGestureRecognizer

**Framework**: WatchKit  
**Kind**: class

A gesture recognizer that interprets a touch event occurring and ending in approximately the same area on the screen.

**Availability**:
- watchOS 3.0+

## Declaration

```swift
class WKTapGestureRecognizer
```

#### Overview

The tap gesture recognizer can report when a single tap happens or when multiple taps happen.

You do not create instances of this class programmatically. Instead, add a tap gesture recognizer to your Watch appʼs storyboard file, dropping it onto a specific interface object. The gesture recognizer tracks touches that occur within the bounds of that interface object and reports to an action method you define on the parent interface controller. For information on defining your action method and connecting it to your gesture recognizer, see [`WKGestureRecognizer`](wkgesturerecognizer.md).

##### State Changes for a Tap Gesture

A tap gesture recognizer tracks discrete events, and therefore has a limited number of state changes. Each tap in a tap gesture comprises the user touching the screen and then lifting the finger off the screen in about the same location and within a preset amount of time. Gesture recognition occurs when the user performs the specified number of taps. The state transition sequences for a tap gesture are as follows:

![Possible state is Recognized or Failed](https://docs-assets.developer.apple.com/published/cb3692b76f000fb3b3a265280f7fdb70/media-3591359%402x.png)

The gesture recognizer calls its action method when it enters the [`WKGestureRecognizerState.recognized`](wkgesturerecognizerstate/recognized.md) state. You can determine the location of the tap by calling its [`locationInObject()`](wkgesturerecognizer/locationinobject().md) method. For more information on implementing discrete gesture recognizers, see [`WKGestureRecognizer`](wkgesturerecognizer.md).

##### Interface Builder Attributes

Xcode lets you configure information about your gesture recognizer in your storyboard file. The following table lists the attributes you can configure in your storyboard and their meanings.

| Attribute | Description |
| --- | --- |
| Taps | The number of taps necessary to complete the gesture. You can set this value using the [`numberOfTapsRequired`](wktapgesturerecognizer/numberoftapsrequired.md) property. |

The [`WKGestureRecognizer`](wkgesturerecognizer.md) parent class also defines attributes that you can configure for your gesture recognizer. For information about those attributes, see [`WKGestureRecognizer`](wkgesturerecognizer.md).

## Topics

### Configuring the Gesture
- [var numberOfTapsRequired: Int](wktapgesturerecognizer/numberoftapsrequired.md)
  The number of taps necessary for gesture recognition.

## Relationships

### Inherits From
- [WKGestureRecognizer](wkgesturerecognizer.md)
### Conforms To
- [CVarArg](https://developer.apple.com/documentation/Swift/CVarArg)
- [CustomDebugStringConvertible](https://developer.apple.com/documentation/Swift/CustomDebugStringConvertible)
- [CustomStringConvertible](https://developer.apple.com/documentation/Swift/CustomStringConvertible)
- [Equatable](https://developer.apple.com/documentation/Swift/Equatable)
- [Hashable](https://developer.apple.com/documentation/Swift/Hashable)
- [NSObjectProtocol](https://developer.apple.com/documentation/ObjectiveC/NSObjectProtocol)

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
- [class WKSwipeGestureRecognizer](wkswipegesturerecognizer.md)
  A gesture recognizer that interprets swiping gestures in one or more directions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wktapgesturerecognizer)*