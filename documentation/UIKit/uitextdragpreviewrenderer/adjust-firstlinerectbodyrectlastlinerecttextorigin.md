# adjust(firstLineRect:bodyRect:lastLineRect:textOrigin:)

**Framework**: UIKit  
**Kind**: method

Adjusts the size and origin of the bounding rectangles during a text drag operation.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func adjust(firstLineRect: UnsafeMutablePointer<CGRect>, bodyRect: UnsafeMutablePointer<CGRect>, lastLineRect: UnsafeMutablePointer<CGRect>, textOrigin origin: CGPoint)
```

#### Discussion

This method does nothing by default. Subclasses may override this method to change the rectangle calculations; for example, in order to enlarge the rectangles by a few points. If you adjust the rectangles, the drag preview changes accordingly.

## Parameters

- `firstLineRect`: The bounding rectangle for the first line of text in the drag preview.
- `bodyRect`: The bounding rectangle for the text in the middle of the drag preview that doesn’t include the first and last line.
- `lastLineRect`: The bounding rectangle for the last line of text in the drag preview.
- `origin`: The origin of the text preview.

## See Also

- [var bodyRect: CGRect](uitextdragpreviewrenderer/bodyrect.md)
  The bounding rectangle of the text in the middle of the drag preview.
- [var firstLineRect: CGRect](uitextdragpreviewrenderer/firstlinerect.md)
  The bounding rectangle of the first line of text in the drag preview.
- [var lastLineRect: CGRect](uitextdragpreviewrenderer/lastlinerect.md)
  The bounding rectangle of the last line of text in the drag preview.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitextdragpreviewrenderer/adjust(firstlinerect:bodyrect:lastlinerect:textorigin:))*