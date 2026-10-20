# isZoomBouncing

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates that zooming has exceeded the scaling limits specified for the scroll view.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
var isZoomBouncing: Bool { get }
```

```objc
@property (nonatomic, readonly, getter=isZoomBouncing) BOOL zoomBouncing;
```

#### Discussion

The value of this property is [`true`](../../Swift/true.md) if the scroll view is zooming back to a minimum or maximum zoom scaling value; otherwise, the value is [`false`](../../Swift/false.md).

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
- [var isZooming: Bool](./iszooming.md)
  A Boolean value that indicates whether the content view is currently zooming in or out.
- [var isZoomAnimating: Bool](./iszoomanimating.md)
  A Boolean value that indicates whether the scroll view is currently animating a zoom update.
- [var bouncesZoom: Bool](./bounceszoom.md)
  A Boolean value that determines whether the scroll view animates the content scaling when the scaling exceeds the maximum or minimum limits.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiscrollview/iszoombouncing)*