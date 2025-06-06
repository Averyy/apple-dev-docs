# minimumValue

**Framework**: UIKit  
**Kind**: property

The lowest possible numeric value for the stepper.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var minimumValue: Double { get set }
```

#### Discussion

Must be numerically less than [`maximumValue`](uistepper/maximumvalue.md). If you attempt to set a value equal to or greater than [`maximumValue`](uistepper/maximumvalue.md), the system raises an [`invalidArgumentException`](https://developer.apple.com/documentation/foundation/nsexceptionname/1415426-invalidargumentexception) exception.

The default value for this property is `0`.

## See Also

- [var isContinuous: Bool](uistepper/iscontinuous.md)
  A Boolean value that determines whether to send value changes during user interaction or after user interaction ends.
- [var autorepeat: Bool](uistepper/autorepeat.md)
  A Boolean value that determines whether to repeatedly change the stepper’s value as the user presses and holds a stepper button.
- [var wraps: Bool](uistepper/wraps.md)
  A Boolean value that determines whether the stepper can wrap its value to the minimum or maximum value when incrementing and decrementing the value.
- [var maximumValue: Double](uistepper/maximumvalue.md)
  The highest possible numeric value for the stepper.
- [var stepValue: Double](uistepper/stepvalue.md)
  The step, or increment, value for the stepper.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uistepper/minimumvalue)*