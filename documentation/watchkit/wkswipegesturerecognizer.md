# WKSwipeGestureRecognizer

**Framework**: Watchkit  
**Kind**: class

A gesture recognizer that interprets swiping gestures in one or more directions.

**Availability**:
- watchOS 3.0+

## Declaration

```swift
class WKSwipeGestureRecognizer
```

## Overview

A swipe is a discrete gesture; the associated action message is sent only once per gesture.

You do not create instances of this class programmatically. Instead, add a swipe gesture recognizer to your Watch app’s storyboard file, dropping it onto a specific interface object. Touches occurring within the bounds of that interface object are tracked by the gesture recognizer and reported to an action method you define on the parent interface controller. For information on defining your action method and connecting it to your gesture recognizer, see [`WKGestureRecognizer`](https://developer.apple.com/documentation/watchkit/wkgesturerecognizer).

A swipe gesture recognizer tracks discrete events, and therefore has a limited number of state changes. The swipe gesture is recognized when a single touch has moved mostly in an allowable direction far enough to be considered a swipe. Swipes can be slow or fast. A slow swipe requires high directional precision but a small distance; a fast swipe requires low directional precision but a large distance.

The gesture recognizer calls its action method when it enters the [`WKGestureRecognizerState.recognized`](https://developer.apple.com/documentation/watchkit/wkgesturerecognizerstate/recognized) state. You may determine the location where a swipe began by calling its [`locationInObject()`](https://developer.apple.com/documentation/watchkit/wkgesturerecognizer/locationinobject()) method. For more information on implementing discrete gesture recognizers, see [`WKGestureRecognizer`](https://developer.apple.com/documentation/watchkit/wkgesturerecognizer).

Xcode lets you configure information about your gesture recognizer in your storyboard file. The following table lists the attributes you can configure in your storyboard and their meaning.

| r | o | w |
| --- | --- | --- |
| [{'type': 'paragraph', 'inlineContent': [{'type': 'text', 'text': 'Attribute'}]}] | [{'type': 'paragraph', 'inlineContent': [{'type': 'text', 'text': 'Description'}]}] |
| [{'type': 'paragraph', 'inlineContent': [{'type': 'text', 'text': 'Swipe'}]}] | [{'type': 'paragraph', 'inlineContent': [{'type': 'text', 'text': 'The direction of the swipe. The swipe must occur in this direction for the gesture to be recognized. You can set this value programmatically using the '}, {'identifier': 'doc://com.apple.watchkit/documentation/WatchKit/WKSwipeGestureRecognizer/direction', 'type': 'reference', 'isActive': True}, {'type': 'text', 'text': ' property.'}]}] |

The [`WKGestureRecognizer`](https://developer.apple.com/documentation/watchkit/wkgesturerecognizer) parent class also defines attributes that you can configure for your gesture recognizer. For information about those attributes, see [`WKGestureRecognizer`](https://developer.apple.com/documentation/watchkit/wkgesturerecognizer).

## Topics

### Configuring the Gesture Recognizer
- [var direction: WKSwipeGestureRecognizerDirection](direction.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkswipegesturerecognizer/direction))
  The permitted directions of the swipe.
### Constants
- [struct WKSwipeGestureRecognizerDirection](wkswipegesturerecognizerdirection.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkswipegesturerecognizerdirection))
  Constants indicating the direction of a swipe.

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
- [class WKPanGestureRecognizer](wkpangesturerecognizer.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkpangesturerecognizer))
- [class WKTapGestureRecognizer](wktapgesturerecognizer.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wktapgesturerecognizer))


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkswipegesturerecognizer)*