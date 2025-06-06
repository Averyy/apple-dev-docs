# value

**Framework**: UIKit  
**Kind**: property

The slider’s current value.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var value: Float { get set }
```

#### Discussion

Use this property to get and set the slider’s current value. To render an animated transition from the current value to the new value, use the [`setValue(_:animated:)`](uislider/setvalue(_:animated:).md) method instead.

If you try to set a value that’s below the minimum or above the maximum, the minimum or maximum value is set instead. The default value of this property is `0.0`.

## See Also

- [func setValue(Float, animated: Bool)](uislider/setvalue(_:animated:).md)
  Sets the slider’s current value, allowing you to animate the change visually.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uislider/value)*