# convert(_:to:)

**Framework**: UIKit  
**Kind**: method

Converts a point from the receiver’s coordinate system to that of the specified view.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
@MainActor
func convert(_ point: CGPoint, to view: UIView?) -> CGPoint
```

#### Return Value

The point converted to the coordinate system of `view`.

## Parameters

- `point`: A point specified in the local coordinate system (bounds) of the receiver.
- `view`: The view into whose coordinate system   is to be converted. If   is  , this method instead converts to window base coordinates. Otherwise, both   and the receiver must belong to the same   object.

## See Also

- [func convert(CGPoint, from: UIView?) -> CGPoint](uiview/convert(_:from:)-8neo1.md)
  Converts a point from the coordinate system of a given view to that of the receiver.
- [func convert(CGRect, to: UIView?) -> CGRect](uiview/convert(_:to:)-2kf3d.md)
  Converts a rectangle from the receiver’s coordinate system to that of another view.
- [func convert(CGRect, from: UIView?) -> CGRect](uiview/convert(_:from:)-7irzk.md)
  Converts a rectangle from the coordinate system of another view to that of the receiver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiview/convert(_:to:)-1xizt)*