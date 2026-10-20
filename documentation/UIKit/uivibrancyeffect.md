# UIVibrancyEffect

**Framework**: UIKit  
**Kind**: class  
**Role**: Class

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

```objc
@interface UIVibrancyEffect : UIVisualEffect
```

#### Overview

A vibrancy effect is intended to be used as a subview of or layered on top of a [`UIVisualEffectView`](./uivisualeffectview.md) that has been configured with a [`UIBlurEffect`](./uiblureffect.md). The use of a vibrancy effect can help the content placed inside the [`contentView`](./uivisualeffectview/contentview.md) become more vivid.

The vibrancy effect is color-dependent. Any subviews that you add to the [`contentView`](./uivisualeffectview/contentview.md) must implement the [`tintColorDidChange()`](./uiview/tintcolordidchange%28%29.md) method and update themselves accordingly. [`UIImageView`](./uiimageview.md) objects with images that have a rendering mode of [`UIImage.RenderingMode.alwaysTemplate`](./uiimage/renderingmode-swift.enum/alwaystemplate.md) as well as [`UILabel`](./uilabel.md) objects update automatically.

## Topics

### Creating a vibrancy effect
- [init(forBlurEffect: UIBlurEffect, style: UIVibrancyEffectStyle)](./uivibrancyeffect/init%28forblureffect,style%29.md)
  Creates a vibrancy effect with the specified blur and style values.
- [init(blurEffect: UIBlurEffect)](./uivibrancyeffect/init%28blureffect%29.md)
  Creates a vibrancy effect for a specific blur effect.
- [enum UIVibrancyEffectStyle](./uivibrancyeffectstyle.md)
  Constants for the vibrancy styles.
### Deprecated
- [class func widgetPrimary() -> UIVibrancyEffect](./uivibrancyeffect/widgetprimary%28%29.md)
  Creates a vibrancy effect suitable for use with certain supporting text and template images within a widget.
- [class func widgetSecondary() -> UIVibrancyEffect](./uivibrancyeffect/widgetsecondary%28%29.md)
  Creates a vibrancy effect suitable for indicating the secondary importance or relevance of supporting text and template images within a widget.
- [class func widgetEffect(forVibrancyStyle: UIVibrancyEffectStyle) -> UIVibrancyEffect](./uivibrancyeffect/widgeteffect%28forvibrancystyle%29.md)
  Creates a vibrancy effect for the specified style.
- [class func notificationCenter() -> UIVibrancyEffect](./uivibrancyeffect/notificationcenter%28%29.md)
  Creates a vibrancy effect for use in Notification Center.
### Initializers
- [init(blurEffect: UIBlurEffect, style: UIVibrancyEffectStyle)](./uivibrancyeffect/init%28blureffect,style%29.md)
- [init(forBlurEffect: UIBlurEffect)](./uivibrancyeffect/init%28forblureffect%29.md)
### Default Implementations
- [UIVibrancyEffect Implementations](./uivibrancyeffect/uivibrancyeffect-implementations.md)

## Relationships

### Inherits From
- [UIVisualEffect](./uivisualeffect.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCoding](../Foundation/nscoding.md)
- [NSCopying](../Foundation/nscopying.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [NSSecureCoding](../Foundation/nssecurecoding.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Visual effects
- [class UIVisualEffect](./uivisualeffect.md)
  An initializer for visual effect views and blur and vibrancy effect objects.
- [class UIVisualEffectView](./uivisualeffectview.md)
  An object that implements some complex visual effects.
- [class UIBlurEffect](./uiblureffect.md)
  An object that applies a blurring effect to the content layered behind a visual effect view.
- [class UIColorEffect](./uicoloreffect.md)
  A visual effect that applies a solid color background.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uivibrancyeffect)*