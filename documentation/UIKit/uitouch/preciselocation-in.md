# preciseLocation(in:)

**Framework**: UIKit  
**Kind**: method

Returns a precise location for the touch, when available.

**Availability**:
- iOS 9.1+
- iPadOS 9.1+
- Mac Catalyst 13.1+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func preciseLocation(in view: UIView?) -> CGPoint
```

## Mentions

- [Implementing coalesced touch support in an app](implementing-coalesced-touch-support-in-an-app.md)

#### Return Value

A precise location for the touch.

#### Discussion

Use this method to get additional precision for a touch (when available). Do not use the returned point for hit testing. In some cases, hit testing can indicate that the touch is within a view, but hit testing against the more precise location may indicate that the touch is outside of the view.

## Parameters

- `view`: The view that contains the touch.

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
- [var majorRadiusTolerance: CGFloat](uitouch/majorradiustolerance.md)
  The tolerance (in points) of the touch’s radius.
- [func precisePreviousLocation(in: UIView?) -> CGPoint](uitouch/precisepreviouslocation(in:).md)
  Returns a precise previous location for the touch, when available.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitouch/preciselocation(in:))*