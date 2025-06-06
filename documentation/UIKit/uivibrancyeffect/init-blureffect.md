# init(blurEffect:)

**Framework**: UIKit  
**Kind**: init

Creates a vibrancy effect for a specific blur effect.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
init(blurEffect: UIBlurEffect)
```

#### Return Value

The vibrancy effect to be used by a [`UIVisualEffectView`](uivisualeffectview.md) object.

#### Discussion

When you create a new vibrancy effect, use the same [`UIBlurEffect`](uiblureffect.md) that you used to create the blur view. Using a different [`UIBlurEffect`](uiblureffect.md) can cause unwanted visual effect combinations.

## Parameters

- `blurEffect`: The   used by the blurred view the vibrancy effect is attached to.

## See Also

- [init(forBlurEffect: UIBlurEffect, style: UIVibrancyEffectStyle)](uivibrancyeffect/init(forblureffect:style:).md)
  Creates a vibrancy effect with the specified blur and style values.
- [enum UIVibrancyEffectStyle](uivibrancyeffectstyle.md)
  Constants for the vibrancy styles.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uivibrancyeffect/init(blureffect:))*