# notificationCenter()

**Framework**: UIKit  
**Kind**: method  
**Role**: Type Method

Creates a vibrancy effect for use in Notification Center.

**Availability**:
- iOS 8.0+ - Deprecated in 10.0
- iPadOS 8.0+ - Deprecated in 10.0

> **Deprecated**: Use [`widgetPrimary()`](./widgetprimary%28%29.md) instead.

## Declaration

```swift
class func notificationCenter() -> UIVibrancyEffect
```

```objc
+ (UIVibrancyEffect *) notificationCenterVibrancyEffect;
```

#### Return Value

The vibrancy effect that’s appropriate for use in Today widgets in Notification Center. To learn more about Today widgets, see [Today](https://developer.apple.com/library/archive/documentation/General/Conceptual/ExtensibilityPG/Today.html#//apple_ref/doc/uid/TP40014214-CH11).

## See Also

### Deprecated
- [class func widgetPrimary() -> UIVibrancyEffect](./widgetprimary%28%29.md)
  Creates a vibrancy effect suitable for use with certain supporting text and template images within a widget.
- [class func widgetSecondary() -> UIVibrancyEffect](./widgetsecondary%28%29.md)
  Creates a vibrancy effect suitable for indicating the secondary importance or relevance of supporting text and template images within a widget.
- [class func widgetEffect(forVibrancyStyle: UIVibrancyEffectStyle) -> UIVibrancyEffect](./widgeteffect%28forvibrancystyle%29.md)
  Creates a vibrancy effect for the specified style.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uivibrancyeffect/notificationcenter())*