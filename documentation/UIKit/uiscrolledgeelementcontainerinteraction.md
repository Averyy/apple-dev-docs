# UIScrollEdgeElementContainerInteraction

**Framework**: UIKit  
**Kind**: class

Add this interaction to a container view of views that overlay the edge of a scroll view. Any descendants of this view that should affect the shape of the edge effect, such as labels, images, glass views, and controls, will automatically do so.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
@MainActor
class UIScrollEdgeElementContainerInteraction
```

#### Overview

In the following example, an interaction is added to a container view of buttons that overlay the bottom edge of a scroll view.

```None
let interaction = UIScrollEdgeElementContainerInteraction()
interaction.scrollView = scrollView
interaction.edge = .bottom
buttonContainer.addInteraction(interaction)
```

## Topics

### Instance Properties
- [var edge: UIRectEdge](uiscrolledgeelementcontainerinteraction/edge.md)
  The edge of the scroll view to affect
- [var scrollView: UIScrollView?](uiscrolledgeelementcontainerinteraction/scrollview.md)
  The scroll view to affect

## Relationships

### Inherits From
- [NSObject](../objectivec/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../swift/cvararg.md)
- [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../swift/customstringconvertible.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [NSObjectProtocol](../objectivec/nsobjectprotocol.md)
- [Sendable](../swift/sendable.md)
- [UIInteraction](uiinteraction.md)

## See Also

- [class UIBackgroundExtensionView](uibackgroundextensionview.md)
  A view that extends content to fill its own bounds.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiscrolledgeelementcontainerinteraction)*