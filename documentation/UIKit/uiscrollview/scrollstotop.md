# scrollsToTop

**Framework**: UIKit  
**Kind**: property

A Boolean value that controls whether the scroll-to-top gesture is enabled.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var scrollsToTop: Bool { get set }
```

#### Discussion

The scroll-to-top gesture is a tap on the status bar. When a user makes this gesture, the system asks the scroll view closest to the status bar to scroll to the top. If that scroll view has [`scrollsToTop`](uiscrollview/scrollstotop.md) set to [`false`](https://developer.apple.com/documentation/swift/false), its delegate returns [`false`](https://developer.apple.com/documentation/swift/false) from [`scrollViewShouldScrollToTop(_:)`](uiscrollviewdelegate/scrollviewshouldscrolltotop(_:).md), or the content is already at the top, nothing happens.

After the scroll view scrolls to the top of the content view, it sends the delegate a [`scrollViewDidScrollToTop(_:)`](uiscrollviewdelegate/scrollviewdidscrolltotop(_:).md) message.

The default value of this property is [`true`](https://developer.apple.com/documentation/swift/true).

##### Special Considerations

On iPhone, the scroll-to-top gesture has no effect if there’s more than one scroll view onscreen that has [`scrollsToTop`](uiscrollview/scrollstotop.md) set to [`true`](https://developer.apple.com/documentation/swift/true).

## See Also

- [var isScrollEnabled: Bool](uiscrollview/isscrollenabled.md)
  A Boolean value that determines whether scrolling is enabled.
- [var isDirectionalLockEnabled: Bool](uiscrollview/isdirectionallockenabled.md)
  A Boolean value that determines whether scrolling is disabled in a particular direction.
- [var isPagingEnabled: Bool](uiscrollview/ispagingenabled.md)
  A Boolean value that determines whether paging is enabled for the scroll view.
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

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiscrollview/scrollstotop)*