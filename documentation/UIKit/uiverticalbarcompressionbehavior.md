# UIVerticalBarCompressionBehavior

**Framework**: UIKit  
**Kind**: enum  
**Role**: Enumeration

How bars compress when different types of bars are hosted together and space is constrained.

**Availability**:
- iOS 27.1+
- iPadOS 27.1+
- Mac Catalyst 27.1+
- tvOS 27.1+
- visionOS 27.1+

## Declaration

```swift
enum UIVerticalBarCompressionBehavior
```

```c
enum UIVerticalBarCompressionBehavior : NSInteger;
```

## Topics

### Specifying a compression behavior
- [UIVerticalBarCompressionBehavior.automatic](./uiverticalbarcompressionbehavior/automatic.md)
  The automatic compression behavior.
- [UIVerticalBarCompressionBehavior.prefersBarItems](./uiverticalbarcompressionbehavior/prefersbaritems.md)
  A compression behavior that prefers keeping bar items visible.
- [UIVerticalBarCompressionBehavior.prefersTabBar](./uiverticalbarcompressionbehavior/preferstabbar.md)
  A compression behavior that prefers keeping the tab bar visible.
### Initializers
- [init?(rawValue: Int)](./uiverticalbarcompressionbehavior/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Configuring bars on the vertical axis
- [enum UIVerticalBarBehavior](./uiverticalbarbehavior.md)
  A behavior that determines whether the vertical bar is used.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiverticalbarcompressionbehavior)*