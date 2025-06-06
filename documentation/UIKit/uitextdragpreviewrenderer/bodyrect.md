# bodyRect

**Framework**: UIKit  
**Kind**: property

The bounding rectangle of the text in the middle of the drag preview.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var bodyRect: CGRect { get }
```

#### Discussion

The body rectangle contains the full lines of text in the middle of the drag preview that doesn’t include the first line and last line. This property can be a zero rectangle. The initial value is also not calculated until the first time it’s used.

## See Also

- [var firstLineRect: CGRect](uitextdragpreviewrenderer/firstlinerect.md)
  The bounding rectangle of the first line of text in the drag preview.
- [var lastLineRect: CGRect](uitextdragpreviewrenderer/lastlinerect.md)
  The bounding rectangle of the last line of text in the drag preview.
- [func adjust(firstLineRect: UnsafeMutablePointer<CGRect>, bodyRect: UnsafeMutablePointer<CGRect>, lastLineRect: UnsafeMutablePointer<CGRect>, textOrigin: CGPoint)](uitextdragpreviewrenderer/adjust(firstlinerect:bodyrect:lastlinerect:textorigin:).md)
  Adjusts the size and origin of the bounding rectangles during a text drag operation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitextdragpreviewrenderer/bodyrect)*