# textPasteConfigurationSupporting(_:shouldAnimatePasteOf:to:)

**Framework**: UIKit  
**Kind**: method

Asks the delegate if the paste or drop operation should be animated.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
optional func textPasteConfigurationSupporting(_ textPasteConfigurationSupporting: any UITextPasteConfigurationSupporting, shouldAnimatePasteOf attributedString: NSAttributedString, to textRange: UITextRange) -> Bool
```

#### Return Value

[`false`](https://developer.apple.com/documentation/Swift/false) if the paste or drop operation should not be animated; otherwise, [`true`](https://developer.apple.com/documentation/Swift/true).

#### Discussion

If you don’t want the system to animate the paste or drop operation, implement this method and return [`false`](https://developer.apple.com/documentation/Swift/false). The operation is animated if you return [`true`](https://developer.apple.com/documentation/Swift/true) or if this method isn’t implemented.

## Parameters

- `textPasteConfigurationSupporting`: The object that received the paste or drop request.
- `attributedString`: The text that will be added to the text view.
- `textRange`: The position in the text view where the paste or drop operation will place the text.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitextpastedelegate/textpasteconfigurationsupporting(_:shouldanimatepasteof:to:))*