# UITextDragPreviewRenderer

**Framework**: UIKit  
**Kind**: class

Renders previews of text dragged by the user.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
class UITextDragPreviewRenderer
```

#### Overview

Use this class to provide custom previews of dragged text that follows user interface guidelines and handles right-to-left text. You provide the layout manager and the range to render the preview.

Subclasses may override the [`adjust(firstLineRect:bodyRect:lastLineRect:textOrigin:)`](uitextdragpreviewrenderer/adjust(firstlinerect:bodyrect:lastlinerect:textorigin:).md) method to modify the detected rectangles as needed during the drag operation.

## Topics

### Initializing a text drag preview renderer
- [convenience init(layoutManager: NSLayoutManager, range: NSRange)](uitextdragpreviewrenderer/init(layoutmanager:range:).md)
  Initializes and returns a text drag preview renderer with the specified layout managers and range to render the text drag preview.
- [init(layoutManager: NSLayoutManager, range: NSRange, unifyRects: Bool)](uitextdragpreviewrenderer/init(layoutmanager:range:unifyrects:).md)
  Returns an initialized renderer of a text drag preview with the specified layout manager, range, and rectangle detection behavior.
### Getting and setting bounding rectangles
- [var bodyRect: CGRect](uitextdragpreviewrenderer/bodyrect.md)
  The bounding rectangle of the text in the middle of the drag preview.
- [var firstLineRect: CGRect](uitextdragpreviewrenderer/firstlinerect.md)
  The bounding rectangle of the first line of text in the drag preview.
- [var lastLineRect: CGRect](uitextdragpreviewrenderer/lastlinerect.md)
  The bounding rectangle of the last line of text in the drag preview.
- [func adjust(firstLineRect: UnsafeMutablePointer<CGRect>, bodyRect: UnsafeMutablePointer<CGRect>, lastLineRect: UnsafeMutablePointer<CGRect>, textOrigin: CGPoint)](uitextdragpreviewrenderer/adjust(firstlinerect:bodyrect:lastlinerect:textorigin:).md)
  Adjusts the size and origin of the bounding rectangles during a text drag operation.
### Getting the preview image
- [var image: UIImage](uitextdragpreviewrenderer/image.md)
  The image of the text drag preview that’s rendered by the layout manager.
### Getting the layout manager
- [var layoutManager: NSLayoutManager](uitextdragpreviewrenderer/layoutmanager.md)
  The layout manager that renders the text drag preview.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [protocol UITextDragRequest](uitextdragrequest.md)
  The interface for describing the attributes of a drag activity originating in a text view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitextdragpreviewrenderer)*