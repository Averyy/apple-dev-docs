# barTintColor

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The tint color to apply to the search bar background.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
var barTintColor: UIColor? { get set }
```

```objc
@property (nonatomic, strong, nullable) UIColor * barTintColor;
```

## Discussion

This color is made translucent by default unless you set the [`isTranslucent`](./istranslucent.md) property to [`false`](../../Swift/false.md).

## See Also

### Configuring the search bar
- [var isEnabled: Bool](./isenabled.md)
  A Boolean value indicating whether the search bar is in the enabled state.
- [var searchBarStyle: UISearchBar.Style](./searchbarstyle.md)
  A search bar style that specifies the search bar’s appearance.
- [UISearchBar.Style](./style.md)
  Specifies whether the search bar has a background.
- [var tintColor: UIColor!](./tintcolor.md)
  The tint color to apply to key elements in the search bar.
- [var isTranslucent: Bool](./istranslucent.md)
  A Boolean value that indicates whether the search bar is translucent (true) or not (false).
- [var barStyle: UIBarStyle](./barstyle.md)
  A bar style that specifies the search bar’s appearance.
- [enum UIBarStyle](../uibarstyle.md)
  Defines the stylistic appearance of different types of views.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uisearchbar/bartintcolor)*