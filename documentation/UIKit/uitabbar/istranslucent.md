# isTranslucent

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the tab bar is translucent.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- tvOS

## Declaration

```swift
var isTranslucent: Bool { get set }
```

```objc
@property (nonatomic, getter=isTranslucent) BOOL translucent;
```

#### Discussion

When the tab bar is translucent, configure the [`edgesForExtendedLayout`](../uiviewcontroller/edgesforextendedlayout.md) and [`extendedLayoutIncludesOpaqueBars`](../uiviewcontroller/extendedlayoutincludesopaquebars.md) properties of your view controller to display your content underneath the tab bar.

If the tab bar doesn’t have a custom background image, or if any pixel of the background image has an alpha value of less than `1.0`, the default value of this property is [`true`](../../Swift/true.md). If the background image is completely opaque, the default value of this property is [`false`](../../Swift/false.md). If you set this property to [`true`](../../Swift/true.md) and the custom background image is completely opaque, UIKit applies a system-defined opacity of less than `1.0` to the image. If you set this property to [`false`](../../Swift/false.md) and the background image is not opaque, UIKit adds an opaque backdrop.

## See Also

### Customizing tab bar appearance
- [var standardAppearance: UITabBarAppearance](./standardappearance.md)
  The appearance settings for a standard-height tab bar.
- [var scrollEdgeAppearance: UITabBarAppearance?](./scrolledgeappearance.md)
  The appearance settings for the tab bar when the edge of scrollable content aligns with the edge of the tab bar.
- [var leadingAccessoryView: UIView](./leadingaccessoryview.md)
  The view at the leading edge of a tab bar on tvOS.
- [var trailingAccessoryView: UIView](./trailingaccessoryview.md)
  The view at the trailing edge of a tab bar on tvOS.
- [Legacy customizations](../uitabbar-legacy-customizations.md)
  Customize appearance information directly on the tab bar object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitabbar/istranslucent)*