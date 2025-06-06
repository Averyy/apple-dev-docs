# Legacy customizations

**Framework**: UIKit

Customize appearance information directly on the tab bar object.

#### Overview

In iOS 13 and later, customize your tab bar using the [`standardAppearance`](uitabbar/standardappearance.md) property. You may also continue to use these legacy accessors to customize your tab bar’s appearance directly.

## Topics

### Setting the bar’s style
- [var barStyle: UIBarStyle](uitabbar/barstyle.md)
  The tab bar style that specifies its appearance.
- [enum UIBarStyle](uibarstyle.md)
  Defines the stylistic appearance of different types of views.
### Configuring tab bar items
- [var tintColor: UIColor!](uitabbar/tintcolor.md)
  The tint color to apply to the tab bar items.
### Customizing item spacing
- [var itemPositioning: UITabBar.ItemPositioning](uitabbar/itempositioning-swift.property.md)
  The positioning scheme for the tab bar items in the tab bar.
- [UITabBar.ItemPositioning](uitabbar/itempositioning-swift.enum.md)
  Constants that specify tab bar item positioning.
- [var itemSpacing: CGFloat](uitabbar/itemspacing.md)
  The amount of space (in points) to use between tab bar items.
- [var itemWidth: CGFloat](uitabbar/itemwidth.md)
  The width (in points) of tab bar items.
### Configuring selection appearance
- [var unselectedItemTintColor: UIColor?](uitabbar/unselecteditemtintcolor.md)
  The tint color to apply to unselected tabs.
- [var selectionIndicatorImage: UIImage?](uitabbar/selectionindicatorimage.md)
  The image to use for the selection indicator.
- [var selectedImageTintColor: UIColor?](uitabbar/selectedimagetintcolor.md)
  The tint color applied to the selected tab bar item.
### Changing the background
- [var barTintColor: UIColor?](uitabbar/bartintcolor.md)
  The tint color to apply to the tab bar background.
- [var backgroundImage: UIImage?](uitabbar/backgroundimage.md)
  The custom background image for the tab bar.
### Adding a shadow
- [var shadowImage: UIImage?](uitabbar/shadowimage.md)
  The shadow image to use for the tab bar.

## See Also

- [var standardAppearance: UITabBarAppearance](uitabbar/standardappearance.md)
  The appearance settings for a standard-height tab bar.
- [var scrollEdgeAppearance: UITabBarAppearance?](uitabbar/scrolledgeappearance.md)
  The appearance settings for the tab bar when the edge of scrollable content aligns with the edge of the tab bar.
- [var leadingAccessoryView: UIView](uitabbar/leadingaccessoryview.md)
  The view at the leading edge of a tab bar on tvOS.
- [var trailingAccessoryView: UIView](uitabbar/trailingaccessoryview.md)
  The view at the trailing edge of a tab bar on tvOS.
- [var isTranslucent: Bool](uitabbar/istranslucent.md)
  A Boolean value that indicates whether the tab bar is translucent.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitabbar-legacy-customizations)*