# pinchGestureRecognizer

**Framework**: UIKit  
**Kind**: property

The underlying gesture recognizer for pinch gestures.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var pinchGestureRecognizer: UIPinchGestureRecognizer? { get }
```

#### Discussion

Your application accesses this property when it wants to more precisely control which pinch gestures are recognized by the scroll view.

## See Also

- [var panGestureRecognizer: UIPanGestureRecognizer](uiscrollview/pangesturerecognizer.md)
  The underlying gesture recognizer for pan gestures.
- [func zoom(to: CGRect, animated: Bool)](uiscrollview/zoom(to:animated:).md)
  Zooms to a specific area of the content so that it’s visible in the scroll view.
- [var zoomScale: CGFloat](uiscrollview/zoomscale.md)
  A floating-point value that specifies the current scale factor applied to the scroll view’s content.
- [func setZoomScale(CGFloat, animated: Bool)](uiscrollview/setzoomscale(_:animated:).md)
  A floating-point value that specifies the current zoom scale.
- [var maximumZoomScale: CGFloat](uiscrollview/maximumzoomscale.md)
  A floating-point value that specifies the maximum scale factor that can apply to the scroll view’s content.
- [var minimumZoomScale: CGFloat](uiscrollview/minimumzoomscale.md)
  A floating-point value that specifies the minimum scale factor that can apply to the scroll view’s content.
- [var isZoomBouncing: Bool](uiscrollview/iszoombouncing.md)
  A Boolean value that indicates that zooming has exceeded the scaling limits specified for the scroll view.
- [var isZooming: Bool](uiscrollview/iszooming.md)
  A Boolean value that indicates whether the content view is currently zooming in or out.
- [var isZoomAnimating: Bool](uiscrollview/iszoomanimating.md)
  A Boolean value that indicates whether the scroll view is currently animating a zoom update.
- [var bouncesZoom: Bool](uiscrollview/bounceszoom.md)
  A Boolean value that determines whether the scroll view animates the content scaling when the scaling exceeds the maximum or minimum limits.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiscrollview/pinchgesturerecognizer)*