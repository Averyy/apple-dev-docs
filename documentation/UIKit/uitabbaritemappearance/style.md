# UITabBarItemAppearance.Style

**Framework**: UIKit  
**Kind**: enum

Constants indicating the layout of a tab bar item’s content.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
enum Style
```

#### Overview

A tab bar adjusts the layout of each item’s icon and title string based on the current trait environment and other factors.

## Topics

### Item layout
- [UITabBarItemAppearance.Style.stacked](uitabbaritemappearance/style/stacked.md)
  A vertically stacked icon and title.
- [UITabBarItemAppearance.Style.inline](uitabbaritemappearance/style/inline.md)
  A side-by-side layout of the icon and title, suitable for use in regular-width environments.
- [UITabBarItemAppearance.Style.compactInline](uitabbaritemappearance/style/compactinline.md)
  A side-by-side layout of the icon and title, suitable for use in compact-width environments.
### Initializers
- [init?(rawValue: Int)](uitabbaritemappearance/style/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [func configureWithDefault(for: UITabBarItemAppearance.Style)](uitabbaritemappearance/configurewithdefault(for:).md)
  Configures the tab bar item appearance object with appropriate values for the specified style.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitabbaritemappearance/style)*