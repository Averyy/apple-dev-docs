# view

**Framework**: UIKit  
**Kind**: property

The view to which touches are being delivered, if any.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var view: UIView? { get }
```

## Mentions

- [Using responders and the responder chain to handle events](using-responders-and-the-responder-chain-to-handle-events.md)

#### Discussion

The value of this property is the view object to which touches are being delivered, which is not necessarily the view the touch is currently in. For example, when a gesture recognizer recognizes the touch, this property is `nil` because no view is receiving the touch.

## See Also

- [func location(in: UIView?) -> CGPoint](uitouch/location(in:)-8rd36.md)
  Returns the current location of the touch in the coordinate system of the given view.
- [func previousLocation(in: UIView?) -> CGPoint](uitouch/previouslocation(in:)-22sws.md)
  Returns the previous location of the touch in the coordinate system of the given view.
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

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitouch/view)*