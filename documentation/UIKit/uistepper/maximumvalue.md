# maximumValue

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The highest possible numeric value for the stepper.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
var maximumValue: Double { get set }
```

```objc
@property (nonatomic) double maximumValue;
```

## Discussion

Must be numerically greater than [`minimumValue`](./minimumvalue.md). If you attempt to set a value equal to or lower than [`minimumValue`](./minimumvalue.md), the system raises an [`invalidArgumentException`](../../Foundation/nsexceptionname/invalidargumentexception.md) exception.

The default value of this property is `100`.

## See Also

### Configuring the stepper
- [var isContinuous: Bool](./iscontinuous.md)
  A Boolean value that determines whether to send value changes during user interaction or after user interaction ends.
- [var autorepeat: Bool](./autorepeat.md)
  A Boolean value that determines whether to repeatedly change the stepper’s value as the user presses and holds a stepper button.
- [var wraps: Bool](./wraps.md)
  A Boolean value that determines whether the stepper can wrap its value to the minimum or maximum value when incrementing and decrementing the value.
- [var minimumValue: Double](./minimumvalue.md)
  The lowest possible numeric value for the stepper.
- [var stepValue: Double](./stepvalue.md)
  The step, or increment, value for the stepper.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uistepper/maximumvalue)*