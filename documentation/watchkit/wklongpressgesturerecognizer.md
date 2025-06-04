# WKLongPressGestureRecognizer

**Framework**: Watchkit  
**Kind**: class

A gesture recognizer that interprets a touch event that occurs in the same relative area for an extended period of time.

**Availability**:
- watchOS 3.0+

## Declaration

```swift
class WKLongPressGestureRecognizer
```

## Overview

A long-press gesture is essentially a tap where the user’s finger remains on the screen for a minimum amount of time, which is configurable. You can configure the amount of time required for the long-press to be recognized and the maximum distance those touches are allowed to move before being disallowed.

You do not create instances of this class programmatically. Instead, add a long-press gesture recognizer to your Watch app’s storyboard file, dropping it onto a specific interface object. Touches occurring within the bounds of that interface object are tracked by the gesture recognizer and reported to an action method you define on the parent interface controller. For information on defining your action method and connecting it to your gesture recognizer, see [`WKGestureRecognizer`](https://developer.apple.com/documentation/watchkit/wkgesturerecognizer).

A long-press gesture recognizer tracks touch events continuously, and therefore has many potential state changes. A long-press gesture transitions to the Began state when the touch event is first detected. After that, the gesture recognizer may transition to the Changed state, the Ended, state, the Failed state, or the Cancelled state. The two most common state transition sequences are as follows:

- Possible → Began → [Changed…] → Ended
- Possible → Began → [Changed…] → Failed

The Changed state is optional and may occur multiple times before the Ended, Failed, or Cancelled state is reached. The gesture recognizer calls its action method at each state transition. For more information on implementing continuous gesture recognizers, see [`WKGestureRecognizer`](https://developer.apple.com/documentation/watchkit/wkgesturerecognizer).

Xcode lets you configure information about your gesture recognizer in your storyboard file. The following table lists the attributes you can configure in your storyboard and their meaning.

| r | o | w |
| --- | --- | --- |
| [{'inlineContent': [{'text': 'Attribute', 'type': 'text'}], 'type': 'paragraph'}] | [{'inlineContent': [{'type': 'text', 'text': 'Description'}], 'type': 'paragraph'}] |
| [{'inlineContent': [{'text': 'Min Duration', 'type': 'text'}], 'type': 'paragraph'}] | [{'inlineContent': [{'type': 'text', 'text': 'The minimum time (in seconds) that the user’s finger must touch the screen before the gesture can be recognized. You can set this value programmatically using the '}, {'type': 'reference', 'isActive': True, 'identifier': 'doc://com.apple.watchkit/documentation/WatchKit/WKLongPressGestureRecognizer/minimumPressDuration'}, {'type': 'text', 'text': ' property.'}], 'type': 'paragraph'}] |
| [{'inlineContent': [{'text': 'Taps', 'type': 'text'}], 'type': 'paragraph'}] | [{'inlineContent': [{'type': 'text', 'text': 'The number of long-press taps that must occur for the gesture to be recognized. Each tap must touch the screen for the minimum duration. You can set this value programmatically using the '}, {'isActive': True, 'type': 'reference', 'identifier': 'doc://com.apple.watchkit/documentation/WatchKit/WKLongPressGestureRecognizer/numberOfTapsRequired'}, {'type': 'text', 'text': ' property.'}], 'type': 'paragraph'}] |
| [{'inlineContent': [{'type': 'text', 'text': 'Movement'}], 'type': 'paragraph'}] | [{'inlineContent': [{'text': 'The amount of movement (in points) allowed for each touch event. Recognition of the gesture fails if any of the touch events moves by the specified amount or more. You can set this value programmatically using the ', 'type': 'text'}, {'isActive': True, 'identifier': 'doc://com.apple.watchkit/documentation/WatchKit/WKLongPressGestureRecognizer/allowableMovement', 'type': 'reference'}, {'text': ' property.', 'type': 'text'}], 'type': 'paragraph'}] |

The [`WKGestureRecognizer`](https://developer.apple.com/documentation/watchkit/wkgesturerecognizer) parent class also defines attributes that you can configure for your gesture recognizer. For information about those attributes, see [`WKGestureRecognizer`](https://developer.apple.com/documentation/watchkit/wkgesturerecognizer).

## Topics

### Configuring the Gesture Recognizer
- [var minimumPressDuration: CFTimeInterval](minimumpressduration.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wklongpressgesturerecognizer/minimumpressduration))
  The minimum amount of time (in seconds) that the user’s fingers must be touching the interface object.
- [var numberOfTapsRequired: Int](numberoftapsrequired.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wklongpressgesturerecognizer/numberoftapsrequired))
  The number of taps on the interface object that are required for the gesture to be recognized.
- [var allowableMovement: CGFloat](allowablemovement.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wklongpressgesturerecognizer/allowablemovement))
  The maximum movement of the finger on the interface object that allows the gesture to be recognized.

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
- [class WKPanGestureRecognizer](wkpangesturerecognizer.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkpangesturerecognizer))
- [class WKSwipeGestureRecognizer](wkswipegesturerecognizer.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkswipegesturerecognizer))
- [class WKTapGestureRecognizer](wktapgesturerecognizer.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wktapgesturerecognizer))


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wklongpressgesturerecognizer)*