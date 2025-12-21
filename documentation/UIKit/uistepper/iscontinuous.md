# isContinuous

**Framework**: UIKit  
**Kind**: property

A Boolean value that determines whether to send value changes during user interaction or after user interaction ends.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var isContinuous: Bool { get set }
```

#### Discussion

If [`true`](https://developer.apple.com/documentation/Swift/true), the stepper sends value change events immediately as the value changes during user interaction. If [`false`](https://developer.apple.com/documentation/Swift/false), the stepper sends a value change event after user interaction ends.

The default value for this property is [`true`](https://developer.apple.com/documentation/Swift/true).

## See Also

- [var autorepeat: Bool](uistepper/autorepeat.md)
  A Boolean value that determines whether to repeatedly change the stepper’s value as the user presses and holds a stepper button.
- [var wraps: Bool](uistepper/wraps.md)
  A Boolean value that determines whether the stepper can wrap its value to the minimum or maximum value when incrementing and decrementing the value.
- [var minimumValue: Double](uistepper/minimumvalue.md)
  The lowest possible numeric value for the stepper.
- [var maximumValue: Double](uistepper/maximumvalue.md)
  The highest possible numeric value for the stepper.
- [var stepValue: Double](uistepper/stepvalue.md)
  The step, or increment, value for the stepper.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uistepper/iscontinuous)*