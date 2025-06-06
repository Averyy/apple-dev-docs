# UIVibrancyEffect

**Framework**: UIKit  
**Kind**: class

An object that amplifies and adjusts the color of the content layered behind a visual effect view.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
class UIVibrancyEffect
```

#### Overview

A vibrancy effect is intended to be used as a subview of or layered on top of a [`UIVisualEffectView`](uivisualeffectview.md) that has been configured with a [`UIBlurEffect`](uiblureffect.md). The use of a vibrancy effect can help the content placed inside the [`contentView`](uivisualeffectview/contentview.md) become more vivid.

The vibrancy effect is color-dependent. Any subviews that you add to the [`contentView`](uivisualeffectview/contentview.md) must implement the [`tintColorDidChange()`](uiview/tintcolordidchange().md) method and update themselves accordingly. [`UIImageView`](uiimageview.md) objects with images that have a rendering mode of [`UIImage.RenderingMode.alwaysTemplate`](uiimage/renderingmode-swift.enum/alwaystemplate.md) as well as [`UILabel`](uilabel.md) objects update automatically.

## Topics

### Creating a vibrancy effect
- [init(forBlurEffect: UIBlurEffect, style: UIVibrancyEffectStyle)](uivibrancyeffect/init(forblureffect:style:).md)
  Creates a vibrancy effect with the specified blur and style values.
- [init(blurEffect: UIBlurEffect)](uivibrancyeffect/init(blureffect:).md)
  Creates a vibrancy effect for a specific blur effect.
- [enum UIVibrancyEffectStyle](uivibrancyeffectstyle.md)
  Constants for the vibrancy styles.
### Deprecated
- [class func widgetPrimary() -> UIVibrancyEffect](uivibrancyeffect/widgetprimary.md)
  Creates a vibrancy effect suitable for use with certain supporting text and template images within a widget.
- [class func widgetSecondary() -> UIVibrancyEffect](uivibrancyeffect/widgetsecondary.md)
  Creates a vibrancy effect suitable for indicating the secondary importance or relevance of supporting text and template images within a widget.
- [class func widgetEffect(forVibrancyStyle: UIVibrancyEffectStyle) -> UIVibrancyEffect](uivibrancyeffect/widgeteffect(forvibrancystyle:).md)
  Creates a vibrancy effect for the specified style.
- [class func notificationCenter() -> UIVibrancyEffect](uivibrancyeffect/notificationcenter.md)
  Creates a vibrancy effect for use in Notification Center.

## Relationships

### Inherits From
- [UIVisualEffect](uivisualeffect.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSSecureCoding](../Foundation/NSSecureCoding.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [class UIVisualEffect](uivisualeffect.md)
  An initializer for visual effect views and blur and vibrancy effect objects.
- [class UIVisualEffectView](uivisualeffectview.md)
  An object that implements some complex visual effects.
- [class UIBlurEffect](uiblureffect.md)
  An object that applies a blurring effect to the content layered behind a visual effect view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uivibrancyeffect)*