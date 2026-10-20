# init(blurEffect:)

**Framework**: UIKit  
**Kind**: init  
**Role**: Initializer

Creates a vibrancy effect for a specific blur effect.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
init(blurEffect: UIBlurEffect)
```

```objc
+ (UIVibrancyEffect *) effectForBlurEffect:(UIBlurEffect *) blurEffect;
```

#### Return Value

The vibrancy effect to be used by a [`UIVisualEffectView`](../uivisualeffectview.md) object.

#### Discussion

When you create a new vibrancy effect, use the same [`UIBlurEffect`](../uiblureffect.md) that you used to create the blur view. Using a different [`UIBlurEffect`](../uiblureffect.md) can cause unwanted visual effect combinations.

## Parameters

- `blurEffect`: The [`UIBlurEffect`](../uiblureffect.md) used by the blurred view the vibrancy effect is attached to.

## See Also

### Creating a vibrancy effect
- [init(forBlurEffect: UIBlurEffect, style: UIVibrancyEffectStyle)](./init%28forblureffect,style%29.md)
  Creates a vibrancy effect with the specified blur and style values.
- [enum UIVibrancyEffectStyle](../uivibrancyeffectstyle.md)
  Constants for the vibrancy styles.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uivibrancyeffect/init(blureffect:))*