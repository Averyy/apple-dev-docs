# UIVerticalBarCompressionBehavior

**Framework**: UIKit  
**Kind**: enum

How bars compress when different types of bars are hosted together and space is constrained.

**Availability**:
- iOS 27.1+ (Beta)
- iPadOS 27.1+ (Beta)

## Declaration

```swift
enum UIVerticalBarCompressionBehavior
```

## Topics

### Specifying a compression behavior
- [UIVerticalBarCompressionBehavior.automatic](uiverticalbarcompressionbehavior/automatic.md)
  The automatic compression behavior.
- [UIVerticalBarCompressionBehavior.prefersBarItems](uiverticalbarcompressionbehavior/prefersbaritems.md)
  A compression behavior that prefers keeping bar items visible.
- [UIVerticalBarCompressionBehavior.prefersTabBar](uiverticalbarcompressionbehavior/preferstabbar.md)
  A compression behavior that prefers keeping the tab bar visible.
### Initializers
- [init?(rawValue: Int)](uiverticalbarcompressionbehavior/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../swift/bitwisecopyable.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [RawRepresentable](../swift/rawrepresentable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [var verticalBarCompressionBehavior: UIVerticalBarCompressionBehavior](uinavigationitem/verticalbarcompressionbehavior.md)
  When the tab bar and navigation/toolbar items are both rendered together in the vertical bar, this property controls which items compress first.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiverticalbarcompressionbehavior)*