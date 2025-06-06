# scrollViewShouldScrollToTop(_:)

**Framework**: UIKit  
**Kind**: method

Asks the delegate if the scroll view should scroll to the top of the content.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
optional func scrollViewShouldScrollToTop(_ scrollView: UIScrollView) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/swift/true) to permit scrolling to the top of the content, [`false`](https://developer.apple.com/documentation/swift/false) to disallow it.

#### Discussion

If the delegate doesn’t implement this method, [`true`](https://developer.apple.com/documentation/swift/true) is assumed. For the scroll-to-top gesture (a tap on the status bar) to be effective, the [`scrollsToTop`](uiscrollview/scrollstotop.md) property of the [`UIScrollView`](uiscrollview.md) must be set to [`true`](https://developer.apple.com/documentation/swift/true).

## Parameters

- `scrollView`: The scroll-view object requesting this information.

## See Also

- [func scrollViewDidScroll(UIScrollView)](uiscrollviewdelegate/scrollviewdidscroll(_:).md)
  Tells the delegate when the user scrolls the content view within the scroll view.
- [func scrollViewWillBeginDragging(UIScrollView)](uiscrollviewdelegate/scrollviewwillbegindragging(_:).md)
  Tells the delegate when the scroll view is about to start scrolling the content.
- [func scrollViewWillEndDragging(UIScrollView, withVelocity: CGPoint, targetContentOffset: UnsafeMutablePointer<CGPoint>)](uiscrollviewdelegate/scrollviewwillenddragging(_:withvelocity:targetcontentoffset:).md)
  Tells the delegate when the user finishes scrolling the content.
- [func scrollViewDidEndDragging(UIScrollView, willDecelerate: Bool)](uiscrollviewdelegate/scrollviewdidenddragging(_:willdecelerate:).md)
  Tells the delegate when dragging ended in the scroll view.
- [func scrollViewDidScrollToTop(UIScrollView)](uiscrollviewdelegate/scrollviewdidscrolltotop(_:).md)
  Tells the delegate that the scroll view scrolled to the top of the content.
- [func scrollViewWillBeginDecelerating(UIScrollView)](uiscrollviewdelegate/scrollviewwillbegindecelerating(_:).md)
  Tells the delegate that the scroll view is starting to decelerate the scrolling movement.
- [func scrollViewDidEndDecelerating(UIScrollView)](uiscrollviewdelegate/scrollviewdidenddecelerating(_:).md)
  Tells the delegate that the scroll view ended decelerating the scrolling movement.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiscrollviewdelegate/scrollviewshouldscrolltotop(_:))*