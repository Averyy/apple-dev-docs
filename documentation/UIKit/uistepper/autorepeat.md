# autorepeat

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that determines whether to repeatedly change the stepper’s value as the user presses and holds a stepper button.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
var autorepeat: Bool { get set }
```

```objc
@property (nonatomic) BOOL autorepeat;
```

## Discussion

If [`true`](../../Swift/true.md), the user pressing and holding on the stepper repeatedly alters [`value`](./value.md).

The default value for this property is [`true`](../../Swift/true.md).

## See Also

### Configuring the stepper
- [var isContinuous: Bool](./iscontinuous.md)
  A Boolean value that determines whether to send value changes during user interaction or after user interaction ends.
- [var wraps: Bool](./wraps.md)
  A Boolean value that determines whether the stepper can wrap its value to the minimum or maximum value when incrementing and decrementing the value.
- [var minimumValue: Double](./minimumvalue.md)
  The lowest possible numeric value for the stepper.
- [var maximumValue: Double](./maximumvalue.md)
  The highest possible numeric value for the stepper.
- [var stepValue: Double](./stepvalue.md)
  The step, or increment, value for the stepper.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uistepper/autorepeat)*