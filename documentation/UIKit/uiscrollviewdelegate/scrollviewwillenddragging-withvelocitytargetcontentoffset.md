# scrollViewWillEndDragging(_:withVelocity:targetContentOffset:)

**Framework**: UIKit  
**Kind**: method

Tells the delegate when the user finishes scrolling the content.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
optional func scrollViewWillEndDragging(_ scrollView: UIScrollView, withVelocity velocity: CGPoint, targetContentOffset: UnsafeMutablePointer<CGPoint>)
```

#### Discussion

Your application can change the value of the `targetContentOffset` parameter to adjust where the scrollview finishes its scrolling animation.

## Parameters

- `scrollView`: The scroll-view object where the user ended the touch.
- `velocity`: The velocity of the scroll view (in points per millisecond) at the moment the touch was released.
- `targetContentOffset`: The expected offset when the scrolling action decelerates to a stop.

## See Also

- [func scrollViewDidScroll(UIScrollView)](uiscrollviewdelegate/scrollviewdidscroll(_:).md)
  Tells the delegate when the user scrolls the content view within the scroll view.
- [func scrollViewWillBeginDragging(UIScrollView)](uiscrollviewdelegate/scrollviewwillbegindragging(_:).md)
  Tells the delegate when the scroll view is about to start scrolling the content.
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

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiscrollviewdelegate/scrollviewwillenddragging(_:withvelocity:targetcontentoffset:))*