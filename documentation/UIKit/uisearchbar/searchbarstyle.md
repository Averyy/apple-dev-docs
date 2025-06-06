# searchBarStyle

**Framework**: UIKit  
**Kind**: property

A search bar style that specifies the search bar’s appearance.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var searchBarStyle: UISearchBar.Style { get set }
```

#### Discussion

This property can be used together with [`barStyle`](uisearchbar/barstyle.md). The style [`UISearchBar.Style.minimal`](uisearchbar/style/minimal.md) provides no default background color or image but will display one if customized as such.

Custom background and search field images take precedence over this property.

See [`UISearchBar.Style`](uisearchbar/style.md) for possible values. The default value is [`UISearchBar.Style.default`](uisearchbar/style/default.md).

## See Also

- [var isEnabled: Bool](uisearchbar/isenabled.md)
  A Boolean value indicating whether the search bar is in the enabled state.
- [var barTintColor: UIColor?](uisearchbar/bartintcolor.md)
  The tint color to apply to the search bar background.
- [UISearchBar.Style](uisearchbar/style.md)
  Specifies whether the search bar has a background.
- [var tintColor: UIColor!](uisearchbar/tintcolor.md)
  The tint color to apply to key elements in the search bar.
- [var isTranslucent: Bool](uisearchbar/istranslucent.md)
  A Boolean value that indicates whether the search bar is translucent (true) or not (false).
- [var barStyle: UIBarStyle](uisearchbar/barstyle.md)
  A bar style that specifies the search bar’s appearance.
- [enum UIBarStyle](uibarstyle.md)
  Defines the stylistic appearance of different types of views.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uisearchbar/searchbarstyle)*