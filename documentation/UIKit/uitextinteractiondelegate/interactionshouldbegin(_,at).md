# interactionShouldBegin(_:at:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Asks the delegate whether the text interaction should begin.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
optional func interactionShouldBegin(_ interaction: UITextInteraction, at point: CGPoint) -> Bool
```

```objc
- (BOOL) interactionShouldBegin:(UITextInteraction *) interaction atPoint:(CGPoint) point;
```

## Return Value

A Boolean value indicating whether the interaction should begin. Return [`true`](../../Swift/true.md) to let the interaction begin; otherwise, return [`false`](../../Swift/false.md) to prevent the interaction from beginning.

## Parameters

- `interaction`: The text interaction that called this method.
- `point`: The position on the screen where the user is touching.

## See Also

### Handling text interaction events
- [func interactionWillBegin(UITextInteraction)](./interactionwillbegin%28_%29.md)
  Tells the delegate that the text interaction will begin.
- [func interactionDidEnd(UITextInteraction)](./interactiondidend%28_%29.md)
  Tells the delegate that the text interaction ended.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitextinteractiondelegate/interactionshouldbegin(_:at:))*