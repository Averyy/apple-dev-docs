# decelerationRate

**Framework**: UIKit  
**Kind**: property

A floating-point value that determines the rate of deceleration after the user lifts their finger.

**Availability**:
- iOS 3.0+
- iPadOS 3.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var decelerationRate: UIScrollView.DecelerationRate { get set }
```

#### Discussion

The default rate is [`normal`](uiscrollview/decelerationrate-swift.struct/normal.md). For possible deceleration rates, see [`UIScrollView.DecelerationRate`](uiscrollview/decelerationrate-swift.struct.md).

## See Also

- [var isTracking: Bool](uiscrollview/istracking.md)
  A Boolean value that indicates whether the user has touched the content to initiate scrolling.
- [var isDragging: Bool](uiscrollview/isdragging.md)
  A Boolean value that indicates whether the user has begun scrolling the content.
- [var isDecelerating: Bool](uiscrollview/isdecelerating.md)
  A Boolean value that indicates whether the content is moving in the scroll view after the user lifted their finger.
- [var isScrollAnimating: Bool](uiscrollview/isscrollanimating.md)
  A Boolean value that indicates whether the scroll view is currently animating a scroll update.
- [func stopScrollingAndZooming()](uiscrollview/stopscrollingandzooming.md)
  Stops active scroll and zoom animations.
- [UIScrollView.DecelerationRate](uiscrollview/decelerationrate-swift.struct.md)
  Deceleration rates for the scroll view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiscrollview/decelerationrate-swift.property)*