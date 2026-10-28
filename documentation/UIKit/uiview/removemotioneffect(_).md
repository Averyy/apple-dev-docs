# removeMotionEffect(_:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Stops applying a motion effect to the view.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
func removeMotionEffect(_ effect: UIMotionEffect)
```

```objc
- (void) removeMotionEffect:(UIMotionEffect *) effect;
```

## Discussion

Any affected presentation values animate to their post-removal values using the present [`UIView`](../uiview.md) animation context.

## Parameters

- `effect`: The motion effect.

## See Also

### Using motion effects
- [func addMotionEffect(UIMotionEffect)](./addmotioneffect%28_%29.md)
  Begins applying a motion effect to the view.
- [var motionEffects: [UIMotionEffect]](./motioneffects.md)
  The array of motion effects for the view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiview/removemotioneffect(_:))*