# UITabBar.ItemPositioning

**Framework**: UIKit  
**Kind**: enum  
**Role**: Enumeration

Constants that specify tab bar item positioning.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
enum ItemPositioning
```

```c
enum UITabBarItemPositioning : NSInteger;
```

## Topics

### Constants
- [UITabBar.ItemPositioning.automatic](./itempositioning-swift.enum/automatic.md)
  Specifies automatic tab bar item positioning according to the user interface idiom, as follows:
- [UITabBar.ItemPositioning.fill](./itempositioning-swift.enum/fill.md)
  Distribute items across the entire width of the tab bar.
- [UITabBar.ItemPositioning.centered](./itempositioning-swift.enum/centered.md)
  Center items in the available space.
### Initializers
- [init?(rawValue: Int)](./itempositioning-swift.enum/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Customizing item spacing
- [var itemPositioning: UITabBar.ItemPositioning](./itempositioning-swift.property.md)
  The positioning scheme for the tab bar items in the tab bar.
- [var itemSpacing: CGFloat](./itemspacing.md)
  The amount of space (in points) to use between tab bar items.
- [var itemWidth: CGFloat](./itemwidth.md)
  The width (in points) of tab bar items.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitabbar/itempositioning-swift.enum)*