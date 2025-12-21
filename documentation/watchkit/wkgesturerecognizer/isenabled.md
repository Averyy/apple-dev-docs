# isEnabled

**Framework**: WatchKit  
**Kind**: property

A Boolean value indicating whether the gesture recognizer is enabled.

**Availability**:
- watchOS 3.0+

## Declaration

```swift
var isEnabled: Bool { get set }
```

#### Discussion

When the value of this property is [`true`](https://developer.apple.com/documentation/Swift/true), the gesture recognizer actively tracks touches and reports state changes to its action method. When the value of this property is [`false`](https://developer.apple.com/documentation/Swift/false), the gesture recognizer does not track events or call its action method. The default value of this property is [`true`](https://developer.apple.com/documentation/Swift/true).

If you change the value of this property to [`false`](https://developer.apple.com/documentation/Swift/false) while the gesture recognizer is in the middle of tracking touch events, the gesture recognizer transitions to the [`WKGestureRecognizerState.cancelled`](wkgesturerecognizerstate/cancelled.md) state.

## See Also

- [var state: WKGestureRecognizerState](wkgesturerecognizer/state.md)
  The current state of the gesture recognizer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkgesturerecognizer/isenabled)*