# majorRadiusTolerance

**Framework**: UIKit  
**Kind**: property

The tolerance (in points) of the touch’s radius.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var majorRadiusTolerance: CGFloat { get }
```

#### Discussion

This value determines the accuracy of the value in the [`majorRadius`](uitouch/majorradius.md) property. Add this value to the radius to get the maximum touch radius. Subtract the value to get the minimum touch radius.

## See Also

- [func location(in: UIView?) -> CGPoint](uitouch/location(in:)-8rd36.md)
  Returns the current location of the touch in the coordinate system of the given view.
- [func previousLocation(in: UIView?) -> CGPoint](uitouch/previouslocation(in:)-22sws.md)
  Returns the previous location of the touch in the coordinate system of the given view.
- [var view: UIView?](uitouch/view.md)
  The view to which touches are being delivered, if any.
- [var window: UIWindow?](uitouch/window.md)
  The window in which the touch initially occurred.
- [var majorRadius: CGFloat](uitouch/majorradius.md)
  The radius (in points) of the touch.
- [func preciseLocation(in: UIView?) -> CGPoint](uitouch/preciselocation(in:).md)
  Returns a precise location for the touch, when available.
- [func precisePreviousLocation(in: UIView?) -> CGPoint](uitouch/precisepreviouslocation(in:).md)
  Returns a precise previous location for the touch, when available.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitouch/majorradiustolerance)*