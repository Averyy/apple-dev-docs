# UITextInteractionDelegate

**Framework**: UIKit  
**Kind**: protocol  
**Role**: Protocol

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

```objc
@protocol UITextInteractionDelegate <NSObject>
```

## Topics

### Handling text interaction events
- [func interactionShouldBegin(UITextInteraction, at: CGPoint) -> Bool](./uitextinteractiondelegate/interactionshouldbegin%28_,at%29.md)
  Asks the delegate whether the text interaction should begin.
- [func interactionWillBegin(UITextInteraction)](./uitextinteractiondelegate/interactionwillbegin%28_%29.md)
  Tells the delegate that the text interaction will begin.
- [func interactionDidEnd(UITextInteraction)](./uitextinteractiondelegate/interactiondidend%28_%29.md)
  Tells the delegate that the text interaction ended.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Text interactions
- [class UITextInteraction](./uitextinteraction.md)
  An interaction that provides text selection gestures and UI to custom text views.
- [enum UITextInteractionMode](./uitextinteractionmode.md)
  Modes that determine the selection behaviors that a text interaction provides.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitextinteractiondelegate)*