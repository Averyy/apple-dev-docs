# WKCrownSequencer

**Framework**: WatchKit  
**Kind**: class

An object that reports the current state of the digital crown, including its rotational speed when it is in motion.

**Availability**:
- watchOS 3.0+

## Declaration

```swift
class WKCrownSequencer
```

#### Overview

Do not create instances of this class yourself. Instead, retrieve a crown sequencer object from the current interface controller’s [`crownSequencer`](https://developer.apple.com/documentation/watchkit/wkinterfacecontroller/crownsequencer) property. Before the sequencer can receive data, you must call its [`focus()`](https://developer.apple.com/documentation/watchkit/wkcrownsequencer/focus()) method. Only one object in your interface can have focus at any given time, so if your interface also contains picker objects or has scrollable scenes, you must coordinate changes in focus accordingly. For example, calling the sequencer’s [`focus()`](https://developer.apple.com/documentation/watchkit/wkcrownsequencer/focus()) method causes any picker objects or interface controllers to resign focus. When the user taps on a picker object, the currently active sequencer resigns focus, and the selected picker object gains the focus. Because the crown sequencer is not tied to a specific interface object, you can use it as general input for your app.

Although the crown sequencer object has properties that contain the current state of the crown, it is more common to use a [`delegate`](https://developer.apple.com/documentation/watchkit/wkcrownsequencer/delegate) object to receive notifications as the user rotates the crown. For more information on receiving data using a delegate, see [`WKCrownDelegate`](https://developer.apple.com/documentation/watchkit/wkcrowndelegate).

## Topics

### Getting the Current Crown Status
- [var rotationsPerSecond: Double](rotationspersecond.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkcrownsequencer/rotationspersecond))
  The rotational speed of the crown, measured in rotations per second.
- [var isIdle: Bool](isidle.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkcrownsequencer/isidle))
  A Boolean value indicating whether the crown is at rest.
### Accessing the Delegate
- [var delegate: (any WKCrownDelegate)?](delegate.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkcrownsequencer/delegate))
  The object you use to monitor changes to the crown state.
### Managing the Focus
- [func focus()](focus().md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkcrownsequencer/focus()))
  Begins the delivery of crown events to the current crown sequencer.
- [func resignFocus()](resignfocus().md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkcrownsequencer/resignfocus()))
  Ends the delivery of crown events to the current crown sequencer.
### Managing Haptic Feedback
- [var isHapticFeedbackEnabled: Bool](ishapticfeedbackenabled.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkcrownsequencer/ishapticfeedbackenabled))
  A Boolean value that determines whether the crown sequencer’s haptic feedback is enabled.

## Relationships

### Inherits From
- NSObject ([Apple Docs](https://developer.apple.com/documentation/ObjectiveC/NSObject-swift.class))
### Conforms To
- CVarArg ([Apple Docs](https://developer.apple.com/documentation/Swift/CVarArg))
- CustomDebugStringConvertible ([Apple Docs](https://developer.apple.com/documentation/Swift/CustomDebugStringConvertible))
- CustomStringConvertible ([Apple Docs](https://developer.apple.com/documentation/Swift/CustomStringConvertible))
- Equatable ([Apple Docs](https://developer.apple.com/documentation/Swift/Equatable))
- Hashable ([Apple Docs](https://developer.apple.com/documentation/Swift/Hashable))
- NSObjectProtocol ([Apple Docs](https://developer.apple.com/documentation/ObjectiveC/NSObjectProtocol))

## See Also

- [protocol WKCrownDelegate](wkcrowndelegate.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkcrowndelegate))
  A collection of methods you can implement to track the user’s interaction with the digital crown, receiving notifications when the user rotates the crown or when rotation stops.
- [class WKGestureRecognizer](wkgesturerecognizer.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkgesturerecognizer))
  The base class for all other gesture recognizer classes.
- [class WKLongPressGestureRecognizer](wklongpressgesturerecognizer.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wklongpressgesturerecognizer))
  A gesture recognizer that interprets a touch event that occurs in the same relative area for an extended period of time.
- [class WKPanGestureRecognizer](wkpangesturerecognizer.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkpangesturerecognizer))
  A gesture recognizer that interprets a touch event that moves around the screen.
- [class WKSwipeGestureRecognizer](wkswipegesturerecognizer.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkswipegesturerecognizer))
  A gesture recognizer that interprets swiping gestures in one or more directions.
- [class WKTapGestureRecognizer](wktapgesturerecognizer.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wktapgesturerecognizer))
  A gesture recognizer that interprets a touch event occurring and ending in approximately the same area on the screen.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkcrownsequencer)*