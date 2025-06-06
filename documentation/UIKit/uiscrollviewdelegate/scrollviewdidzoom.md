# scrollViewDidZoom(_:)

**Framework**: UIKit  
**Kind**: method

Tells the delegate that the scroll view’s zoom factor changed.

**Availability**:
- iOS 3.2+
- iPadOS 3.2+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
optional func scrollViewDidZoom(_ scrollView: UIScrollView)
```

## Parameters

- `scrollView`: The scroll-view object whose zoom factor changed.

## See Also

- [func viewForZooming(in: UIScrollView) -> UIView?](uiscrollviewdelegate/viewforzooming(in:).md)
  Asks the delegate for the view to scale when zooming is about to occur in the scroll view.
- [func scrollViewWillBeginZooming(UIScrollView, with: UIView?)](uiscrollviewdelegate/scrollviewwillbeginzooming(_:with:).md)
  Tells the delegate that zooming of the content in the scroll view is about to commence.
- [func scrollViewDidEndZooming(UIScrollView, with: UIView?, atScale: CGFloat)](uiscrollviewdelegate/scrollviewdidendzooming(_:with:atscale:).md)
  Tells the delegate when zooming of the content in the scroll view completed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiscrollviewdelegate/scrollviewdidzoom(_:))*