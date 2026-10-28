# scrollViewDidEndZooming(_:with:atScale:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Tells the delegate when zooming of the content in the scroll view completed.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
optional func scrollViewDidEndZooming(_ scrollView: UIScrollView, with view: UIView?, atScale scale: CGFloat)
```

```objc
- (void) scrollViewDidEndZooming:(UIScrollView *) scrollView withView:(UIView *) view atScale:(CGFloat) scale;
```

## Discussion

The scroll view also calls this method after any “bounce” animations. It also calls this method after animated changes to the zoom level and after a zoom-related gesture ends (regardless of whether the gesture resulted in a change to the zoom level).

## Parameters

- `scrollView`: The scroll-view object displaying the content view.
- `view`: The view object representing that part of the content view that needs to be scaled.
- `scale`: The scale factor to use for scaling; this value must be between the limits established by the `UIScrollView` properties [`maximumZoomScale`](../uiscrollview/maximumzoomscale.md) and [`minimumZoomScale`](../uiscrollview/minimumzoomscale.md).

## See Also

### Managing zooming
- [func viewForZooming(in: UIScrollView) -> UIView?](./viewforzooming%28in%29.md)
  Asks the delegate for the view to scale when zooming is about to occur in the scroll view.
- [func scrollViewWillBeginZooming(UIScrollView, with: UIView?)](./scrollviewwillbeginzooming%28_,with%29.md)
  Tells the delegate that zooming of the content in the scroll view is about to commence.
- [func scrollViewDidZoom(UIScrollView)](./scrollviewdidzoom%28_%29.md)
  Tells the delegate that the scroll view’s zoom factor changed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiscrollviewdelegate/scrollviewdidendzooming(_:with:atscale:))*