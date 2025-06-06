# isTranslucent

**Framework**: UIKit  
**Kind**: property

A Boolean value that indicates whether the toolbar is translucent.

**Availability**:
- iOS 3.0+
- iPadOS 3.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var isTranslucent: Bool { get set }
```

#### Discussion

When the toolbar is translucent, configure the [`edgesForExtendedLayout`](uiviewcontroller/edgesforextendedlayout.md) and [`extendedLayoutIncludesOpaqueBars`](uiviewcontroller/extendedlayoutincludesopaquebars.md) properties of your view controller to display your content underneath the toolbar.

If the toolbar doesn’t have a custom background image, or if any pixel of the background image has an alpha value of less than `1.0`, the default value of this property is [`true`](https://developer.apple.com/documentation/swift/true). If the background image is completely opaque, the default value of this property is [`false`](https://developer.apple.com/documentation/swift/false). If you set this property to [`true`](https://developer.apple.com/documentation/swift/true) and the custom background image is completely opaque, UIKit applies a system-defined opacity of less than `1.0` to the image. If you set this property to [`false`](https://developer.apple.com/documentation/swift/false) and the background image isn’t opaque, UIKit adds an opaque backdrop.

## See Also

- [var standardAppearance: UIToolbarAppearance](uitoolbar/standardappearance.md)
  The appearance settings to use for a standard-height toolbar.
- [var compactAppearance: UIToolbarAppearance?](uitoolbar/compactappearance.md)
  The appearance settings to use for a compact-height toolbar.
- [var scrollEdgeAppearance: UIToolbarAppearance?](uitoolbar/scrolledgeappearance.md)
  The appearance settings for a standard-height toolbar when the edge of scrollable content aligns with the edge of the toolbar.
- [var compactScrollEdgeAppearance: UIToolbarAppearance?](uitoolbar/compactscrolledgeappearance.md)
  The appearance settings for a compact-height toolbar when the edge of any scrollable content aligns with the edge of a compact-height toolbar.
- [Legacy customizations](uitoolbar-legacy-customizations.md)
  Customize appearance information directly on the toolbar object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitoolbar/istranslucent)*