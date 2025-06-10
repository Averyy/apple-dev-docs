# UITabBar.ItemPositioning.automatic

**Framework**: UIKit  
**Kind**: case

Specifies automatic tab bar item positioning according to the user interface idiom, as follows:

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
case automatic
```

#### Discussion

- In a horizontally compact environment, the tab bar spreads items across the entire space, adjusting inter-item spacing as needed.
- In a horizontally regular environment, the tab bar uses the [`itemWidth`](uitabbar/itemwidth.md) and [`itemSpacing`](uitabbar/itemspacing.md) properties to set the width of items and the spacing between items, positioning those items in the center of the available space. This configuration has the potential to leave space along the left and right edges of the tab bar.

## See Also

- [UITabBar.ItemPositioning.fill](uitabbar/itempositioning-swift.enum/fill.md)
  Distribute items across the entire width of the tab bar.
- [UITabBar.ItemPositioning.centered](uitabbar/itempositioning-swift.enum/centered.md)
  Center items in the available space.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitabbar/itempositioning-swift.enum/automatic)*