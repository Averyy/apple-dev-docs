# isDecelerating

**Framework**: UIKit  
**Kind**: property

A Boolean value that indicates whether the content is moving in the scroll view after the user lifted their finger.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var isDecelerating: Bool { get }
```

#### Discussion

The returned value is [`true`](https://developer.apple.com/documentation/Swift/true) if user isn’t dragging the content but scrolling is still occurring.

## See Also

- [var isTracking: Bool](uiscrollview/istracking.md)
  A Boolean value that indicates whether the user has touched the content to initiate scrolling.
- [var isDragging: Bool](uiscrollview/isdragging.md)
  A Boolean value that indicates whether the user has begun scrolling the content.
- [var isScrollAnimating: Bool](uiscrollview/isscrollanimating.md)
  A Boolean value that indicates whether the scroll view is currently animating a scroll update.
- [func stopScrollingAndZooming()](uiscrollview/stopscrollingandzooming.md)
  Stops active scroll and zoom animations.
- [var decelerationRate: UIScrollView.DecelerationRate](uiscrollview/decelerationrate-swift.property.md)
  A floating-point value that determines the rate of deceleration after the user lifts their finger.
- [UIScrollView.DecelerationRate](uiscrollview/decelerationrate-swift.struct.md)
  Deceleration rates for the scroll view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiscrollview/isdecelerating)*