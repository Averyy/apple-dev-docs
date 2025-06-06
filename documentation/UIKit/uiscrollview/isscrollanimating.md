# isScrollAnimating

**Framework**: UIKit  
**Kind**: property

A Boolean value that indicates whether the scroll view is currently animating a scroll update.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- Mac Catalyst 17.4+
- tvOS 17.4+
- visionOS 1.1+

## Declaration

```swift
@MainActor
var isScrollAnimating: Bool { get }
```

#### Discussion

Call [`stopScrollingAndZooming()`](uiscrollview/stopscrollingandzooming().md) to stop the animation.

## See Also

- [var isTracking: Bool](uiscrollview/istracking.md)
  A Boolean value that indicates whether the user has touched the content to initiate scrolling.
- [var isDragging: Bool](uiscrollview/isdragging.md)
  A Boolean value that indicates whether the user has begun scrolling the content.
- [var isDecelerating: Bool](uiscrollview/isdecelerating.md)
  A Boolean value that indicates whether the content is moving in the scroll view after the user lifted their finger.
- [func stopScrollingAndZooming()](uiscrollview/stopscrollingandzooming.md)
  Stops active scroll and zoom animations.
- [var decelerationRate: UIScrollView.DecelerationRate](uiscrollview/decelerationrate-swift.property.md)
  A floating-point value that determines the rate of deceleration after the user lifts their finger.
- [UIScrollView.DecelerationRate](uiscrollview/decelerationrate-swift.struct.md)
  Deceleration rates for the scroll view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiscrollview/isscrollanimating)*