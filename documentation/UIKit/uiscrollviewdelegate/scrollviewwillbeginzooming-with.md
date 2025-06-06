# scrollViewWillBeginZooming(_:with:)

**Framework**: UIKit  
**Kind**: method

Tells the delegate that zooming of the content in the scroll view is about to commence.

**Availability**:
- iOS 3.2+
- iPadOS 3.2+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
optional func scrollViewWillBeginZooming(_ scrollView: UIScrollView, with view: UIView?)
```

#### Discussion

This method is called at the beginning of zoom gestures and in cases where a change in zoom level is to be animated. You can use this method to store state information or perform any additional actions prior to zooming the view’s content.

## Parameters

- `scrollView`: The scroll-view object displaying the content view.
- `view`: The view object whose content is about to be zoomed.

## See Also

- [func viewForZooming(in: UIScrollView) -> UIView?](uiscrollviewdelegate/viewforzooming(in:).md)
  Asks the delegate for the view to scale when zooming is about to occur in the scroll view.
- [func scrollViewDidEndZooming(UIScrollView, with: UIView?, atScale: CGFloat)](uiscrollviewdelegate/scrollviewdidendzooming(_:with:atscale:).md)
  Tells the delegate when zooming of the content in the scroll view completed.
- [func scrollViewDidZoom(UIScrollView)](uiscrollviewdelegate/scrollviewdidzoom(_:).md)
  Tells the delegate that the scroll view’s zoom factor changed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiscrollviewdelegate/scrollviewwillbeginzooming(_:with:))*