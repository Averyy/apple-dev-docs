# previousLocation(in:)

**Framework**: UIKit  
**Kind**: method

Returns the previous location of the touch in the coordinate system of the given view.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func previousLocation(in view: UIView?) -> CGPoint
```

#### Return Value

This method returns the previous location of a [`UITouch`](uitouch.md) object in the coordinate system of the specified view. Because the touch object might have been forwarded to a view from another view, this method performs any necessary conversion of the touch location to the coordinate system of the specified view.

## Parameters

- `view`: The view object in whose coordinate system you want the touch located. A custom view that is handling the touch may specify   to get the touch location in its own coordinate system. Pass   to get the touch location in the window’s coordinates.

## See Also

- [func location(in: UIView?) -> CGPoint](uitouch/location(in:)-8rd36.md)
  Returns the current location of the touch in the coordinate system of the given view.
- [var view: UIView?](uitouch/view.md)
  The view to which touches are being delivered, if any.
- [var window: UIWindow?](uitouch/window.md)
  The window in which the touch initially occurred.
- [var majorRadius: CGFloat](uitouch/majorradius.md)
  The radius (in points) of the touch.
- [var majorRadiusTolerance: CGFloat](uitouch/majorradiustolerance.md)
  The tolerance (in points) of the touch’s radius.
- [func preciseLocation(in: UIView?) -> CGPoint](uitouch/preciselocation(in:).md)
  Returns a precise location for the touch, when available.
- [func precisePreviousLocation(in: UIView?) -> CGPoint](uitouch/precisepreviouslocation(in:).md)
  Returns a precise previous location for the touch, when available.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitouch/previouslocation(in:)-22sws)*