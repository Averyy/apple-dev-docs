# init(forBlurEffect:style:)

**Framework**: UIKit  
**Kind**: init

Creates a vibrancy effect with the specified blur and style values.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
init(blurEffect: UIBlurEffect, style: UIVibrancyEffectStyle)
```

#### Return Value

The vibrancy effect object to use in your visual effect view.

#### Discussion

When you create a new vibrancy effect, use the same [`UIBlurEffect`](uiblureffect.md) that you used to create the blur view. Using a different [`UIBlurEffect`](uiblureffect.md) can cause unwanted visual effect combinations.

## Parameters

- `blurEffect`: The   used by the blurred view the vibrancy effect is attached to.
- `style`: The style that defines what level of vibrancy to apply to the content. For a list of possible values, see  .

## See Also

- [init(blurEffect: UIBlurEffect)](uivibrancyeffect/init(blureffect:).md)
  Creates a vibrancy effect for a specific blur effect.
- [enum UIVibrancyEffectStyle](uivibrancyeffectstyle.md)
  Constants for the vibrancy styles.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uivibrancyeffect/init(forblureffect:style:))*