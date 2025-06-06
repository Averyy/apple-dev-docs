# value

**Framework**: UIKit  
**Kind**: property

The numeric value of the stepper.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var value: Double { get set }
```

#### Discussion

When the value changes, the stepper sends the [`valueChanged`](uicontrol/event/valuechanged.md) flag to its target (see [`addTarget(_:action:for:)`](uicontrol/addtarget(_:action:for:).md)). Refer to the description of the [`isContinuous`](uistepper/iscontinuous.md) property for information about whether value change events are sent continuously or when user interaction ends.

The default value for this property is `0`. This property is clamped at its lower extreme to [`minimumValue`](uistepper/minimumvalue.md) and is clamped at its upper extreme to [`maximumValue`](uistepper/maximumvalue.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uistepper/value)*