# majorRadius

**Framework**: UIKit  
**Kind**: property

The radius (in points) of the touch.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var majorRadius: CGFloat { get }
```

#### Discussion

Use the value in this property to determine the size of the touch that was reported by the hardware. This value is an approximation of the size and can vary by the amount specified in the [`majorRadiusTolerance`](uitouch/majorradiustolerance.md) property.

## See Also

- [func location(in: UIView?) -> CGPoint](uitouch/location(in:)-8rd36.md)
  Returns the current location of the touch in the coordinate system of the given view.
- [func previousLocation(in: UIView?) -> CGPoint](uitouch/previouslocation(in:)-22sws.md)
  Returns the previous location of the touch in the coordinate system of the given view.
- [var view: UIView?](uitouch/view.md)
  The view to which touches are being delivered, if any.
- [var window: UIWindow?](uitouch/window.md)
  The window in which the touch initially occurred.
- [var majorRadiusTolerance: CGFloat](uitouch/majorradiustolerance.md)
  The tolerance (in points) of the touch’s radius.
- [func preciseLocation(in: UIView?) -> CGPoint](uitouch/preciselocation(in:).md)
  Returns a precise location for the touch, when available.
- [func precisePreviousLocation(in: UIView?) -> CGPoint](uitouch/precisepreviouslocation(in:).md)
  Returns a precise previous location for the touch, when available.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitouch/majorradius)*