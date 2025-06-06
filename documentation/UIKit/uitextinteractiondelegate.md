# UITextInteractionDelegate

**Framework**: UIKit  
**Kind**: protocol

An interface that an object implements to receive information about text interaction events.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
protocol UITextInteractionDelegate : NSObjectProtocol
```

## Topics

### Handling text interaction events
- [func interactionShouldBegin(UITextInteraction, at: CGPoint) -> Bool](uitextinteractiondelegate/interactionshouldbegin(_:at:).md)
  Asks the delegate whether the text interaction should begin.
- [func interactionWillBegin(UITextInteraction)](uitextinteractiondelegate/interactionwillbegin(_:).md)
  Tells the delegate that the text interaction will begin.
- [func interactionDidEnd(UITextInteraction)](uitextinteractiondelegate/interactiondidend(_:).md)
  Tells the delegate that the text interaction ended.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class UITextInteraction](uitextinteraction.md)
  An interaction that provides text selection gestures and UI to custom text views.
- [enum UITextInteractionMode](uitextinteractionmode.md)
  Modes that determine the selection behaviors that a text interaction provides.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitextinteractiondelegate)*