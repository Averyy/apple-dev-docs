# handleViews

**Framework**: UIKit  
**Kind**: property

The view that draws the selection handles for the selected text.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var handleViews: [any UIView & UITextSelectionHandleView] { get set }
```

## Mentions

- [Adopting system selection UI in custom text views](adopting-system-selection-ui-in-custom-text-views.md)

#### Discussion

When you install the interaction on your text input view, the system installs two views in this property that provide the standard system appearance for the selection handles. You can replace these views with custom ones you provide to change the appearance of the selection handles.

> ❗ **Important**:  When assigning a value to this property, you must provide exactly two views. One view provides the leading selection handle and the other provides the trailing selection handle.

 When assigning a value to this property, you must provide exactly two views. One view provides the leading selection handle and the other provides the trailing selection handle.

## See Also

- [var highlightView: any UIView & UITextSelectionHighlightView](uitextselectiondisplayinteraction/highlightview.md)
  The view that draws the selection highlight behind the rendered text.
- [var cursorView: any UIView & UITextCursorView](uitextselectiondisplayinteraction/cursorview.md)
  The view that draws the caret at the text insertion point.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitextselectiondisplayinteraction/handleviews)*