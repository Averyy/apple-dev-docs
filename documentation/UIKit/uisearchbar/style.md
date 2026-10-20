# UISearchBar.Style

**Framework**: UIKit  
**Kind**: enum  
**Role**: Enumeration

Specifies whether the search bar has a background.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
enum Style
```

```c
enum UISearchBarStyle : NSUInteger;
```

## Topics

### Constants
- [UISearchBar.Style.default](./style/default.md)
  The search bar has the default style.
- [UISearchBar.Style.prominent](./style/prominent.md)
  The search bar has a translucent background, and the search field is opaque.
- [UISearchBar.Style.minimal](./style/minimal.md)
  The search bar has no background, and the search field is translucent.
### Initializers
- [init?(rawValue: UInt)](./style/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Configuring the search bar
- [var isEnabled: Bool](./isenabled.md)
  A Boolean value indicating whether the search bar is in the enabled state.
- [var barTintColor: UIColor?](./bartintcolor.md)
  The tint color to apply to the search bar background.
- [var searchBarStyle: UISearchBar.Style](./searchbarstyle.md)
  A search bar style that specifies the search bar’s appearance.
- [var tintColor: UIColor!](./tintcolor.md)
  The tint color to apply to key elements in the search bar.
- [var isTranslucent: Bool](./istranslucent.md)
  A Boolean value that indicates whether the search bar is translucent (true) or not (false).
- [var barStyle: UIBarStyle](./barstyle.md)
  A bar style that specifies the search bar’s appearance.
- [enum UIBarStyle](../uibarstyle.md)
  Defines the stylistic appearance of different types of views.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uisearchbar/style)*