# interactionShouldBegin(_:at:)

**Framework**: UIKit  
**Kind**: method

Asks the delegate whether the text interaction should begin.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
optional func interactionShouldBegin(_ interaction: UITextInteraction, at point: CGPoint) -> Bool
```

#### Return Value

A Boolean value indicating whether the interaction should begin. Return [`true`](https://developer.apple.com/documentation/swift/true) to let the interaction begin; otherwise, return [`false`](https://developer.apple.com/documentation/swift/false) to prevent the interaction from beginning.

## Parameters

- `interaction`: The text interaction that called this method.
- `point`: The position on the screen where the user is touching.

## See Also

- [func interactionWillBegin(UITextInteraction)](uitextinteractiondelegate/interactionwillbegin(_:).md)
  Tells the delegate that the text interaction will begin.
- [func interactionDidEnd(UITextInteraction)](uitextinteractiondelegate/interactiondidend(_:).md)
  Tells the delegate that the text interaction ended.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitextinteractiondelegate/interactionshouldbegin(_:at:))*