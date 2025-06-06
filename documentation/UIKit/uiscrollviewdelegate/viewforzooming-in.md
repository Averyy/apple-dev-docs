# viewForZooming(in:)

**Framework**: UIKit  
**Kind**: method

Asks the delegate for the view to scale when zooming is about to occur in the scroll view.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
optional func viewForZooming(in scrollView: UIScrollView) -> UIView?
```

#### Return Value

A [`UIView`](uiview.md) object that will be scaled as a result of the zooming gesture. Return `nil` if you don’t want zooming to occur.

## Parameters

- `scrollView`: The scroll-view object displaying the content view.

## See Also

- [func scrollViewWillBeginZooming(UIScrollView, with: UIView?)](uiscrollviewdelegate/scrollviewwillbeginzooming(_:with:).md)
  Tells the delegate that zooming of the content in the scroll view is about to commence.
- [func scrollViewDidEndZooming(UIScrollView, with: UIView?, atScale: CGFloat)](uiscrollviewdelegate/scrollviewdidendzooming(_:with:atscale:).md)
  Tells the delegate when zooming of the content in the scroll view completed.
- [func scrollViewDidZoom(UIScrollView)](uiscrollviewdelegate/scrollviewdidzoom(_:).md)
  Tells the delegate that the scroll view’s zoom factor changed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiscrollviewdelegate/viewforzooming(in:))*