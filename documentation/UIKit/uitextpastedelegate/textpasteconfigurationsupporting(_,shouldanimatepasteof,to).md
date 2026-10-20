# textPasteConfigurationSupporting(_:shouldAnimatePasteOf:to:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Asks the delegate if the paste or drop operation should be animated.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
optional func textPasteConfigurationSupporting(_ textPasteConfigurationSupporting: any UITextPasteConfigurationSupporting, shouldAnimatePasteOf attributedString: NSAttributedString, to textRange: UITextRange) -> Bool
```

```objc
- (BOOL) textPasteConfigurationSupporting:(id<UITextPasteConfigurationSupporting>) textPasteConfigurationSupporting shouldAnimatePasteOfAttributedString:(NSAttributedString *) attributedString toRange:(UITextRange *) textRange;
```

#### Return Value

[`false`](../../Swift/false.md) if the paste or drop operation should not be animated; otherwise, [`true`](../../Swift/true.md).

#### Discussion

If you don’t want the system to animate the paste or drop operation, implement this method and return [`false`](../../Swift/false.md). The operation is animated if you return [`true`](../../Swift/true.md) or if this method isn’t implemented.

## Parameters

- `textPasteConfigurationSupporting`: The object that received the paste or drop request.
- `attributedString`: The text that will be added to the text view.
- `textRange`: The position in the text view where the paste or drop operation will place the text.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitextpastedelegate/textpasteconfigurationsupporting(_:shouldanimatepasteof:to:))*