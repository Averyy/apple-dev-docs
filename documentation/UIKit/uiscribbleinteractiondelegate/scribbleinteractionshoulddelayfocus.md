# scribbleInteractionShouldDelayFocus(_:)

**Framework**: UIKit  
**Kind**: method

Tells the delegate to delay focusing the text input view.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+

## Declaration

```swift
@MainActor
optional func scribbleInteractionShouldDelayFocus(_ interaction: UIScribbleInteraction) -> Bool
```

#### Return Value

Return `true` to delay focusing the text input, `false` otherwise.

#### Discussion

Normally, Scribble focuses the target input as soon as the user starts writing. If you return `true` from this callback, Scribble waits until the user pauses briefly while writing. This is useful in cases where the view shifts or transforms when becoming first responder, which can be disruptive to a user trying to write in the field.

It’s preferable to adjust the UI behavior and minimize these kinds transformations to avoid the layout changes. Only use this method as a last resort, since transcription happens all at once instead of incrementally.

## Parameters

- `interaction`: The text input view asking about delaying focus.

## See Also

- [func scribbleInteraction(UIScribbleInteraction, shouldBeginAt: CGPoint) -> Bool](uiscribbleinteractiondelegate/scribbleinteraction(_:shouldbeginat:).md)
  Returns a Boolean value that indicates whether the delegate should allow writing at a specific location in the view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiscribbleinteractiondelegate/scribbleinteractionshoulddelayfocus(_:))*