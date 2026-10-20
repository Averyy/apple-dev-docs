# value

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The numeric value of the stepper.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
var value: Double { get set }
```

```objc
@property (nonatomic) double value;
```

#### Discussion

When the value changes, the stepper sends the [`valueChanged`](../uicontrol/event/valuechanged.md) flag to its target (see [`addTarget(_:action:for:)`](../uicontrol/addtarget%28_,action,for%29.md)). Refer to the description of the [`isContinuous`](./iscontinuous.md) property for information about whether value change events are sent continuously or when user interaction ends.

The default value for this property is `0`. This property is clamped at its lower extreme to [`minimumValue`](./minimumvalue.md) and is clamped at its upper extreme to [`maximumValue`](./maximumvalue.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uistepper/value)*