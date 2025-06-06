# contentOffset

**Framework**: UIKit  
**Kind**: property

The point at which the origin of the content view is offset from the origin of the scroll view.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var contentOffset: CGPoint { get set }
```

## Mentions

- [Estimating the height of a table’s scrolling area](estimating-the-height-of-a-table-s-scrolling-area.md)

#### Discussion

The default value is [`CGPointZero`](https://developer.apple.com/documentation/CoreGraphics/CGPointZero).

## See Also

- [var contentSize: CGSize](uiscrollview/contentsize.md)
  The size of the content view.
- [func setContentOffset(CGPoint, animated: Bool)](uiscrollview/setcontentoffset(_:animated:).md)
  Sets the offset from the content view’s origin that corresponds to the scroll view’s origin.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiscrollview/contentoffset)*