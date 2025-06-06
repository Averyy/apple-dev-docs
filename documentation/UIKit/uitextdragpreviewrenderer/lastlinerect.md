# lastLineRect

**Framework**: UIKit  
**Kind**: property

The bounding rectangle of the last line of text in the drag preview.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var lastLineRect: CGRect { get }
```

#### Discussion

The last line rectangle contains the last line of text in the drag preview that may be a partial line. This property can be a zero rectangle. The initial value is also not calculated until the first time it’s used.

## See Also

- [var bodyRect: CGRect](uitextdragpreviewrenderer/bodyrect.md)
  The bounding rectangle of the text in the middle of the drag preview.
- [var firstLineRect: CGRect](uitextdragpreviewrenderer/firstlinerect.md)
  The bounding rectangle of the first line of text in the drag preview.
- [func adjust(firstLineRect: UnsafeMutablePointer<CGRect>, bodyRect: UnsafeMutablePointer<CGRect>, lastLineRect: UnsafeMutablePointer<CGRect>, textOrigin: CGPoint)](uitextdragpreviewrenderer/adjust(firstlinerect:bodyrect:lastlinerect:textorigin:).md)
  Adjusts the size and origin of the bounding rectangles during a text drag operation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitextdragpreviewrenderer/lastlinerect)*