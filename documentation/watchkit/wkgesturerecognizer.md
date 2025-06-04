# WKGestureRecognizer

**Framework**: WatchKit  
**Kind**: class

The base class for all other gesture recognizer classes.

**Availability**:
- watchOS 3.0+

## Declaration

```swift
class WKGestureRecognizer
```

#### Overview

Gesture recognizers simplify the event-handling process by tracking touch events for you and calling your custom code when those events match a specific pattern. Gesture recognizers report the results of their tracking to an action method that you define.

You do not subclass [`WKGestureRecognizer`](https://developer.apple.com/documentation/watchkit/wkgesturerecognizer) or create instances of it directly. Instead, you add concrete gesture recognizer objects to your Watch app’s storyboard file and connect that gesture recognizer to your custom action method. At runtime, you use the methods of this class to get and set the state of your gesture recognizer. The concrete gesture recognizer classes are as follows:

- [`WKLongPressGestureRecognizer`](https://developer.apple.com/documentation/watchkit/wklongpressgesturerecognizer)
- [`WKPanGestureRecognizer`](https://developer.apple.com/documentation/watchkit/wkpangesturerecognizer)
- [`WKSwipeGestureRecognizer`](https://developer.apple.com/documentation/watchkit/wkswipegesturerecognizer)
- [`WKTapGestureRecognizer`](https://developer.apple.com/documentation/watchkit/wktapgesturerecognizer)

##### Executing Code in Response to a Gesture

A gesture recognizer has an associated action method that it calls during the recognition process to report on its progress. You define the action method in your interface controller and connect it to the gesture recognizer in Interface Builder. Action methods must conform to one of the following signatures:

The gesture recognizer calls your action method whenever the value in the [`state`](https://developer.apple.com/documentation/watchkit/wkgesturerecognizer/state) property changes in a significant way. All gesture recognizers start out in the [`WKGestureRecognizerState.possible`](https://developer.apple.com/documentation/watchkit/wkgesturerecognizerstate/possible) state and move to other states as appropriate based on the type of gesture. Gesture recognizers do not call your action method for every state change. For information about when the action method is called, see the constant descriptions of the [`WKGestureRecognizerState`](https://developer.apple.com/documentation/watchkit/wkgesturerecognizerstate) type.

watchOS supports two broad categories of gesture recognizers: continuous gesture recognizers and discrete gesture recognizer.

###### Continuous Gesture Recognizers

![None](https://docs-assets.developer.apple.com/published/eadbf2c2039e5658266f0bc849dbbbdc/media-2557562%402x.png)

Continuous gesture recognizers—for example, pan or long touch recognizers—track the user’s gesture and call the action method multiple times during a single gesture. They typically call the action method once when the gesture begins, one or more times as the gesture progresses, and once when the gesture either ends or is canceled. In your action method, use the gesture recognizer’s [`state`](https://developer.apple.com/documentation/watchkit/wkgesturerecognizer/state) property to perform appropriate tasks based on the current state. For example:

- [`WKGestureRecognizerState.began`](https://developer.apple.com/documentation/watchkit/wkgesturerecognizerstate/began). Alter the user interface’s appearance to indicate that a gesture has begun.
- [`WKGestureRecognizerState.changed`](https://developer.apple.com/documentation/watchkit/wkgesturerecognizerstate/changed). Update the user interface based on the current touch location.
- [`WKGestureRecognizerState.ended`](https://developer.apple.com/documentation/watchkit/wkgesturerecognizerstate/ended). Return to the normal user interface appearance, indicating that the gesture has ended. Keep any updates.
- [`WKGestureRecognizerState.cancelled`](https://developer.apple.com/documentation/watchkit/wkgesturerecognizerstate/cancelled). Return to the normal user interface appearance, indicating that the gesture has ended. Discard any updates.

###### Discrete Gesture Recognizers

![None](https://docs-assets.developer.apple.com/published/cb3692b76f000fb3b3a265280f7fdb70/media-2557566%402x.png)

Discrete gesture recognizers—for example, tap or swipe recognizers—only trigger a single event as soon as the gesture is recognized. For example, discrete recognizers call their action method when they enter the [`WKGestureRecognizerState.recognized`](https://developer.apple.com/documentation/watchkit/wkgesturerecognizerstate/recognized) state. If they enter the [`WKGestureRecognizerState.failed`](https://developer.apple.com/documentation/watchkit/wkgesturerecognizerstate/failed) state, they fail silently.

##### Interface Builder Attributes

Xcode lets you configure information about your gesture recognizer in your storyboard file. The following table lists the attributes you can configure in your storyboard and their meaning.

| Attribute | Description |
| --- | --- |
| State | A checkbox indicating whether the gesture recognizer is enabled. You can also configure this value programmatically using the [`isEnabled`](https://developer.apple.com/documentation/watchkit/wkgesturerecognizer/isenabled) property. |
| Behavior | Checkboxes indicating additional gesture recognizer behaviors. Use these options to specify how the gesture recognizer responds to touch events. |
| Must Fail First | Gesture recognizers that must fail before the current one can succeed. Drag from this option to the gesture recognizers in your storyboard file. |

## Topics

### Getting the Touch Information
- [func locationInObject() -> CGPoint](locationinobject().md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkgesturerecognizer/locationinobject()))
  Returns the point computed as the current position of the touch event.
- [func objectBounds() -> CGRect](objectbounds().md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkgesturerecognizer/objectbounds()))
  Returns the dimensions of the interface object (measured in points) associated with the gesture recognizer.
### Getting the Gesture Recognizer’s State
- [var state: WKGestureRecognizerState](state.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkgesturerecognizer/state))
  The current state of the gesture recognizer.
- [var isEnabled: Bool](isenabled.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkgesturerecognizer/isenabled))
  A Boolean value indicating whether the gesture recognizer is enabled.
### Constants
- [enum WKGestureRecognizerState](wkgesturerecognizerstate.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkgesturerecognizerstate))
  Constants describing the possible states of a gesture recognizer.

## Relationships

### Inherits From
- NSObject ([Apple Docs](https://developer.apple.com/documentation/ObjectiveC/NSObject-swift.class))
### Inherited By
- [WKLongPressGestureRecognizer](wklongpressgesturerecognizer.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wklongpressgesturerecognizer))
- [WKPanGestureRecognizer](wkpangesturerecognizer.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkpangesturerecognizer))
- [WKSwipeGestureRecognizer](wkswipegesturerecognizer.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkswipegesturerecognizer))
- [WKTapGestureRecognizer](wktapgesturerecognizer.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wktapgesturerecognizer))
### Conforms To
- CVarArg ([Apple Docs](https://developer.apple.com/documentation/Swift/CVarArg))
- CustomDebugStringConvertible ([Apple Docs](https://developer.apple.com/documentation/Swift/CustomDebugStringConvertible))
- CustomStringConvertible ([Apple Docs](https://developer.apple.com/documentation/Swift/CustomStringConvertible))
- Equatable ([Apple Docs](https://developer.apple.com/documentation/Swift/Equatable))
- Hashable ([Apple Docs](https://developer.apple.com/documentation/Swift/Hashable))
- NSObjectProtocol ([Apple Docs](https://developer.apple.com/documentation/ObjectiveC/NSObjectProtocol))

## See Also

- [class WKCrownSequencer](wkcrownsequencer.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkcrownsequencer))
  An object that reports the current state of the digital crown, including its rotational speed when it is in motion.
- [protocol WKCrownDelegate](wkcrowndelegate.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkcrowndelegate))
  A collection of methods you can implement to track the user’s interaction with the digital crown, receiving notifications when the user rotates the crown or when rotation stops.
- [class WKLongPressGestureRecognizer](wklongpressgesturerecognizer.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wklongpressgesturerecognizer))
  A gesture recognizer that interprets a touch event that occurs in the same relative area for an extended period of time.
- [class WKPanGestureRecognizer](wkpangesturerecognizer.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkpangesturerecognizer))
  A gesture recognizer that interprets a touch event that moves around the screen.
- [class WKSwipeGestureRecognizer](wkswipegesturerecognizer.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkswipegesturerecognizer))
  A gesture recognizer that interprets swiping gestures in one or more directions.
- [class WKTapGestureRecognizer](wktapgesturerecognizer.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wktapgesturerecognizer))
  A gesture recognizer that interprets a touch event occurring and ending in approximately the same area on the screen.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkgesturerecognizer)*