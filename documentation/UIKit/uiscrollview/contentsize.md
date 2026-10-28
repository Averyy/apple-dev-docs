# contentSize

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The size of the content view.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
var contentSize: CGSize { get set }
```

```objc
@property (nonatomic) CGSize contentSize;
```

## Mentions

- [Estimating the height of a table’s scrolling area](../estimating-the-height-of-a-table-s-scrolling-area.md)

## Discussion

The unit of size is points. The default size is [`CGSizeZero`](../../CoreGraphics/cgsizezero.md).

## See Also

### Managing the content size and offset
- [var contentOffset: CGPoint](./contentoffset.md)
  The point at which the origin of the content view is offset from the origin of the scroll view.
- [func setContentOffset(CGPoint, animated: Bool)](./setcontentoffset%28_,animated%29.md)
  Sets the point at which the origin of the content view is offset from the origin of the scroll view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiscrollview/contentsize)*