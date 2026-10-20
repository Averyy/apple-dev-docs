# scribbleInteractionDidFinishWriting(_:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Informs the delegate that the user stops writing in the view, after Scribble transcribes and enters the last word.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+

## Declaration

```swift
optional func scribbleInteractionDidFinishWriting(_ interaction: UIScribbleInteraction)
```

```objc
- (void) scribbleInteractionDidFinishWriting:(UIScribbleInteraction *) interaction;
```

#### Discussion

Use this to reset placeholders or other UI elements, if appropriate, to their state from before the user started writing.

## Parameters

- `interaction`: The interaction where the user finished writing.

## See Also

### Tracking Scribble input
- [func scribbleInteractionWillBeginWriting(UIScribbleInteraction)](./scribbleinteractionwillbeginwriting%28_%29.md)
  Informs the delegate when the user begins writing in the view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiscribbleinteractiondelegate/scribbleinteractiondidfinishwriting(_:))*