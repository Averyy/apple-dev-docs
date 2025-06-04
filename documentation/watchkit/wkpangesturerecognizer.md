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

## Overview

In watchOS, a pan gesture must track exactly one touch event, but that touch event may move freely. Pan gestures are often used to drag content around a given area.

You do not create instances of this class programmatically. Instead, add a pan gesture recognizer to your Watch app’s storyboard file, dropping it onto a specific interface object. Touches occurring within the bounds of that interface object are tracked by the gesture recognizer and reported to an action method you define on the parent interface controller. For information on defining your action method and connecting it to your gesture recognizer, see [`WKGestureRecognizer`](https://developer.apple.com/documentation/watchkit/wkgesturerecognizer).

A pan gesture recognizer tracks touch events continuously, and therefore has many potential state changes. A pan gesture does not transition to the Began state until after the touch event starts moving. After that, it may transition to the Changed state, to the Ended, state, to the Failed state, or to the Cancelled state. The two most common state transition sequences are as follows:

- Possible —> Began —> [Changed…] —> Ended
- Possible —> Began —> [Changed…] —> Failed

The Changed state is optional and may occur multiple times before the Ended, Failed, or Cancelled state is reached. The gesture recognizer calls its action method at each state transition. For more information on implementing continuous gesture recognizers, see [`WKGestureRecognizer`](https://developer.apple.com/documentation/watchkit/wkgesturerecognizer).

Xcode lets you configure information about your gesture recognizer in your storyboard file. A pan gesture recognizer defines no attributes of its own, but you can configure attributes of the [`WKGestureRecognizer`](https://developer.apple.com/documentation/watchkit/wkgesturerecognizer) parent class. For information about those attributes, see [`WKGestureRecognizer`](https://developer.apple.com/documentation/watchkit/wkgesturerecognizer).

## Topics

### Tracking the Location and Velocity of the Gesture
- [func translationInObject() -> CGPoint](translationinobject().md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkpangesturerecognizer/translationinobject()))
  The amount of translation for the pan gesture in the current object.
- [func velocityInObject() -> CGPoint](velocityinobject().md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkpangesturerecognizer/velocityinobject()))
  The velocity of the pan gesture in the current object.

## Relationships

### Inherits From
- [WKGestureRecognizer](wkgesturerecognizer.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkgesturerecognizer))
### Conforms To
- CVarArg ([Apple Docs](https://developer.apple.com/documentation/Swift/CVarArg))
- CustomDebugStringConvertible ([Apple Docs](https://developer.apple.com/documentation/Swift/CustomDebugStringConvertible))
- CustomStringConvertible ([Apple Docs](https://developer.apple.com/documentation/Swift/CustomStringConvertible))
- Equatable ([Apple Docs](https://developer.apple.com/documentation/Swift/Equatable))
- Hashable ([Apple Docs](https://developer.apple.com/documentation/Swift/Hashable))
- NSObjectProtocol ([Apple Docs](https://developer.apple.com/documentation/ObjectiveC/NSObjectProtocol))

## See Also

- [class WKCrownSequencer](wkcrownsequencer.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkcrownsequencer))
- [protocol WKCrownDelegate](wkcrowndelegate.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkcrowndelegate))
- [class WKGestureRecognizer](wkgesturerecognizer.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkgesturerecognizer))
- [class WKLongPressGestureRecognizer](wklongpressgesturerecognizer.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wklongpressgesturerecognizer))
- [class WKSwipeGestureRecognizer](wkswipegesturerecognizer.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkswipegesturerecognizer))
- [class WKTapGestureRecognizer](wktapgesturerecognizer.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wktapgesturerecognizer))


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkpangesturerecognizer)*