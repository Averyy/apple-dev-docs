# bounces

**Framework**: UIKit  
**Kind**: property

A Boolean value that controls whether the scroll view bounces past the edge of content and back again.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var bounces: Bool { get set }
```

#### Discussion

If the value of this property is [`true`](https://developer.apple.com/documentation/swift/true), the scroll view bounces when it encounters a boundary of the content. Bouncing visually indicates that scrolling has reached an edge of the content. If the value is [`false`](https://developer.apple.com/documentation/swift/false), scrolling stops immediately at the content boundary without bouncing. The default value is [`true`](https://developer.apple.com/documentation/swift/true).

Setting [`bounces`](uiscrollview/bounces.md) is equivalent to setting both [`bouncesHorizontally`](uiscrollview/bounceshorizontally.md) and [`bouncesVertically`](uiscrollview/bouncesvertically.md) to the same value. To set different behavior for the two axes, set those properties to distinct values.

## See Also

- [var isScrollEnabled: Bool](uiscrollview/isscrollenabled.md)
  A Boolean value that determines whether scrolling is enabled.
- [var isDirectionalLockEnabled: Bool](uiscrollview/isdirectionallockenabled.md)
  A Boolean value that determines whether scrolling is disabled in a particular direction.
- [var isPagingEnabled: Bool](uiscrollview/ispagingenabled.md)
  A Boolean value that determines whether paging is enabled for the scroll view.
- [var scrollsToTop: Bool](uiscrollview/scrollstotop.md)
  A Boolean value that controls whether the scroll-to-top gesture is enabled.
- [var bouncesHorizontally: Bool](uiscrollview/bounceshorizontally.md)
  A Boolean value that determines whether the scroll view bounces when it reaches the ends of its horizontal axis.
- [var bouncesVertically: Bool](uiscrollview/bouncesvertically.md)
  A Boolean value that determines whether the scroll view bounces when it reaches the ends of its vertical axis.
- [var alwaysBounceVertical: Bool](uiscrollview/alwaysbouncevertical.md)
  A Boolean value that determines whether bouncing always occurs when vertical scrolling reaches the end of the content.
- [var alwaysBounceHorizontal: Bool](uiscrollview/alwaysbouncehorizontal.md)
  A Boolean value that determines whether bouncing always occurs when horizontal scrolling reaches the end of the content view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiscrollview/bounces)*