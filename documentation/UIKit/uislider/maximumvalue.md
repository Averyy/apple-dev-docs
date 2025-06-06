# maximumValue

**Framework**: UIKit  
**Kind**: property

The maximum value of the slider.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var maximumValue: Float { get set }
```

#### Discussion

Use this property to set the value that the trailing end of the slider represents. If you change the value of this property, and the current value of the slider is above the new maximum, the slider adjusts the [`value`](uislider/value.md) property to match the new maximum. If you set the maximum value to a value smaller than the minimum, the slider updates the minimum value to equal the maximum.

The default value of this property is 1.0.

## See Also

- [var minimumValue: Float](uislider/minimumvalue.md)
  The minimum value of the slider.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uislider/maximumvalue)*