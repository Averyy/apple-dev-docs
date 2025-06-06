# UIScribbleInteractionDelegate

**Framework**: UIKit  
**Kind**: protocol

Methods for customizing or suppressing Scribble behavior within text input views.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+

## Declaration

```swift
@MainActor
protocol UIScribbleInteractionDelegate : NSObjectProtocol
```

#### Overview

By default, Scribble let users enter text by writing directly into any editable view that implement [`UITextInput`](uitextinput.md). In apps with customized text fields, you can use the [`UIScribbleInteractionDelegate`](uiscribbleinteractiondelegate.md) callbacks to optimize the UI for a better writing experience, including:

- Opting individual text fields in or out of Scribble interactions.
- Controlling how quickly a given text field responds to input, giving the view an opportunity to change its configuration, if necessary.
- Receiving notifications when the user writing begins and ends.

## Topics

### Allowing and controlling Scribble interactions
- [func scribbleInteraction(UIScribbleInteraction, shouldBeginAt: CGPoint) -> Bool](uiscribbleinteractiondelegate/scribbleinteraction(_:shouldbeginat:).md)
  Returns a Boolean value that indicates whether the delegate should allow writing at a specific location in the view.
- [func scribbleInteractionShouldDelayFocus(UIScribbleInteraction) -> Bool](uiscribbleinteractiondelegate/scribbleinteractionshoulddelayfocus(_:).md)
  Tells the delegate to delay focusing the text input view.
### Tracking Scribble input
- [func scribbleInteractionWillBeginWriting(UIScribbleInteraction)](uiscribbleinteractiondelegate/scribbleinteractionwillbeginwriting(_:).md)
  Informs the delegate when the user begins writing in the view.
- [func scribbleInteractionDidFinishWriting(UIScribbleInteraction)](uiscribbleinteractiondelegate/scribbleinteractiondidfinishwriting(_:).md)
  Informs the delegate that the user stops writing in the view, after Scribble transcribes and enters the last word.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class UIScribbleInteraction](uiscribbleinteraction.md)
  An interaction for customizing the behavior of Scribble on text input views, or for suppressing it entirely in specific cases.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiscribbleinteractiondelegate)*