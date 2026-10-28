# view

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The view to which touches are being delivered, if any.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
var view: UIView? { get }
```

```objc
@property (nonatomic, strong, readonly, nullable) UIView * view;
```

## Mentions

- [Using responders and the responder chain to handle events](../using-responders-and-the-responder-chain-to-handle-events.md)

## Discussion

The value of this property is the view object to which touches are being delivered, which is not necessarily the view the touch is currently in. For example, when a gesture recognizer recognizes the touch, this property is `nil` because no view is receiving the touch.

## See Also

### Getting the location of a touch
- [func location(in: UIView?) -> CGPoint](./location%28in%29-8rd36.md)
  Returns the current location of the touch in the coordinate system of the given view.
- [func previousLocation(in: UIView?) -> CGPoint](./previouslocation%28in%29-22sws.md)
  Returns the previous location of the touch in the coordinate system of the given view.
- [var window: UIWindow?](./window.md)
  The window in which the touch initially occurred.
- [var majorRadius: CGFloat](./majorradius.md)
  The radius (in points) of the touch.
- [var majorRadiusTolerance: CGFloat](./majorradiustolerance.md)
  The tolerance (in points) of the touch’s radius.
- [func preciseLocation(in: UIView?) -> CGPoint](./preciselocation%28in%29.md)
  Returns a precise location for the touch, when available.
- [func precisePreviousLocation(in: UIView?) -> CGPoint](./precisepreviouslocation%28in%29.md)
  Returns a precise previous location for the touch, when available.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitouch/view)*