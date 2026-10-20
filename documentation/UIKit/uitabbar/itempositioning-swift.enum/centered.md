# UITabBar.ItemPositioning.centered

**Framework**: UIKit  
**Kind**: case  
**Role**: Case

Center items in the available space.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
case centered
```

```c
UITabBarItemPositioningCentered
```

#### Discussion

With this option, the tab bar uses the [`itemWidth`](../itemwidth.md) and [`itemSpacing`](../itemspacing.md) properties to set the width of items and the spacing between items, positioning those items in the center of the available space. When the [`UITabBar.ItemPositioning.automatic`](./automatic.md) option is selected, the tab bar uses this behavior in horizontally regular environments.

## See Also

### Constants
- [UITabBar.ItemPositioning.automatic](./automatic.md)
  Specifies automatic tab bar item positioning according to the user interface idiom, as follows:
- [UITabBar.ItemPositioning.fill](./fill.md)
  Distribute items across the entire width of the tab bar.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitabbar/itempositioning-swift.enum/centered)*