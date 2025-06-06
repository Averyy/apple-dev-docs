# top

**Framework**: UIKit  
**Kind**: property

A layout for horizontal stacks where the stack view aligns the top edge of its arranged views along its top edge.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
static var top: UIStackView.Alignment { get }
```

#### Discussion

This value is equivalent to the [`UIStackView.Alignment.leading`](uistackview/alignment-swift.enum/leading.md) alignment for vertical stacks.

The following image shows an example of a horizontal stack view that uses the [`top`](uistackview/alignment-swift.enum/top.md) alignment.

![A horizontal stack view with four arranged subviews. The stack view aligns the subviews to its top edge.](https://docs-assets.developer.apple.com/published/ac8be4305f320bb371d4f5981fdc2cfb/media-2557465%402x.png)

## See Also

- [UIStackView.Alignment.fill](uistackview/alignment-swift.enum/fill.md)
  A layout where the stack view resizes its arranged views so that they fill the available space perpendicular to the stack view’s axis.
- [UIStackView.Alignment.center](uistackview/alignment-swift.enum/center.md)
  A layout where the stack view aligns the center of its arranged views with its center along its axis.
- [UIStackView.Alignment.leading](uistackview/alignment-swift.enum/leading.md)
  A layout for vertical stacks where the stack view aligns the leading edge of its arranged views along its leading edge.
- [UIStackView.Alignment.trailing](uistackview/alignment-swift.enum/trailing.md)
  A layout for vertical stacks where the stack view aligns the trailing edge of its arranged views along its trailing edge.
- [static var bottom: UIStackView.Alignment](uistackview/alignment-swift.enum/bottom.md)
  A layout for horizontal stacks where the stack view aligns the bottom edge of its arranged views along its bottom edge.
- [UIStackView.Alignment.firstBaseline](uistackview/alignment-swift.enum/firstbaseline.md)
  A layout for horizontal stacks where the stack view aligns its arranged views based on their first baseline.
- [UIStackView.Alignment.lastBaseline](uistackview/alignment-swift.enum/lastbaseline.md)
  A layout for horizontal stacks where the stack view aligns its arranged views based on their last baseline.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uistackview/alignment-swift.enum/top)*