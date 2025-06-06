# convert(_:from:)

**Framework**: UIKit  
**Kind**: method

Converts a rectangle from the coordinate system of another view to that of the receiver.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
@MainActor
func convert(_ rect: CGRect, from view: UIView?) -> CGRect
```

#### Return Value

The converted rectangle.

## Parameters

- `rect`: A rectangle specified in the local coordinate system (bounds) of  .
- `view`: The view with   in its coordinate system. If   is  , this method instead converts from window base coordinates. Otherwise, both   and the receiver must belong to the same   object.

## See Also

- [func convert(CGPoint, to: UIView?) -> CGPoint](uiview/convert(_:to:)-1xizt.md)
  Converts a point from the receiver’s coordinate system to that of the specified view.
- [func convert(CGPoint, from: UIView?) -> CGPoint](uiview/convert(_:from:)-8neo1.md)
  Converts a point from the coordinate system of a given view to that of the receiver.
- [func convert(CGRect, to: UIView?) -> CGRect](uiview/convert(_:to:)-2kf3d.md)
  Converts a rectangle from the receiver’s coordinate system to that of another view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiview/convert(_:from:)-7irzk)*