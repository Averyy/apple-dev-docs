# scrollViewWillEndDragging(_:withVelocity:targetContentOffset:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Tells the delegate when the user finishes scrolling the content.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
optional func scrollViewWillEndDragging(_ scrollView: UIScrollView, withVelocity velocity: CGPoint, targetContentOffset: UnsafeMutablePointer<CGPoint>)
```

```objc
- (void) scrollViewWillEndDragging:(UIScrollView *) scrollView withVelocity:(CGPoint) velocity targetContentOffset:(CGPoint *) targetContentOffset;
```

## Discussion

Your application can change the value of the `targetContentOffset` parameter to adjust where the scrollview finishes its scrolling animation.

## Parameters

- `scrollView`: The scroll-view object where the user ended the touch.
- `velocity`: The velocity of the scroll view (in points per millisecond) at the moment the touch was released.
- `targetContentOffset`: The expected offset when the scrolling action decelerates to a stop.

## See Also

### Responding to scrolling and dragging
- [func scrollViewDidScroll(UIScrollView)](./scrollviewdidscroll%28_%29.md)
  Tells the delegate when the user scrolls the content view within the scroll view.
- [func scrollViewWillBeginDragging(UIScrollView)](./scrollviewwillbegindragging%28_%29.md)
  Tells the delegate when the scroll view is about to start scrolling the content.
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

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiscrollviewdelegate/scrollviewwillenddragging(_:withvelocity:targetcontentoffset:))*