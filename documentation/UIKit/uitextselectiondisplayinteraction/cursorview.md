# cursorView

**Framework**: UIKit  
**Kind**: property

The view that draws the caret at the text insertion point.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var cursorView: any UIView & UITextCursorView { get set }
```

## Mentions

- [Adopting system selection UI in custom text views](adopting-system-selection-ui-in-custom-text-views.md)

#### Discussion

When you install the interaction on your text input view, the system installs a view in this property that provides the standard system appearance for the caret at the insertion point. You can replace this view with a custom one you provide to change the appearance of the caret.

## See Also

- [var highlightView: any UIView & UITextSelectionHighlightView](uitextselectiondisplayinteraction/highlightview.md)
  The view that draws the selection highlight behind the rendered text.
- [var handleViews: [any UIView & UITextSelectionHandleView]](uitextselectiondisplayinteraction/handleviews.md)
  The view that draws the selection handles for the selected text.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitextselectiondisplayinteraction/cursorview)*