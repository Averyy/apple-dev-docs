# scribbleInteraction(_:shouldBeginAt:)

**Framework**: UIKit  
**Kind**: method

Returns a Boolean value that indicates whether the delegate should allow writing at a specific location in the view.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+

## Declaration

```swift
@MainActor
optional func scribbleInteraction(_ interaction: UIScribbleInteraction, shouldBeginAt location: CGPoint) -> Bool
```

#### Return Value

Return `false` to disallow writing at the specified location; otherwise return `true`.

#### Discussion

Use this callback to temporarily suppress Scribble in text input views if your app supports drawing over text or special interaction when using Apple Pencil. In cases like this, consider providing a UI for the user to toggle between drawing and handwriting.

This callback can also return `false` for views that handle Apple Pencil events directly, like a drawing canvas, since nearby text fields could take over the events for writing.

## Parameters

- `interaction`: The text view asking if it can start receiving user input.
- `location`: The location of the text view as a   in the view’s coordinate system.

## See Also

- [func scribbleInteractionShouldDelayFocus(UIScribbleInteraction) -> Bool](uiscribbleinteractiondelegate/scribbleinteractionshoulddelayfocus(_:).md)
  Tells the delegate to delay focusing the text input view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiscribbleinteractiondelegate/scribbleinteraction(_:shouldbeginat:))*