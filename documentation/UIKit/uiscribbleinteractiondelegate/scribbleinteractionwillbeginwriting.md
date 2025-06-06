# scribbleInteractionWillBeginWriting(_:)

**Framework**: UIKit  
**Kind**: method

Informs the delegate when the user begins writing in the view.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+

## Declaration

```swift
@MainActor
optional func scribbleInteractionWillBeginWriting(_ interaction: UIScribbleInteraction)
```

#### Discussion

Use this method to hide custom placeholders or other UI elements that can interfere with writing.

## Parameters

- `interaction`: The interaction where the user started writing.

## See Also

- [func scribbleInteractionDidFinishWriting(UIScribbleInteraction)](uiscribbleinteractiondelegate/scribbleinteractiondidfinishwriting(_:).md)
  Informs the delegate that the user stops writing in the view, after Scribble transcribes and enters the last word.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiscribbleinteractiondelegate/scribbleinteractionwillbeginwriting(_:))*