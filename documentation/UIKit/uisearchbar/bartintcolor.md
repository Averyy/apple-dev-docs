# barTintColor

**Framework**: UIKit  
**Kind**: property

The tint color to apply to the search bar background.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var barTintColor: UIColor? { get set }
```

#### Discussion

This color is made translucent by default unless you set the [`isTranslucent`](uisearchbar/istranslucent.md) property to [`false`](https://developer.apple.com/documentation/swift/false).

## See Also

- [var isEnabled: Bool](uisearchbar/isenabled.md)
  A Boolean value indicating whether the search bar is in the enabled state.
- [var searchBarStyle: UISearchBar.Style](uisearchbar/searchbarstyle.md)
  A search bar style that specifies the search bar’s appearance.
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

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uisearchbar/bartintcolor)*