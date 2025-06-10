# UIScrollView.DecelerationRate

**Framework**: UIKit  
**Kind**: struct

Deceleration rates for the scroll view.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
struct DecelerationRate
```

#### Overview

You use these constants to set the value of the [`decelerationRate`](uiscrollview/decelerationrate-swift.property.md) property.

## Topics

### Deceleration rates
- [static let normal: UIScrollView.DecelerationRate](uiscrollview/decelerationrate-swift.struct/normal.md)
  The default deceleration rate for a scroll view.
- [static let fast: UIScrollView.DecelerationRate](uiscrollview/decelerationrate-swift.struct/fast.md)
  A fast deceleration rate for a scroll view.
### Initializers
- [init(rawValue: CGFloat)](uiscrollview/decelerationrate-swift.struct/init(rawvalue:).md)
  Creates a deceleration rate with the specified raw value.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

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
- [var decelerationRate: UIScrollView.DecelerationRate](uiscrollview/decelerationrate-swift.property.md)
  A floating-point value that determines the rate of deceleration after the user lifts their finger.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiscrollview/decelerationrate-swift.struct)*