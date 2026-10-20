# contentOffset

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The point at which the origin of the content view is offset from the origin of the scroll view.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
var contentOffset: CGPoint { get set }
```

```objc
@property (nonatomic) CGPoint contentOffset;
```

## Mentions

- [Estimating the height of a table’s scrolling area](../estimating-the-height-of-a-table-s-scrolling-area.md)

#### Discussion

The default value is [`CGPointZero`](../../CoreGraphics/cgpointzero.md).

## See Also

### Managing the content size and offset
- [var contentSize: CGSize](./contentsize.md)
  The size of the content view.
- [func setContentOffset(CGPoint, animated: Bool)](./setcontentoffset%28_,animated%29.md)
  Sets the point at which the origin of the content view is offset from the origin of the scroll view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiscrollview/contentoffset)*