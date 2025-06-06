# interactionDidEnd(_:)

**Framework**: UIKit  
**Kind**: method

Tells the delegate that the text interaction ended.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
optional func interactionDidEnd(_ interaction: UITextInteraction)
```

## Parameters

- `interaction`: The text interaction that called this method.

## See Also

- [func interactionShouldBegin(UITextInteraction, at: CGPoint) -> Bool](uitextinteractiondelegate/interactionshouldbegin(_:at:).md)
  Asks the delegate whether the text interaction should begin.
- [func interactionWillBegin(UITextInteraction)](uitextinteractiondelegate/interactionwillbegin(_:).md)
  Tells the delegate that the text interaction will begin.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitextinteractiondelegate/interactiondidend(_:))*