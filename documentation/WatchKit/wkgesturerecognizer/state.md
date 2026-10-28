# state

**Framework**: WatchKit  
**Kind**: property  
**Role**: Instance Property

The current state of the gesture recognizer.

**Availability**:
- watchOS 3.0+

## Declaration

```swift
var state: WKGestureRecognizerState { get }
```

```objc
@property (nonatomic, readonly) WKGestureRecognizerState state;
```

## Discussion

As the gesture recognizer processes touch events, it updates the value of this property. Some states apply only to gestures that comprise a continuous sequences of touch events that must be tracked over time, such as pan gestures.

## See Also

### Getting the Gesture Recognizer’s State
- [var isEnabled: Bool](./isenabled.md)
  A Boolean value indicating whether the gesture recognizer is enabled.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkgesturerecognizer/state)*