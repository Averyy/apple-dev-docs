# isTranslucent

**Framework**: UIKit  
**Kind**: property

A Boolean value that indicates whether the search bar is translucent (true) or not (false).

**Availability**:
- iOS 3.0+
- iPadOS 3.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var isTranslucent: Bool { get set }
```

#### Discussion

The default value is [`true`](https://developer.apple.com/documentation/Swift/true). If the search bar has a custom background image, the default is [`true`](https://developer.apple.com/documentation/Swift/true) if any pixel of the image has an alpha value of less than `1.0`, and [`false`](https://developer.apple.com/documentation/Swift/false) otherwise.

If you set this property to [`true`](https://developer.apple.com/documentation/Swift/true) on a search bar with an opaque custom background image, the search bar will apply a system opacity less than `1.0` to the image.

If you set this property to [`false`](https://developer.apple.com/documentation/Swift/false) on a search bar with a translucent custom background image, the search bar provides an opaque background for the image using black if the search bar has [`UIBarStyle.black`](uibarstyle/black.md) style, white if the search bar has [`UIBarStyle.default`](uibarstyle/default.md), or the search bar’s [`barTintColor`](uisearchbar/bartintcolor.md) if a custom value is defined.

## See Also

- [var isEnabled: Bool](uisearchbar/isenabled.md)
  A Boolean value indicating whether the search bar is in the enabled state.
- [var barTintColor: UIColor?](uisearchbar/bartintcolor.md)
  The tint color to apply to the search bar background.
- [var searchBarStyle: UISearchBar.Style](uisearchbar/searchbarstyle.md)
  A search bar style that specifies the search bar’s appearance.
- [UISearchBar.Style](uisearchbar/style.md)
  Specifies whether the search bar has a background.
- [var tintColor: UIColor!](uisearchbar/tintcolor.md)
  The tint color to apply to key elements in the search bar.
- [var barStyle: UIBarStyle](uisearchbar/barstyle.md)
  A bar style that specifies the search bar’s appearance.
- [enum UIBarStyle](uibarstyle.md)
  Defines the stylistic appearance of different types of views.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uisearchbar/istranslucent)*