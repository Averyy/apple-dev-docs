# removeMotionEffect(_:)

**Framework**: UIKit  
**Kind**: method

Stops applying a motion effect to the view.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func removeMotionEffect(_ effect: UIMotionEffect)
```

#### Discussion

Any affected presentation values animate to their post-removal values using the present [`UIView`](uiview.md) animation context.

## Parameters

- `effect`: The motion effect.

## See Also

- [func addMotionEffect(UIMotionEffect)](uiview/addmotioneffect(_:).md)
  Begins applying a motion effect to the view.
- [var motionEffects: [UIMotionEffect]](uiview/motioneffects.md)
  The array of motion effects for the view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiview/removemotioneffect(_:))*