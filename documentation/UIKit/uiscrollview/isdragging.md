# isDragging

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the user has begun scrolling the content.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
var isDragging: Bool { get }
```

```objc
@property (nonatomic, readonly, getter=isDragging) BOOL dragging;
```

## Discussion

The value held by this property might require some time or distance of scrolling before it returns [`true`](../../Swift/true.md).

## See Also

### Managing the scrolling state
- [var isTracking: Bool](./istracking.md)
  A Boolean value that indicates whether the user has touched the content to initiate scrolling.
- [var isDecelerating: Bool](./isdecelerating.md)
  A Boolean value that indicates whether the content is moving in the scroll view after the user lifted their finger.
- [var isScrollAnimating: Bool](./isscrollanimating.md)
  A Boolean value that indicates whether the scroll view is currently animating a scroll update.
- [func stopScrollingAndZooming()](./stopscrollingandzooming%28%29.md)
  Stops active scroll and zoom animations.
- [var decelerationRate: UIScrollView.DecelerationRate](./decelerationrate-swift.property.md)
  A floating-point value that determines the rate of deceleration after the user lifts their finger.
- [UIScrollView.DecelerationRate](./decelerationrate-swift.struct.md)
  Deceleration rates for the scroll view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiscrollview/isdragging)*