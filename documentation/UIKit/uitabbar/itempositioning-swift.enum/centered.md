# UITabBar.ItemPositioning.centered

**Framework**: UIKit  
**Kind**: case

Center items in the available space.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
case centered
```

#### Discussion

With this option, the tab bar uses the [`itemWidth`](uitabbar/itemwidth.md) and [`itemSpacing`](uitabbar/itemspacing.md) properties to set the width of items and the spacing between items, positioning those items in the center of the available space. When the [`UITabBar.ItemPositioning.automatic`](uitabbar/itempositioning-swift.enum/automatic.md) option is selected, the tab bar uses this behavior in horizontally regular environments.

## See Also

- [UITabBar.ItemPositioning.automatic](uitabbar/itempositioning-swift.enum/automatic.md)
  Specifies automatic tab bar item positioning according to the user interface idiom, as follows:
- [UITabBar.ItemPositioning.fill](uitabbar/itempositioning-swift.enum/fill.md)
  Distribute items across the entire width of the tab bar.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitabbar/itempositioning-swift.enum/centered)*