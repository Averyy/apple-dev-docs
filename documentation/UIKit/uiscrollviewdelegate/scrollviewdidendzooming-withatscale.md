# scrollViewDidEndZooming(_:with:atScale:)

**Framework**: UIKit  
**Kind**: method

Tells the delegate when zooming of the content in the scroll view completed.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
optional func scrollViewDidEndZooming(_ scrollView: UIScrollView, with view: UIView?, atScale scale: CGFloat)
```

#### Discussion

The scroll view also calls this method after any “bounce” animations. It also calls this method after animated changes to the zoom level and after a zoom-related gesture ends (regardless of whether the gesture resulted in a change to the zoom level).

## Parameters

- `scrollView`: The scroll-view object displaying the content view.
- `view`: The view object representing that part of the content view that needs to be scaled.
- `scale`: The scale factor to use for scaling; this value must be between the limits established by the   properties   and  .

## See Also

- [func viewForZooming(in: UIScrollView) -> UIView?](uiscrollviewdelegate/viewforzooming(in:).md)
  Asks the delegate for the view to scale when zooming is about to occur in the scroll view.
- [func scrollViewWillBeginZooming(UIScrollView, with: UIView?)](uiscrollviewdelegate/scrollviewwillbeginzooming(_:with:).md)
  Tells the delegate that zooming of the content in the scroll view is about to commence.
- [func scrollViewDidZoom(UIScrollView)](uiscrollviewdelegate/scrollviewdidzoom(_:).md)
  Tells the delegate that the scroll view’s zoom factor changed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiscrollviewdelegate/scrollviewdidendzooming(_:with:atscale:))*