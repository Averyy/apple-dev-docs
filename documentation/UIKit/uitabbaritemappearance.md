# UITabBarItemAppearance

**Framework**: UIKit  
**Kind**: class

An object for customizing the appearance of tab bar items.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
class UITabBarItemAppearance
```

#### Overview

Use a [`UITabBarItemAppearance`](uitabbaritemappearance.md) object to customize the appearance of a tab bar item in each of its possible states. You can customize the appearance differently for each state. For example, you might apply different colors to the tab bar item’s icon in the [`normal`](uitabbaritemappearance/normal.md) and [`selected`](uitabbaritemappearance/selected.md) states.

## Topics

### Creating a tab bar item appearance object
- [init(style: UITabBarItemAppearance.Style)](uitabbaritemappearance/init(style:).md)
  Creates an appearance object with appropriate default values for a tab bar, displaying its items with the specified layout style.
- [convenience init()](uitabbaritemappearance/init.md)
  Creates an appearance object with default values for a stacked tab bar item.
- [init(coder: NSCoder)](uitabbaritemappearance/init(coder:).md)
  Creates an appearance object from data in an unarchiver.
### Copying a tab bar item appearance object
- [func copy() -> Self](uitabbaritemappearance/copy.md)
  Creates a copy of the appearance object.
### Resetting the appearance properties
- [func configureWithDefault(for: UITabBarItemAppearance.Style)](uitabbaritemappearance/configurewithdefault(for:).md)
  Configures the tab bar item appearance object with appropriate values for the specified style.
- [UITabBarItemAppearance.Style](uitabbaritemappearance/style.md)
  Constants indicating the layout of a tab bar item’s content.
### Configuring attributes for different item states
- [var normal: UITabBarItemStateAppearance](uitabbaritemappearance/normal.md)
  The appearance data to apply to the tab bar item when it’s enabled, unselected, and not the focused item.
- [var selected: UITabBarItemStateAppearance](uitabbaritemappearance/selected.md)
  The appearance data to apply to the tab bar item when it’s selected.
- [var disabled: UITabBarItemStateAppearance](uitabbaritemappearance/disabled.md)
  The appearance data to apply to the tab bar item when it’s disabled.
- [var focused: UITabBarItemStateAppearance](uitabbaritemappearance/focused.md)
  The appearance data to apply to the tab bar item when it’s focused.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSSecureCoding](../Foundation/NSSecureCoding.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [class UITabBarAppearance](uitabbarappearance.md)
  An object for customizing the appearance of a tab bar.
- [class UITabBarItemStateAppearance](uitabbaritemstateappearance.md)
  A data object containing the specific customizations for tab bar items in a particular state.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitabbaritemappearance)*