# isTracking

**Framework**: UIKit  
**Kind**: property

A Boolean value that indicates whether the user has touched the content to initiate scrolling.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var isTracking: Bool { get }
```

#### Discussion

The value of this property is [`true`](https://developer.apple.com/documentation/Swift/true) if the user has touched the content view but might not have yet have started dragging it.

## See Also

- [var isDragging: Bool](uiscrollview/isdragging.md)
  A Boolean value that indicates whether the user has begun scrolling the content.
- [var isDecelerating: Bool](uiscrollview/isdecelerating.md)
  A Boolean value that indicates whether the content is moving in the scroll view after the user lifted their finger.
- [var isScrollAnimating: Bool](uiscrollview/isscrollanimating.md)
  A Boolean value that indicates whether the scroll view is currently animating a scroll update.
- [func stopScrollingAndZooming()](uiscrollview/stopscrollingandzooming.md)
  Stops active scroll and zoom animations.
- [var decelerationRate: UIScrollView.DecelerationRate](uiscrollview/decelerationrate-swift.property.md)
  A floating-point value that determines the rate of deceleration after the user lifts their finger.
- [UIScrollView.DecelerationRate](uiscrollview/decelerationrate-swift.struct.md)
  Deceleration rates for the scroll view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiscrollview/istracking)*