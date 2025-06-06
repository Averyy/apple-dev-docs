# decorationContainerView

**Framework**: UIKit  
**Kind**: property

The view that Writing Tools uses to display background decorations such as proofreading marks.

**Availability**:
- iOS 18.2+
- iPadOS 18.2+
- Mac Catalyst 18.2+
- visionOS 2.4+

## Declaration

```swift
@MainActor
weak var decorationContainerView: UIView? { get set }
```

#### Discussion

Writing Tools uses the view in this property to host proofreading marks and other visual elements that show any suggested changes. Set this property to a subview situated visibly below the text in your custom text view. It’s also satisfactory to place this view visually in front of the text. Make sure the size of the view is big enough to cover all of the affected text. If you don’t assign a value to this property, the coordinator uses the object in its [`view`](uiinteraction/view.md) property to host any visual elements.

If you display your view’s text using multiple text containers, implement the [`writingToolsCoordinator(_:requestsSingleContainerSubrangesOf:in:completion:)`](uiwritingtoolscoordinator/delegate-swift.protocol/writingtoolscoordinator(_:requestssinglecontainersubrangesof:in:completion:).md) and [`writingToolsCoordinator(_:requestsDecorationContainerViewFor:in:completion:)`](uiwritingtoolscoordinator/delegate-swift.protocol/writingtoolscoordinator(_:requestsdecorationcontainerviewfor:in:completion:).md) methods to provide separate decoration views for each container.

## See Also

- [var effectContainerView: UIView?](uiwritingtoolscoordinator/effectcontainerview.md)
  The view that Writing Tools uses to display visual effects during the text-rewriting process.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiwritingtoolscoordinator/decorationcontainerview)*