# scribbleInteractionDidFinishWriting(_:)

**Framework**: UIKit  
**Kind**: method

Informs the delegate that the user stops writing in the view, after Scribble transcribes and enters the last word.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+

## Declaration

```swift
@MainActor
optional func scribbleInteractionDidFinishWriting(_ interaction: UIScribbleInteraction)
```

#### Discussion

Use this to reset placeholders or other UI elements, if appropriate, to their state from before the user started writing.

## Parameters

- `interaction`: The interaction where the user finished writing.

## See Also

- [func scribbleInteractionWillBeginWriting(UIScribbleInteraction)](uiscribbleinteractiondelegate/scribbleinteractionwillbeginwriting(_:).md)
  Informs the delegate when the user begins writing in the view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiscribbleinteractiondelegate/scribbleinteractiondidfinishwriting(_:))*