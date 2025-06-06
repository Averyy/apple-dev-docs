# addMotionEffect(_:)

**Framework**: UIKit  
**Kind**: method

Begins applying a motion effect to the view.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func addMotionEffect(_ effect: UIMotionEffect)
```

#### Discussion

The system animates the transition to the motion effect’s values using the present [`UIView`](uiview.md) animation context. The motion effect’s keyPath/value pairs are applied to the view’s presentation layer.

## Parameters

- `effect`: The motion effect.

## See Also

- [var motionEffects: [UIMotionEffect]](uiview/motioneffects.md)
  The array of motion effects for the view.
- [func removeMotionEffect(UIMotionEffect)](uiview/removemotioneffect(_:).md)
  Stops applying a motion effect to the view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiview/addmotioneffect(_:))*