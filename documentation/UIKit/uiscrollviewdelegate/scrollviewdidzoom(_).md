# scrollViewDidZoom(_:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Tells the delegate that the scroll view’s zoom factor changed.

**Availability**:
- iOS 3.2+
- iPadOS 3.2+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
optional func scrollViewDidZoom(_ scrollView: UIScrollView)
```

```objc
- (void) scrollViewDidZoom:(UIScrollView *) scrollView;
```

## Parameters

- `scrollView`: The scroll-view object whose zoom factor changed.

## See Also

### Managing zooming
- [func viewForZooming(in: UIScrollView) -> UIView?](./viewforzooming%28in%29.md)
  Asks the delegate for the view to scale when zooming is about to occur in the scroll view.
- [func scrollViewWillBeginZooming(UIScrollView, with: UIView?)](./scrollviewwillbeginzooming%28_,with%29.md)
  Tells the delegate that zooming of the content in the scroll view is about to commence.
- [func scrollViewDidEndZooming(UIScrollView, with: UIView?, atScale: CGFloat)](./scrollviewdidendzooming%28_,with,atscale%29.md)
  Tells the delegate when zooming of the content in the scroll view completed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiscrollviewdelegate/scrollviewdidzoom(_:))*