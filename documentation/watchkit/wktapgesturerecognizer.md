# WKTapGestureRecognizer

**Framework**: Watchkit  
**Kind**: class

A gesture recognizer that interprets a touch event occurring and ending in approximately the same area on the screen.

**Availability**:
- watchOS 3.0+

## Declaration

```swift
class WKTapGestureRecognizer
```

## Overview

The tap gesture recognizer can report when a single tap happens or when multiple taps happen.

You do not create instances of this class programmatically. Instead, add a tap gesture recognizer to your Watch appʼs storyboard file, dropping it onto a specific interface object. The gesture recognizer tracks touches that occur within the bounds of that interface object and reports to an action method you define on the parent interface controller. For information on defining your action method and connecting it to your gesture recognizer, see [`WKGestureRecognizer`](https://developer.apple.com/documentation/watchkit/wkgesturerecognizer).

A tap gesture recognizer tracks discrete events, and therefore has a limited number of state changes. Each tap in a tap gesture comprises the user touching the screen and then lifting the finger off the screen in about the same location and within a preset amount of time. Gesture recognition occurs when the user performs the specified number of taps. The state transition sequences for a tap gesture are as follows:

The gesture recognizer calls its action method when it enters the [`WKGestureRecognizerState.recognized`](https://developer.apple.com/documentation/watchkit/wkgesturerecognizerstate/recognized) state. You can determine the location of the tap by calling its [`locationInObject()`](https://developer.apple.com/documentation/watchkit/wkgesturerecognizer/locationinobject()) method. For more information on implementing discrete gesture recognizers, see [`WKGestureRecognizer`](https://developer.apple.com/documentation/watchkit/wkgesturerecognizer).

Xcode lets you configure information about your gesture recognizer in your storyboard file. The following table lists the attributes you can configure in your storyboard and their meanings.

| r | o | w |
| --- | --- | --- |
| [{'type': 'paragraph', 'inlineContent': [{'text': 'Attribute', 'type': 'text'}]}] | [{'type': 'paragraph', 'inlineContent': [{'text': 'Description', 'type': 'text'}]}] |
| [{'type': 'paragraph', 'inlineContent': [{'text': 'Taps', 'type': 'text'}]}] | [{'type': 'paragraph', 'inlineContent': [{'type': 'text', 'text': 'The number of taps necessary to complete the gesture. You can set this value using the '}, {'type': 'reference', 'isActive': True, 'identifier': 'doc://com.apple.watchkit/documentation/WatchKit/WKTapGestureRecognizer/numberOfTapsRequired'}, {'type': 'text', 'text': ' property.'}]}] |

The [`WKGestureRecognizer`](https://developer.apple.com/documentation/watchkit/wkgesturerecognizer) parent class also defines attributes that you can configure for your gesture recognizer. For information about those attributes, see [`WKGestureRecognizer`](https://developer.apple.com/documentation/watchkit/wkgesturerecognizer).

## Topics

### Configuring the Gesture
- [var numberOfTapsRequired: Int](numberoftapsrequired.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wktapgesturerecognizer/numberoftapsrequired))
  The number of taps necessary for gesture recognition.

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
- [class WKSwipeGestureRecognizer](wkswipegesturerecognizer.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkswipegesturerecognizer))


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wktapgesturerecognizer)*