# widgetEffect(forVibrancyStyle:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Type Method

Creates a vibrancy effect for the specified style.

**Availability**:
- iOS 13.0+ - Deprecated in 14.0
- iPadOS 13.0+ - Deprecated in 14.0

> **Deprecated**: Use [`init(forBlurEffect:style:)`](./init%28forblureffect,style%29.md) instead.

## Declaration

```swift
class func widgetEffect(forVibrancyStyle vibrancyStyle: UIVibrancyEffectStyle) -> UIVibrancyEffect
```

```objc
+ (UIVibrancyEffect *) widgetEffectForVibrancyStyle:(UIVibrancyEffectStyle) vibrancyStyle;
```

## See Also

### Deprecated
- [class func widgetPrimary() -> UIVibrancyEffect](./widgetprimary%28%29.md)
  Creates a vibrancy effect suitable for use with certain supporting text and template images within a widget.
- [class func widgetSecondary() -> UIVibrancyEffect](./widgetsecondary%28%29.md)
  Creates a vibrancy effect suitable for indicating the secondary importance or relevance of supporting text and template images within a widget.
- [class func notificationCenter() -> UIVibrancyEffect](./notificationcenter%28%29.md)
  Creates a vibrancy effect for use in Notification Center.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uivibrancyeffect/widgeteffect(forvibrancystyle:))*