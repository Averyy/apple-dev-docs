# alwaysBounceHorizontal

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that determines whether bouncing always occurs when horizontal scrolling reaches the end of the content view.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
var alwaysBounceHorizontal: Bool { get set }
```

```objc
@property (nonatomic) BOOL alwaysBounceHorizontal;
```

#### Discussion

If the value of this property is [`true`](../../Swift/true.md) and [`bouncesHorizontally`](./bounceshorizontally.md) is [`true`](../../Swift/true.md), the scroll view allows horizontal dragging even if the content is smaller than the bounds of the scroll view. The default value is [`false`](../../Swift/false.md).

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
- [var bounces: Bool](./bounces.md)
  A Boolean value that controls whether the scroll view bounces past the edge of content and back again.
- [var bouncesHorizontally: Bool](./bounceshorizontally.md)
  A Boolean value that determines whether the scroll view bounces when it reaches the ends of its horizontal axis.
- [var bouncesVertically: Bool](./bouncesvertically.md)
  A Boolean value that determines whether the scroll view bounces when it reaches the ends of its vertical axis.
- [var alwaysBounceVertical: Bool](./alwaysbouncevertical.md)
  A Boolean value that determines whether bouncing always occurs when vertical scrolling reaches the end of the content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiscrollview/alwaysbouncehorizontal)*