# scrollViewWillBeginDragging(_:)

**Framework**: UIKit  
**Kind**: method

Tells the delegate when the scroll view is about to start scrolling the content.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
optional func scrollViewWillBeginDragging(_ scrollView: UIScrollView)
```

#### Discussion

The delegate might not receive this message until dragging has occurred over a small distance.

## Parameters

- `scrollView`: The scroll-view object that’s about to scroll the content view.

## See Also

- [func scrollViewDidScroll(UIScrollView)](uiscrollviewdelegate/scrollviewdidscroll(_:).md)
  Tells the delegate when the user scrolls the content view within the scroll view.
- [func scrollViewWillEndDragging(UIScrollView, withVelocity: CGPoint, targetContentOffset: UnsafeMutablePointer<CGPoint>)](uiscrollviewdelegate/scrollviewwillenddragging(_:withvelocity:targetcontentoffset:).md)
  Tells the delegate when the user finishes scrolling the content.
- [func scrollViewDidEndDragging(UIScrollView, willDecelerate: Bool)](uiscrollviewdelegate/scrollviewdidenddragging(_:willdecelerate:).md)
  Tells the delegate when dragging ended in the scroll view.
- [func scrollViewShouldScrollToTop(UIScrollView) -> Bool](uiscrollviewdelegate/scrollviewshouldscrolltotop(_:).md)
  Asks the delegate if the scroll view should scroll to the top of the content.
- [func scrollViewDidScrollToTop(UIScrollView)](uiscrollviewdelegate/scrollviewdidscrolltotop(_:).md)
  Tells the delegate that the scroll view scrolled to the top of the content.
- [func scrollViewWillBeginDecelerating(UIScrollView)](uiscrollviewdelegate/scrollviewwillbegindecelerating(_:).md)
  Tells the delegate that the scroll view is starting to decelerate the scrolling movement.
- [func scrollViewDidEndDecelerating(UIScrollView)](uiscrollviewdelegate/scrollviewdidenddecelerating(_:).md)
  Tells the delegate that the scroll view ended decelerating the scrolling movement.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiscrollviewdelegate/scrollviewwillbegindragging(_:))*