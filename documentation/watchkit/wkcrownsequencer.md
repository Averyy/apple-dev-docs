# WKCrownSequencer

**Framework**: Watchkit  
**Kind**: class

An object that reports the current state of the digital crown, including its rotational speed when it is in motion.

**Availability**:
- watchOS 3.0+

## Declaration

```swift
class WKCrownSequencer
```

#### Overview

Do not create instances of this class yourself. Instead, retrieve a crown sequencer object from the current interface controller’s [`crownSequencer`](wkinterfacecontroller/crownsequencer.md) property. Before the sequencer can receive data, you must call its [`focus()`](wkcrownsequencer/focus().md) method. Only one object in your interface can have focus at any given time, so if your interface also contains picker objects or has scrollable scenes, you must coordinate changes in focus accordingly. For example, calling the sequencer’s [`focus()`](wkcrownsequencer/focus().md) method causes any picker objects or interface controllers to resign focus. When the user taps on a picker object, the currently active sequencer resigns focus, and the selected picker object gains the focus. Because the crown sequencer is not tied to a specific interface object, you can use it as general input for your app.

Although the crown sequencer object has properties that contain the current state of the crown, it is more common to use a [`delegate`](wkcrownsequencer/delegate.md) object to receive notifications as the user rotates the crown. For more information on receiving data using a delegate, see [`WKCrownDelegate`](wkcrowndelegate.md).

## Topics

### Getting the Current Crown Status
- [var rotationsPerSecond: Double](wkcrownsequencer/rotationspersecond.md)
  The rotational speed of the crown, measured in rotations per second.
- [var isIdle: Bool](wkcrownsequencer/isidle.md)
  A Boolean value indicating whether the crown is at rest.
### Accessing the Delegate
- [var delegate: (any WKCrownDelegate)?](wkcrownsequencer/delegate.md)
  The object you use to monitor changes to the crown state.
### Managing the Focus
- [func focus()](wkcrownsequencer/focus.md)
  Begins the delivery of crown events to the current crown sequencer.
- [func resignFocus()](wkcrownsequencer/resignfocus.md)
  Ends the delivery of crown events to the current crown sequencer.
### Managing Haptic Feedback
- [var isHapticFeedbackEnabled: Bool](wkcrownsequencer/ishapticfeedbackenabled.md)
  A Boolean value that determines whether the crown sequencer’s haptic feedback is enabled.

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

## See Also

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
- [class WKTapGestureRecognizer](wktapgesturerecognizer.md)
  A gesture recognizer that interprets a touch event occurring and ending in approximately the same area on the screen.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkcrownsequencer)*