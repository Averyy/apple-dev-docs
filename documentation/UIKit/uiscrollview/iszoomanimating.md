# isZoomAnimating

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the scroll view is currently animating a zoom update.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- Mac Catalyst 17.4+
- tvOS 17.4+
- visionOS 1.1+

## Declaration

```swift
var isZoomAnimating: Bool { get }
```

```objc
@property (nonatomic, readonly, getter=isZoomAnimating) BOOL zoomAnimating;
```

#### Discussion

Call [`stopScrollingAndZooming()`](./stopscrollingandzooming%28%29.md) to stop the animation.

## See Also

### Zooming and panning
- [var panGestureRecognizer: UIPanGestureRecognizer](./pangesturerecognizer.md)
  The underlying gesture recognizer for pan gestures.
- [var pinchGestureRecognizer: UIPinchGestureRecognizer?](./pinchgesturerecognizer.md)
  The underlying gesture recognizer for pinch gestures.
- [func zoom(to: CGRect, animated: Bool)](./zoom%28to,animated%29.md)
  Zooms to a specific area of the content so that it’s visible in the scroll view.
- [var zoomScale: CGFloat](./zoomscale.md)
  A floating-point value that specifies the current scale factor applied to the scroll view’s content.
- [func setZoomScale(CGFloat, animated: Bool)](./setzoomscale%28_,animated%29.md)
  A floating-point value that specifies the current zoom scale.
- [var maximumZoomScale: CGFloat](./maximumzoomscale.md)
  A floating-point value that specifies the maximum scale factor that can apply to the scroll view’s content.
- [var minimumZoomScale: CGFloat](./minimumzoomscale.md)
  A floating-point value that specifies the minimum scale factor that can apply to the scroll view’s content.
- [var isZoomBouncing: Bool](./iszoombouncing.md)
  A Boolean value that indicates that zooming has exceeded the scaling limits specified for the scroll view.
- [var isZooming: Bool](./iszooming.md)
  A Boolean value that indicates whether the content view is currently zooming in or out.
- [var bouncesZoom: Bool](./bounceszoom.md)
  A Boolean value that determines whether the scroll view animates the content scaling when the scaling exceeds the maximum or minimum limits.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiscrollview/iszoomanimating)*