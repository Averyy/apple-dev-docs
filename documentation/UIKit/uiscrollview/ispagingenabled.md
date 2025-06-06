# isPagingEnabled

**Framework**: UIKit  
**Kind**: property

A Boolean value that determines whether paging is enabled for the scroll view.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var isPagingEnabled: Bool { get set }
```

#### Discussion

If the value of this property is [`true`](https://developer.apple.com/documentation/swift/true), the scroll view stops on multiples of the scroll view’s bounds when the user scrolls. The default value is [`false`](https://developer.apple.com/documentation/swift/false).

## See Also

- [var isScrollEnabled: Bool](uiscrollview/isscrollenabled.md)
  A Boolean value that determines whether scrolling is enabled.
- [var isDirectionalLockEnabled: Bool](uiscrollview/isdirectionallockenabled.md)
  A Boolean value that determines whether scrolling is disabled in a particular direction.
- [var scrollsToTop: Bool](uiscrollview/scrollstotop.md)
  A Boolean value that controls whether the scroll-to-top gesture is enabled.
- [var bounces: Bool](uiscrollview/bounces.md)
  A Boolean value that controls whether the scroll view bounces past the edge of content and back again.
- [var bouncesHorizontally: Bool](uiscrollview/bounceshorizontally.md)
  A Boolean value that determines whether the scroll view bounces when it reaches the ends of its horizontal axis.
- [var bouncesVertically: Bool](uiscrollview/bouncesvertically.md)
  A Boolean value that determines whether the scroll view bounces when it reaches the ends of its vertical axis.
- [var alwaysBounceVertical: Bool](uiscrollview/alwaysbouncevertical.md)
  A Boolean value that determines whether bouncing always occurs when vertical scrolling reaches the end of the content.
- [var alwaysBounceHorizontal: Bool](uiscrollview/alwaysbouncehorizontal.md)
  A Boolean value that determines whether bouncing always occurs when horizontal scrolling reaches the end of the content view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiscrollview/ispagingenabled)*