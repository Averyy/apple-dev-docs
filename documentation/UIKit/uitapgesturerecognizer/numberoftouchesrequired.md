# numberOfTouchesRequired

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The number of fingers that the user must tap for gesture recognition.

**Availability**:
- iOS 3.2+
- iPadOS 3.2+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
var numberOfTouchesRequired: Int { get set }
```

```objc
@property (nonatomic) NSUInteger numberOfTouchesRequired;
```

## Mentions

- [Handling tap gestures](../handling-tap-gestures.md)

#### Discussion

The default value is 1.

## See Also

### Configuring the gesture
- [var buttonMaskRequired: UIEvent.ButtonMask](./buttonmaskrequired.md)
  The bit mask of the buttons the user must press for gesture recognition.
- [var numberOfTapsRequired: Int](./numberoftapsrequired.md)
  The number of taps necessary for gesture recognition.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitapgesturerecognizer/numberoftouchesrequired)*