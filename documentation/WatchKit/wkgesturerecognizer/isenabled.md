# isEnabled

**Framework**: WatchKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value indicating whether the gesture recognizer is enabled.

**Availability**:
- watchOS 3.0+

## Declaration

```swift
var isEnabled: Bool { get set }
```

```objc
@property (nonatomic, getter=isEnabled) BOOL enabled;
```

#### Discussion

When the value of this property is [`true`](../../Swift/true.md), the gesture recognizer actively tracks touches and reports state changes to its action method. When the value of this property is [`false`](../../Swift/false.md), the gesture recognizer does not track events or call its action method. The default value of this property is [`true`](../../Swift/true.md).

If you change the value of this property to [`false`](../../Swift/false.md) while the gesture recognizer is in the middle of tracking touch events, the gesture recognizer transitions to the [`WKGestureRecognizerState.cancelled`](../wkgesturerecognizerstate/cancelled.md) state.

## See Also

### Getting the Gesture Recognizer’s State
- [var state: WKGestureRecognizerState](./state.md)
  The current state of the gesture recognizer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkgesturerecognizer/isenabled)*