# barStyle

**Framework**: UIKit  
**Kind**: property

A bar style that specifies the search bar’s appearance.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var barStyle: UIBarStyle { get set }
```

#### Discussion

This property can be used together with [`searchBarStyle`](uisearchbar/searchbarstyle.md).

See [`UIBarStyle`](uibarstyle.md) for possible values. The default value is [`UIBarStyle.default`](uibarstyle/default.md).

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
- [var isTranslucent: Bool](uisearchbar/istranslucent.md)
  A Boolean value that indicates whether the search bar is translucent (true) or not (false).
- [enum UIBarStyle](uibarstyle.md)
  Defines the stylistic appearance of different types of views.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uisearchbar/barstyle)*