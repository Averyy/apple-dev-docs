# highlightView

**Framework**: UIKit  
**Kind**: property

The view that draws the selection highlight behind the rendered text.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var highlightView: any UIView & UITextSelectionHighlightView { get set }
```

## Mentions

- [Adopting system selection UI in custom text views](adopting-system-selection-ui-in-custom-text-views.md)

#### Discussion

When you install the interaction on your text input view, the system installs a view in this property that provides the standard system highlight appearance for selections. You can replace this view with a custom one you provide to change the appearance of selections.

## See Also

- [var handleViews: [any UIView & UITextSelectionHandleView]](uitextselectiondisplayinteraction/handleviews.md)
  The view that draws the selection handles for the selected text.
- [var cursorView: any UIView & UITextCursorView](uitextselectiondisplayinteraction/cursorview.md)
  The view that draws the caret at the text insertion point.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitextselectiondisplayinteraction/highlightview)*