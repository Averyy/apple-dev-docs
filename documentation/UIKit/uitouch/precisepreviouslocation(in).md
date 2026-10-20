# precisePreviousLocation(in:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Returns a precise previous location for the touch, when available.

**Availability**:
- iOS 9.1+
- iPadOS 9.1+
- Mac Catalyst 13.1+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func precisePreviousLocation(in view: UIView?) -> CGPoint
```

```objc
- (CGPoint) precisePreviousLocationInView:(UIView *) view;
```

#### Return Value

A precise previous location for the touch.

#### Discussion

Use this method to get additional precision for a touch’s previous location (when available). Do not use the returned point for hit testing. In some cases, hit testing can indicate that the touch is within a view, but hit testing against the more precise location may indicate that the touch is outside of the view.

## Parameters

- `view`: The view that contained the touch.

## See Also

### Getting the location of a touch
- [func location(in: UIView?) -> CGPoint](./location%28in%29-8rd36.md)
  Returns the current location of the touch in the coordinate system of the given view.
- [func previousLocation(in: UIView?) -> CGPoint](./previouslocation%28in%29-22sws.md)
  Returns the previous location of the touch in the coordinate system of the given view.
- [var view: UIView?](./view.md)
  The view to which touches are being delivered, if any.
- [var window: UIWindow?](./window.md)
  The window in which the touch initially occurred.
- [var majorRadius: CGFloat](./majorradius.md)
  The radius (in points) of the touch.
- [var majorRadiusTolerance: CGFloat](./majorradiustolerance.md)
  The tolerance (in points) of the touch’s radius.
- [func preciseLocation(in: UIView?) -> CGPoint](./preciselocation%28in%29.md)
  Returns a precise location for the touch, when available.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitouch/precisepreviouslocation(in:))*