# isDragging

**Framework**: UIKit  
**Kind**: property

A Boolean value that indicates whether the user has begun scrolling the content.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var isDragging: Bool { get }
```

#### Discussion

The value held by this property might require some time or distance of scrolling before it returns [`true`](https://developer.apple.com/documentation/Swift/true).

## See Also

- [var isTracking: Bool](uiscrollview/istracking.md)
  A Boolean value that indicates whether the user has touched the content to initiate scrolling.
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

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiscrollview/isdragging)*