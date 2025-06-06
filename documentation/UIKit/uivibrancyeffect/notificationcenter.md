# notificationCenter()

**Framework**: UIKit  
**Kind**: method

Creates a vibrancy effect for use in Notification Center.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+

## Declaration

```swift
@MainActor
class func notificationCenter() -> UIVibrancyEffect
```

#### Return Value

The vibrancy effect that’s appropriate for use in Today widgets in Notification Center. To learn more about Today widgets, see [`Today`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/General/Conceptual/ExtensibilityPG/Today.html#//apple_ref/doc/uid/TP40014214-CH11).

## See Also

- [class func widgetPrimary() -> UIVibrancyEffect](uivibrancyeffect/widgetprimary.md)
  Creates a vibrancy effect suitable for use with certain supporting text and template images within a widget.
- [class func widgetSecondary() -> UIVibrancyEffect](uivibrancyeffect/widgetsecondary.md)
  Creates a vibrancy effect suitable for indicating the secondary importance or relevance of supporting text and template images within a widget.
- [class func widgetEffect(forVibrancyStyle: UIVibrancyEffectStyle) -> UIVibrancyEffect](uivibrancyeffect/widgeteffect(forvibrancystyle:).md)
  Creates a vibrancy effect for the specified style.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uivibrancyeffect/notificationcenter())*