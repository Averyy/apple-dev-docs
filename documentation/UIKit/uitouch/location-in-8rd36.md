# location(in:)

**Framework**: UIKit  
**Kind**: method

Returns the current location of the touch in the coordinate system of the given view.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func location(in view: UIView?) -> CGPoint
```

## Mentions

- [Implementing coalesced touch support in an app](implementing-coalesced-touch-support-in-an-app.md)

#### Return Value

A point specifying the location of the receiver in `view`.

#### Discussion

This method returns the current location of a [`UITouch`](uitouch.md) object in the coordinate system of the specified view. Because the touch object might have been forwarded to a view from another view, this method performs any necessary conversion of the touch location to the coordinate system of the specified view.

## Parameters

- `view`: The view object in whose coordinate system you want the touch located. A custom view that is handling the touch may specify   to get the touch location in its own coordinate system. Pass   to get the touch location in the window’s coordinates.

## See Also

- [func previousLocation(in: UIView?) -> CGPoint](uitouch/previouslocation(in:)-22sws.md)
  Returns the previous location of the touch in the coordinate system of the given view.
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

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitouch/location(in:)-8rd36)*