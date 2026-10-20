# scrollViewShouldScrollToTop(_:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Asks the delegate if the scroll view should scroll to the top of the content.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
optional func scrollViewShouldScrollToTop(_ scrollView: UIScrollView) -> Bool
```

```objc
- (BOOL) scrollViewShouldScrollToTop:(UIScrollView *) scrollView;
```

#### Return Value

[`true`](../../Swift/true.md) to permit scrolling to the top of the content, [`false`](../../Swift/false.md) to disallow it.

#### Discussion

If the delegate doesn’t implement this method, [`true`](../../Swift/true.md) is assumed. For the scroll-to-top gesture (a tap on the status bar) to be effective, the [`scrollsToTop`](../uiscrollview/scrollstotop.md) property of the [`UIScrollView`](../uiscrollview.md) must be set to [`true`](../../Swift/true.md).

## Parameters

- `scrollView`: The scroll-view object requesting this information.

## See Also

### Responding to scrolling and dragging
- [func scrollViewDidScroll(UIScrollView)](./scrollviewdidscroll%28_%29.md)
  Tells the delegate when the user scrolls the content view within the scroll view.
- [func scrollViewWillBeginDragging(UIScrollView)](./scrollviewwillbegindragging%28_%29.md)
  Tells the delegate when the scroll view is about to start scrolling the content.
- [func scrollViewWillEndDragging(UIScrollView, withVelocity: CGPoint, targetContentOffset: UnsafeMutablePointer<CGPoint>)](./scrollviewwillenddragging%28_,withvelocity,targetcontentoffset%29.md)
  Tells the delegate when the user finishes scrolling the content.
- [func scrollViewDidEndDragging(UIScrollView, willDecelerate: Bool)](./scrollviewdidenddragging%28_,willdecelerate%29.md)
  Tells the delegate when dragging ended in the scroll view.
- [func scrollViewDidScrollToTop(UIScrollView)](./scrollviewdidscrolltotop%28_%29.md)
  Tells the delegate that the scroll view scrolled to the top of the content.
- [func scrollViewWillBeginDecelerating(UIScrollView)](./scrollviewwillbegindecelerating%28_%29.md)
  Tells the delegate that the scroll view is starting to decelerate the scrolling movement.
- [func scrollViewDidEndDecelerating(UIScrollView)](./scrollviewdidenddecelerating%28_%29.md)
  Tells the delegate that the scroll view ended decelerating the scrolling movement.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiscrollviewdelegate/scrollviewshouldscrolltotop(_:))*