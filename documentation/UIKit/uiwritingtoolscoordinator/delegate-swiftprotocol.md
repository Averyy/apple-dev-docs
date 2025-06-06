# UIWritingToolsCoordinator.Delegate

**Framework**: UIKit  
**Kind**: protocol

An interface that you use to manage interactions between Writing Tools and your custom text view.

**Availability**:
- iOS 18.2+
- iPadOS 18.2+
- Mac Catalyst 18.2+
- visionOS 2.4+

## Declaration

```swift
protocol Delegate : NSObjectProtocol
```

## Mentions

- [Adding Writing Tools support to a custom UIKit view](adding-writing-tools-support-to-a-custom-uiview.md)

#### Overview

Adopt the `UIWritingToolsCoordinator.Delegate` protocol in the type you use to manage your custom text view. When you add a [`UIWritingToolsCoordinator`](uiwritingtoolscoordinator.md) object to your view, the coordinator uses this protocol to communicate with that view. The protocol lets Writing Tools fetch your view’s text, report suggested changes back to your view, and deliver visual feedback when Writing Tools features are active. Make sure the type that adopts this protocol has access to your view’s text storage and can perform relevant tasks on behalf of the view.

Writing Tools expects you to call the provided handler blocks at the end of your delegate methods. It’s crucial that you execute these blocks in a timely manner to allow Writing Tools to perform subsequent tasks. For example, Writing Tools waits for you to execute the handlers for animation-related methods before moving on to the next stage of the animations.

## Topics

### Starting a Writing Tools operation
- [func writingToolsCoordinator(UIWritingToolsCoordinator, requestsContextsFor: UIWritingToolsCoordinator.ContextScope, completion: ([UIWritingToolsCoordinator.Context]) -> Void)](uiwritingtoolscoordinator/delegate-swift.protocol/writingtoolscoordinator(_:requestscontextsfor:completion:).md)
  Asks your delegate to provide the text to evaluate during the Writing Tools operation.
### Incorporating Writing Tools suggestions
- [func writingToolsCoordinator(UIWritingToolsCoordinator, replace: NSRange, in: UIWritingToolsCoordinator.Context, proposedText: NSAttributedString, reason: UIWritingToolsCoordinator.TextReplacementReason, animationParameters: UIWritingToolsCoordinator.AnimationParameters?, completion: (NSAttributedString?) -> Void)](uiwritingtoolscoordinator/delegate-swift.protocol/writingtoolscoordinator(_:replace:in:proposedtext:reason:animationparameters:completion:).md)
  Tells the delegate that there are text changes to incorporate into the view.
- [func writingToolsCoordinator(UIWritingToolsCoordinator, select: [NSValue], in: UIWritingToolsCoordinator.Context, completion: () -> Void)](uiwritingtoolscoordinator/delegate-swift.protocol/writingtoolscoordinator(_:select:in:completion:).md)
  Asks the delegate to update your view’s current text selection.
### Responding to lifecycle changes
- [func writingToolsCoordinator(UIWritingToolsCoordinator, willChangeTo: UIWritingToolsCoordinator.State, completion: () -> Void)](uiwritingtoolscoordinator/delegate-swift.protocol/writingtoolscoordinator(_:willchangeto:completion:).md)
  Notifies your delegate of relevant state changes when Writing Tools is running in your view.
### Animating inline text changes
- [func writingToolsCoordinator(UIWritingToolsCoordinator, requestsPreviewFor: UIWritingToolsCoordinator.TextAnimation, of: NSRange, in: UIWritingToolsCoordinator.Context, completion: (UITargetedPreview?) -> Void)](uiwritingtoolscoordinator/delegate-swift.protocol/writingtoolscoordinator(_:requestspreviewfor:of:in:completion:).md)
  Asks the delegate for a preview image and layout information for the specified text.
- [func writingToolsCoordinator(UIWritingToolsCoordinator, prepareFor: UIWritingToolsCoordinator.TextAnimation, for: NSRange, in: UIWritingToolsCoordinator.Context, completion: () -> Void)](uiwritingtoolscoordinator/delegate-swift.protocol/writingtoolscoordinator(_:preparefor:for:in:completion:).md)
  Prepare for animations for the content that Writing Tools is evaluating.
- [func writingToolsCoordinator(UIWritingToolsCoordinator, finish: UIWritingToolsCoordinator.TextAnimation, for: NSRange, in: UIWritingToolsCoordinator.Context, completion: () -> Void)](uiwritingtoolscoordinator/delegate-swift.protocol/writingtoolscoordinator(_:finish:for:in:completion:).md)
  Asks the delegate to clean up any state related to the specified Writing Tools animation.
### Displaying proofreading marks
- [func writingToolsCoordinator(UIWritingToolsCoordinator, requestsRangeInContextWithIdentifierFor: CGPoint, completion: (NSRange, UUID) -> Void)](uiwritingtoolscoordinator/delegate-swift.protocol/writingtoolscoordinator(_:requestsrangeincontextwithidentifierfor:completion:).md)
  Asks the delegate to provide the location of the character at the specified point in your view’s coordinate system.
- [func writingToolsCoordinator(UIWritingToolsCoordinator, requestsBoundingBezierPathsFor: NSRange, in: UIWritingToolsCoordinator.Context, completion: ([UIBezierPath]) -> Void)](uiwritingtoolscoordinator/delegate-swift.protocol/writingtoolscoordinator(_:requestsboundingbezierpathsfor:in:completion:).md)
  Asks the delegate to provide the bounding paths for the specified text in your view.
- [func writingToolsCoordinator(UIWritingToolsCoordinator, requestsUnderlinePathsFor: NSRange, in: UIWritingToolsCoordinator.Context, completion: ([UIBezierPath]) -> Void)](uiwritingtoolscoordinator/delegate-swift.protocol/writingtoolscoordinator(_:requestsunderlinepathsfor:in:completion:).md)
  Asks the delegate to provide an underline shape for the specified text during a proofreading session.
### Providing animation container views dynamically
- [func writingToolsCoordinator(UIWritingToolsCoordinator, requestsSingleContainerSubrangesOf: NSRange, in: UIWritingToolsCoordinator.Context, completion: ([NSValue]) -> Void)](uiwritingtoolscoordinator/delegate-swift.protocol/writingtoolscoordinator(_:requestssinglecontainersubrangesof:in:completion:).md)
  Asks the delegate to divide the specified range of text into the separate containers that render that text.
- [func writingToolsCoordinator(UIWritingToolsCoordinator, requestsDecorationContainerViewFor: NSRange, in: UIWritingToolsCoordinator.Context, completion: (UIView) -> Void)](uiwritingtoolscoordinator/delegate-swift.protocol/writingtoolscoordinator(_:requestsdecorationcontainerviewfor:in:completion:).md)
  Asks the delegate to provide a decoration view for the specified range of text.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [Adding Writing Tools support to a custom UIKit view](adding-writing-tools-support-to-a-custom-uiview.md)
  Add Writing Tools support, including support for inline replacement animations, to your custom iOS views that contain text.
- [class UIWritingToolsCoordinator](uiwritingtoolscoordinator.md)
  An object that manages interactions between Writing Tools and your custom text view.
- [UIWritingToolsCoordinator.Context](uiwritingtoolscoordinator/context.md)
  A data object that you use to share your custom view’s text with Writing Tools.
- [UIWritingToolsCoordinator.AnimationParameters](uiwritingtoolscoordinator/animationparameters.md)
  An object you use to configure additional tasks or animations to run alongside the Writing Tools animations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiwritingtoolscoordinator/delegate-swift.protocol)*