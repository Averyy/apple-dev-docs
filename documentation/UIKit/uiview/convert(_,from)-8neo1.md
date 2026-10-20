# convert(_:from:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Converts a point from the coordinate system of a given view to that of the receiver.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- tvOS
- visionOS

## Declaration

```swift
func convert(_ point: CGPoint, from view: UIView?) -> CGPoint
```

```objc
- (CGPoint) convertPoint:(CGPoint) point fromView:(UIView *) view;
```

#### Return Value

The point converted to the local coordinate system (bounds) of the receiver.

## Parameters

- `point`: A point specified in the local coordinate system (bounds) of `view`.
- `view`: The view with `point` in its coordinate system. If `view` is `nil`, this method instead converts from window base coordinates. Otherwise, both `view` and the receiver must belong to the same [`UIWindow`](../uiwindow.md) object.

## See Also

### Converting between view coordinate systems
- [func convert(CGPoint, to: UIView?) -> CGPoint](./convert%28_,to%29-1xizt.md)
  Converts a point from the receiver’s coordinate system to that of the specified view.
- [func convert(CGRect, to: UIView?) -> CGRect](./convert%28_,to%29-2kf3d.md)
  Converts a rectangle from the receiver’s coordinate system to that of another view.
- [func convert(CGRect, from: UIView?) -> CGRect](./convert%28_,from%29-7irzk.md)
  Converts a rectangle from the coordinate system of another view to that of the receiver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiview/convert(_:from:)-8neo1)*