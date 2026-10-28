# UIScrollView.DecelerationRate

**Framework**: UIKit  
**Kind**: struct  
**Role**: Structure

Deceleration rates for the scroll view.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- tvOS
- visionOS

## Declaration

```swift
struct DecelerationRate
```

```c
typedef CGFloat UIScrollViewDecelerationRate;
```

## Overview

You use these constants to set the value of the [`decelerationRate`](./decelerationrate-swift.property.md) property.

## Topics

### Deceleration rates
- [static let normal: UIScrollView.DecelerationRate](./decelerationrate-swift.struct/normal.md)
  The default deceleration rate for a scroll view.
- [static let fast: UIScrollView.DecelerationRate](./decelerationrate-swift.struct/fast.md)
  A fast deceleration rate for a scroll view.
### Initializers
- [init(rawValue: CGFloat)](./decelerationrate-swift.struct/init%28rawvalue%29.md)
  Creates a deceleration rate with the specified raw value.

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Managing the scrolling state
- [var isTracking: Bool](./istracking.md)
  A Boolean value that indicates whether the user has touched the content to initiate scrolling.
- [var isDragging: Bool](./isdragging.md)
  A Boolean value that indicates whether the user has begun scrolling the content.
- [var isDecelerating: Bool](./isdecelerating.md)
  A Boolean value that indicates whether the content is moving in the scroll view after the user lifted their finger.
- [var isScrollAnimating: Bool](./isscrollanimating.md)
  A Boolean value that indicates whether the scroll view is currently animating a scroll update.
- [func stopScrollingAndZooming()](./stopscrollingandzooming%28%29.md)
  Stops active scroll and zoom animations.
- [var decelerationRate: UIScrollView.DecelerationRate](./decelerationrate-swift.property.md)
  A floating-point value that determines the rate of deceleration after the user lifts their finger.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiscrollview/decelerationrate-swift.struct)*