# isTranslucent

**Framework**: UIKit  
**Kind**: property

A Boolean value that indicates whether the tab bar is translucent.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- tvOS ?+

## Declaration

```swift
@MainActor
var isTranslucent: Bool { get set }
```

#### Discussion

When the tab bar is translucent, configure the [`edgesForExtendedLayout`](uiviewcontroller/edgesforextendedlayout.md) and [`extendedLayoutIncludesOpaqueBars`](uiviewcontroller/extendedlayoutincludesopaquebars.md) properties of your view controller to display your content underneath the tab bar.

If the tab bar doesn’t have a custom background image, or if any pixel of the background image has an alpha value of less than `1.0`, the default value of this property is [`true`](https://developer.apple.com/documentation/Swift/true). If the background image is completely opaque, the default value of this property is [`false`](https://developer.apple.com/documentation/Swift/false). If you set this property to [`true`](https://developer.apple.com/documentation/Swift/true) and the custom background image is completely opaque, UIKit applies a system-defined opacity of less than `1.0` to the image. If you set this property to [`false`](https://developer.apple.com/documentation/Swift/false) and the background image is not opaque, UIKit adds an opaque backdrop.

## See Also

- [var standardAppearance: UITabBarAppearance](uitabbar/standardappearance.md)
  The appearance settings for a standard-height tab bar.
- [var scrollEdgeAppearance: UITabBarAppearance?](uitabbar/scrolledgeappearance.md)
  The appearance settings for the tab bar when the edge of scrollable content aligns with the edge of the tab bar.
- [var leadingAccessoryView: UIView](uitabbar/leadingaccessoryview.md)
  The view at the leading edge of a tab bar on tvOS.
- [var trailingAccessoryView: UIView](uitabbar/trailingaccessoryview.md)
  The view at the trailing edge of a tab bar on tvOS.
- [Legacy customizations](uitabbar-legacy-customizations.md)
  Customize appearance information directly on the tab bar object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitabbar/istranslucent)*