# UIStackView.Alignment

**Framework**: UIKit  
**Kind**: enum  
**Role**: Enumeration

The layout of arranged views perpendicular to the stack view’s axis.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
enum Alignment
```

```c
enum UIStackViewAlignment : NSInteger;
```

## Topics

### Constants
- [UIStackView.Alignment.fill](./alignment-swift.enum/fill.md)
  A layout where the stack view resizes its arranged views so that they fill the available space perpendicular to the stack view’s axis.
- [UIStackView.Alignment.center](./alignment-swift.enum/center.md)
  A layout where the stack view aligns the center of its arranged views with its center along its axis.
- [UIStackView.Alignment.leading](./alignment-swift.enum/leading.md)
  A layout for vertical stacks where the stack view aligns the leading edge of its arranged views along its leading edge.
- [UIStackView.Alignment.trailing](./alignment-swift.enum/trailing.md)
  A layout for vertical stacks where the stack view aligns the trailing edge of its arranged views along its trailing edge.
- [static var top: UIStackView.Alignment](./alignment-swift.enum/top.md)
  A layout for horizontal stacks where the stack view aligns the top edge of its arranged views along its top edge.
- [static var bottom: UIStackView.Alignment](./alignment-swift.enum/bottom.md)
  A layout for horizontal stacks where the stack view aligns the bottom edge of its arranged views along its bottom edge.
- [UIStackView.Alignment.firstBaseline](./alignment-swift.enum/firstbaseline.md)
  A layout for horizontal stacks where the stack view aligns its arranged views based on their first baseline.
- [UIStackView.Alignment.lastBaseline](./alignment-swift.enum/lastbaseline.md)
  A layout for horizontal stacks where the stack view aligns its arranged views based on their last baseline.
### Initializers
- [init?(rawValue: Int)](./alignment-swift.enum/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Constants
- [UIStackView.Distribution](./distribution-swift.enum.md)
  The layout that defines the size and position of the arranged views along the stack view’s axis.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uistackview/alignment-swift.enum)*