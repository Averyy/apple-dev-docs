# setZoomScale(_:animated:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

A floating-point value that specifies the current zoom scale.

**Availability**:
- iOS 3.0+
- iPadOS 3.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
func setZoomScale(_ scale: CGFloat, animated: Bool)
```

```objc
- (void) setZoomScale:(CGFloat) scale animated:(BOOL) animated;
```

## Discussion

The new scale value should be between the [`minimumZoomScale`](./minimumzoomscale.md) and the [`maximumZoomScale`](./maximumzoomscale.md).

## Parameters

- `scale`: The new value to scale the content to.
- `animated`: [`true`](../../Swift/true.md) to animate the transition to the new scale, [`false`](../../Swift/false.md) to make the transition immediate.

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
- [var maximumZoomScale: CGFloat](./maximumzoomscale.md)
  A floating-point value that specifies the maximum scale factor that can apply to the scroll view’s content.
- [var minimumZoomScale: CGFloat](./minimumzoomscale.md)
  A floating-point value that specifies the minimum scale factor that can apply to the scroll view’s content.
- [var isZoomBouncing: Bool](./iszoombouncing.md)
  A Boolean value that indicates that zooming has exceeded the scaling limits specified for the scroll view.
- [var isZooming: Bool](./iszooming.md)
  A Boolean value that indicates whether the content view is currently zooming in or out.
- [var isZoomAnimating: Bool](./iszoomanimating.md)
  A Boolean value that indicates whether the scroll view is currently animating a zoom update.
- [var bouncesZoom: Bool](./bounceszoom.md)
  A Boolean value that determines whether the scroll view animates the content scaling when the scaling exceeds the maximum or minimum limits.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiscrollview/setzoomscale(_:animated:))*