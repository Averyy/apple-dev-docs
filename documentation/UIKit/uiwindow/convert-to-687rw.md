# convert(_:to:)

**Framework**: UIKit  
**Kind**: method

Converts a point from the current window’s coordinate system to the coordinate system of another window.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func convert(_ point: CGPoint, to window: UIWindow?) -> CGPoint
```

#### Return Value

The point converted to the coordinate system of `window`.

## Parameters

- `point`: A point specifying a location in the logical coordinate system of the current window object.
- `window`: The window defining the destination coordinate system for  . Specify   to convert the point to the logical coordinate system of the screen, which is measured in points.

## See Also

- [func convert(CGPoint, from: UIWindow?) -> CGPoint](uiwindow/convert(_:from:)-1gbm1.md)
  Converts a point from the coordinate system of a given window to the coordinate system of the current window.
- [func convert(CGRect, to: UIWindow?) -> CGRect](uiwindow/convert(_:to:)-7k3l0.md)
  Converts a rectangle from the current window’s coordinate system to the coordinate system of another window.
- [func convert(CGRect, from: UIWindow?) -> CGRect](uiwindow/convert(_:from:)-10p2b.md)
  Converts a rectangle from the coordinate system of another window to coordinate system of the current window.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiwindow/convert(_:to:)-687rw)*