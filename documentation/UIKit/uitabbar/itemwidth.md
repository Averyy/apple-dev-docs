# itemWidth

**Framework**: UIKit  
**Kind**: property

The width (in points) of tab bar items.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var itemWidth: CGFloat { get set }
```

#### Discussion

When the tab bar positions items using the [`UITabBar.ItemPositioning.centered`](uitabbar/itempositioning-swift.enum/centered.md) option, it checks the value of this property to see if a custom width value has been supplied. The default value of this property is `0`, which causes the tab bar to use a system-defined default width for each item. Specifying a value greater than `0` causes the tab bar to use your custom value instead. If you try to set this property to a negative value, the tab bar sets the value to `0` instead.

## See Also

- [var itemPositioning: UITabBar.ItemPositioning](uitabbar/itempositioning-swift.property.md)
  The positioning scheme for the tab bar items in the tab bar.
- [UITabBar.ItemPositioning](uitabbar/itempositioning-swift.enum.md)
  Constants that specify tab bar item positioning.
- [var itemSpacing: CGFloat](uitabbar/itemspacing.md)
  The amount of space (in points) to use between tab bar items.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitabbar/itemwidth)*