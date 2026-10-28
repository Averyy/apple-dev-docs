# UITabBarItemAppearance.Style

**Framework**: UIKit  
**Kind**: enum  
**Role**: Enumeration

Constants indicating the layout of a tab bar item’s content.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- tvOS
- visionOS

## Declaration

```swift
enum Style
```

```c
enum UITabBarItemAppearanceStyle : NSInteger;
```

## Overview

A tab bar adjusts the layout of each item’s icon and title string based on the current trait environment and other factors.

## Topics

### Item layout
- [UITabBarItemAppearance.Style.stacked](./style/stacked.md)
  A vertically stacked icon and title.
- [UITabBarItemAppearance.Style.inline](./style/inline.md)
  A side-by-side layout of the icon and title, suitable for use in regular-width environments.
- [UITabBarItemAppearance.Style.compactInline](./style/compactinline.md)
  A side-by-side layout of the icon and title, suitable for use in compact-width environments.
### Initializers
- [init?(rawValue: Int)](./style/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Resetting the appearance properties
- [func configureWithDefault(for: UITabBarItemAppearance.Style)](./configurewithdefault%28for%29.md)
  Configures the tab bar item appearance object with appropriate values for the specified style.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitabbaritemappearance/style)*