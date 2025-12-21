# wraps

**Framework**: UIKit  
**Kind**: property

A Boolean value that determines whether the stepper can wrap its value to the minimum or maximum value when incrementing and decrementing the value.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var wraps: Bool { get set }
```

#### Discussion

If [`true`](https://developer.apple.com/documentation/Swift/true), incrementing beyond [`maximumValue`](uistepper/maximumvalue.md) sets [`value`](uistepper/value.md) to [`minimumValue`](uistepper/minimumvalue.md); likewise, decrementing below [`minimumValue`](uistepper/minimumvalue.md) sets [`value`](uistepper/value.md) to [`maximumValue`](uistepper/maximumvalue.md). If [`false`](https://developer.apple.com/documentation/Swift/false), the stepper doesn’t increment beyond [`maximumValue`](uistepper/maximumvalue.md) nor does it decrement below [`minimumValue`](uistepper/minimumvalue.md) but rather holds at those values.

The default value for this property is [`false`](https://developer.apple.com/documentation/Swift/false).

## See Also

- [var isContinuous: Bool](uistepper/iscontinuous.md)
  A Boolean value that determines whether to send value changes during user interaction or after user interaction ends.
- [var autorepeat: Bool](uistepper/autorepeat.md)
  A Boolean value that determines whether to repeatedly change the stepper’s value as the user presses and holds a stepper button.
- [var minimumValue: Double](uistepper/minimumvalue.md)
  The lowest possible numeric value for the stepper.
- [var maximumValue: Double](uistepper/maximumvalue.md)
  The highest possible numeric value for the stepper.
- [var stepValue: Double](uistepper/stepvalue.md)
  The step, or increment, value for the stepper.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uistepper/wraps)*