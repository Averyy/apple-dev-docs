# minimumValue

**Framework**: UIKit  
**Kind**: property

The minimum value of the slider.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var minimumValue: Float { get set }
```

#### Discussion

Use this property to set the value that the leading end of the slider represents. If you change the value of this property, and the current value of the slider is below the new minimum, the slider adjusts the [`value`](uislider/value.md) property to match the new minimum. If you set the minimum value to a value larger than the maximum, the slider updates the maximum value to equal the minimum.

The default value of this property is 0.0.

## See Also

- [var maximumValue: Float](uislider/maximumvalue.md)
  The maximum value of the slider.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uislider/minimumvalue)*