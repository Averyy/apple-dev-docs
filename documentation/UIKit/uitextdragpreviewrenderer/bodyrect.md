# bodyRect

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The bounding rectangle of the text in the middle of the drag preview.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
var bodyRect: CGRect { get }
```

```objc
@property (nonatomic, readonly) CGRect bodyRect;
```

## Discussion

The body rectangle contains the full lines of text in the middle of the drag preview that doesn’t include the first line and last line. This property can be a zero rectangle. The initial value is also not calculated until the first time it’s used.

## See Also

### Getting and setting bounding rectangles
- [var firstLineRect: CGRect](./firstlinerect.md)
  The bounding rectangle of the first line of text in the drag preview.
- [var lastLineRect: CGRect](./lastlinerect.md)
  The bounding rectangle of the last line of text in the drag preview.
- [func adjust(firstLineRect: UnsafeMutablePointer<CGRect>, bodyRect: UnsafeMutablePointer<CGRect>, lastLineRect: UnsafeMutablePointer<CGRect>, textOrigin: CGPoint)](./adjust%28firstlinerect,bodyrect,lastlinerect,textorigin%29.md)
  Adjusts the size and origin of the bounding rectangles during a text drag operation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitextdragpreviewrenderer/bodyrect)*