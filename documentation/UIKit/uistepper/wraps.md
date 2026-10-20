# wraps

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that determines whether the stepper can wrap its value to the minimum or maximum value when incrementing and decrementing the value.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
var wraps: Bool { get set }
```

```objc
@property (nonatomic) BOOL wraps;
```

#### Discussion

If [`true`](../../Swift/true.md), incrementing beyond [`maximumValue`](./maximumvalue.md) sets [`value`](./value.md) to [`minimumValue`](./minimumvalue.md); likewise, decrementing below [`minimumValue`](./minimumvalue.md) sets [`value`](./value.md) to [`maximumValue`](./maximumvalue.md). If [`false`](../../Swift/false.md), the stepper doesn’t increment beyond [`maximumValue`](./maximumvalue.md) nor does it decrement below [`minimumValue`](./minimumvalue.md) but rather holds at those values.

The default value for this property is [`false`](../../Swift/false.md).

## See Also

### Configuring the stepper
- [var isContinuous: Bool](./iscontinuous.md)
  A Boolean value that determines whether to send value changes during user interaction or after user interaction ends.
- [var autorepeat: Bool](./autorepeat.md)
  A Boolean value that determines whether to repeatedly change the stepper’s value as the user presses and holds a stepper button.
- [var minimumValue: Double](./minimumvalue.md)
  The lowest possible numeric value for the stepper.
- [var maximumValue: Double](./maximumvalue.md)
  The highest possible numeric value for the stepper.
- [var stepValue: Double](./stepvalue.md)
  The step, or increment, value for the stepper.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uistepper/wraps)*