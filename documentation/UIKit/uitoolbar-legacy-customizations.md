# Legacy customizations

**Framework**: UIKit

Customize appearance information directly on the toolbar object.

#### Overview

In iOS 13 and later, customize your toolbar using the [`standardAppearance`](uitoolbar/standardappearance.md) and [`compactAppearance`](uitoolbar/compactappearance.md) properties. You may continue to use these legacy accessors to customize your toolbar’s appearance directly, but you must update the appearance for different bar configurations yourself.

## Topics

### Setting the bar’s style
- [var barStyle: UIBarStyle](uitoolbar/barstyle.md)
  The toolbar style that specifies its appearance.
- [enum UIBarStyle](uibarstyle.md)
  Defines the stylistic appearance of different types of views.
### Configuring bar button items
- [var tintColor: UIColor!](uitoolbar/tintcolor.md)
  The tint color to apply to the bar button items.
### Changing the background
- [var barTintColor: UIColor?](uitoolbar/bartintcolor.md)
  The tint color to apply to the toolbar background.
- [func backgroundImage(forToolbarPosition: UIBarPosition, barMetrics: UIBarMetrics) -> UIImage?](uitoolbar/backgroundimage(fortoolbarposition:barmetrics:).md)
  Returns the image to use for the background in a given position and with given metrics.
- [func setBackgroundImage(UIImage?, forToolbarPosition: UIBarPosition, barMetrics: UIBarMetrics)](uitoolbar/setbackgroundimage(_:fortoolbarposition:barmetrics:).md)
  Sets the image to use for the background in a given position and with given metrics.
### Adding a shadow
- [func shadowImage(forToolbarPosition: UIBarPosition) -> UIImage?](uitoolbar/shadowimage(fortoolbarposition:).md)
  Returns the image to use for the toolbar shadow in a given position.
- [func setShadowImage(UIImage?, forToolbarPosition: UIBarPosition)](uitoolbar/setshadowimage(_:fortoolbarposition:).md)
  Sets the image to use for the toolbar shadow in a given position.

## See Also

- [var standardAppearance: UIToolbarAppearance](uitoolbar/standardappearance.md)
  The appearance settings to use for a standard-height toolbar.
- [var compactAppearance: UIToolbarAppearance?](uitoolbar/compactappearance.md)
  The appearance settings to use for a compact-height toolbar.
- [var scrollEdgeAppearance: UIToolbarAppearance?](uitoolbar/scrolledgeappearance.md)
  The appearance settings for a standard-height toolbar when the edge of scrollable content aligns with the edge of the toolbar.
- [var compactScrollEdgeAppearance: UIToolbarAppearance?](uitoolbar/compactscrolledgeappearance.md)
  The appearance settings for a compact-height toolbar when the edge of any scrollable content aligns with the edge of a compact-height toolbar.
- [var isTranslucent: Bool](uitoolbar/istranslucent.md)
  A Boolean value that indicates whether the toolbar is translucent.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitoolbar-legacy-customizations)*