# bounces

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that controls whether the scroll view bounces past the edge of content and back again.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
var bounces: Bool { get set }
```

```objc
@property (nonatomic) BOOL bounces;
```

#### Discussion

If the value of this property is [`true`](../../Swift/true.md), the scroll view bounces when it encounters a boundary of the content. Bouncing visually indicates that scrolling has reached an edge of the content. If the value is [`false`](../../Swift/false.md), scrolling stops immediately at the content boundary without bouncing. The default value is [`true`](../../Swift/true.md).

Setting [`bounces`](./bounces.md) is equivalent to setting both [`bouncesHorizontally`](./bounceshorizontally.md) and [`bouncesVertically`](./bouncesvertically.md) to the same value. To set different behavior for the two axes, set those properties to distinct values.

## See Also

### Configuring the scroll view
- [var isScrollEnabled: Bool](./isscrollenabled.md)
  A Boolean value that determines whether scrolling is enabled.
- [var isDirectionalLockEnabled: Bool](./isdirectionallockenabled.md)
  A Boolean value that determines whether scrolling is disabled in a particular direction.
- [var isPagingEnabled: Bool](./ispagingenabled.md)
  A Boolean value that determines whether paging is enabled for the scroll view.
- [var scrollsToTop: Bool](./scrollstotop.md)
  A Boolean value that controls whether the scroll-to-top gesture is enabled.
- [var bouncesHorizontally: Bool](./bounceshorizontally.md)
  A Boolean value that determines whether the scroll view bounces when it reaches the ends of its horizontal axis.
- [var bouncesVertically: Bool](./bouncesvertically.md)
  A Boolean value that determines whether the scroll view bounces when it reaches the ends of its vertical axis.
- [var alwaysBounceVertical: Bool](./alwaysbouncevertical.md)
  A Boolean value that determines whether bouncing always occurs when vertical scrolling reaches the end of the content.
- [var alwaysBounceHorizontal: Bool](./alwaysbouncehorizontal.md)
  A Boolean value that determines whether bouncing always occurs when horizontal scrolling reaches the end of the content view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiscrollview/bounces)*