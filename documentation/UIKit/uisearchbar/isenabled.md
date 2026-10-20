# isEnabled

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value indicating whether the search bar is in the enabled state.

**Availability**:
- iOS 16.4+
- iPadOS 16.4+
- Mac Catalyst 16.4+
- tvOS 16.4+
- visionOS 1.0+

## Declaration

```swift
var isEnabled: Bool { get set }
```

```objc
@property (nonatomic, getter=isEnabled) BOOL enabled;
```

#### Discussion

Set the value of this property to `true` to enable the search bar or `false` to disable it. An enabled search bar responds to user interactions; a disabled search bar ignores touch events and takes on a disabled appearance.

If the search bar is associated with a [`UINavigationItem`](../uinavigationitem.md) with [`inline`](../uinavigationitem/searchbarplacement-swift.enum/inline.md), then the minimized (icon-only) [`UISearchBar`](../uisearchbar.md) won’t grow to the text field while [`isEnabled`](./isenabled.md) is `false`.

The default value of this property is `true` for a newly created search bar. You can set the search bar’s initial enabled state in your storyboard file.

## See Also

### Configuring the search bar
- [var barTintColor: UIColor?](./bartintcolor.md)
  The tint color to apply to the search bar background.
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

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uisearchbar/isenabled)*