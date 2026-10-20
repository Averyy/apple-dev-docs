# interactionDidEnd(_:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Tells the delegate that the text interaction ended.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
optional func interactionDidEnd(_ interaction: UITextInteraction)
```

```objc
- (void) interactionDidEnd:(UITextInteraction *) interaction;
```

## Parameters

- `interaction`: The text interaction that called this method.

## See Also

### Handling text interaction events
- [func interactionShouldBegin(UITextInteraction, at: CGPoint) -> Bool](./interactionshouldbegin%28_,at%29.md)
  Asks the delegate whether the text interaction should begin.
- [func interactionWillBegin(UITextInteraction)](./interactionwillbegin%28_%29.md)
  Tells the delegate that the text interaction will begin.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitextinteractiondelegate/interactiondidend(_:))*