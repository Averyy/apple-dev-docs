# buttonMaskRequired

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The bit mask of the buttons the user must press for gesture recognition.

**Availability**:
- iOS 13.4+
- iPadOS 13.4+
- Mac Catalyst 13.4+
- visionOS 1.0+

## Declaration

```swift
var buttonMaskRequired: UIEvent.ButtonMask { get set }
```

```objc
@property (nonatomic) UIEventButtonMask buttonMaskRequired;
```

## See Also

### Configuring the gesture
- [var numberOfTapsRequired: Int](./numberoftapsrequired.md)
  The number of taps necessary for gesture recognition.
- [var numberOfTouchesRequired: Int](./numberoftouchesrequired.md)
  The number of fingers that the user must tap for gesture recognition.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitapgesturerecognizer/buttonmaskrequired)*