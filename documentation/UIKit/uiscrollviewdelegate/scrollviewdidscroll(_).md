# scrollViewDidScroll(_:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Tells the delegate when the user scrolls the content view within the scroll view.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
optional func scrollViewDidScroll(_ scrollView: UIScrollView)
```

```objc
- (void) scrollViewDidScroll:(UIScrollView *) scrollView;
```

## Discussion

The delegate typically implements this method to obtain the change in content offset from `scrollView` and draw the affected portion of the content view.

## Parameters

- `scrollView`: The scroll-view object in which the scrolling occurred.

## See Also

### Responding to scrolling and dragging
- [func scrollViewWillBeginDragging(UIScrollView)](./scrollviewwillbegindragging%28_%29.md)
  Tells the delegate when the scroll view is about to start scrolling the content.
- [func scrollViewWillEndDragging(UIScrollView, withVelocity: CGPoint, targetContentOffset: UnsafeMutablePointer<CGPoint>)](./scrollviewwillenddragging%28_,withvelocity,targetcontentoffset%29.md)
  Tells the delegate when the user finishes scrolling the content.
- [func scrollViewDidEndDragging(UIScrollView, willDecelerate: Bool)](./scrollviewdidenddragging%28_,willdecelerate%29.md)
  Tells the delegate when dragging ended in the scroll view.
- [func scrollViewShouldScrollToTop(UIScrollView) -> Bool](./scrollviewshouldscrolltotop%28_%29.md)
  Asks the delegate if the scroll view should scroll to the top of the content.
- [func scrollViewDidScrollToTop(UIScrollView)](./scrollviewdidscrolltotop%28_%29.md)
  Tells the delegate that the scroll view scrolled to the top of the content.
- [func scrollViewWillBeginDecelerating(UIScrollView)](./scrollviewwillbegindecelerating%28_%29.md)
  Tells the delegate that the scroll view is starting to decelerate the scrolling movement.
- [func scrollViewDidEndDecelerating(UIScrollView)](./scrollviewdidenddecelerating%28_%29.md)
  Tells the delegate that the scroll view ended decelerating the scrolling movement.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiscrollviewdelegate/scrollviewdidscroll(_:))*