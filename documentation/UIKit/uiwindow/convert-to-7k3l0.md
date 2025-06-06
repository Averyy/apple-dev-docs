# convert(_:to:)

**Framework**: UIKit  
**Kind**: method

Converts a rectangle from the current window’s coordinate system to the coordinate system of another window.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func convert(_ rect: CGRect, to window: UIWindow?) -> CGRect
```

#### Return Value

The rectangle converted to the coordinate system of `window`.

## Parameters

- `rect`: A rectangle in the current window’s coordinate system.
- `window`: The window defining the destination coordinate system for  . Specify   to convert the rectangle to the logical coordinate system of the screen, which is measured in points.

## See Also

- [func convert(CGPoint, to: UIWindow?) -> CGPoint](uiwindow/convert(_:to:)-687rw.md)
  Converts a point from the current window’s coordinate system to the coordinate system of another window.
- [func convert(CGPoint, from: UIWindow?) -> CGPoint](uiwindow/convert(_:from:)-1gbm1.md)
  Converts a point from the coordinate system of a given window to the coordinate system of the current window.
- [func convert(CGRect, from: UIWindow?) -> CGRect](uiwindow/convert(_:from:)-10p2b.md)
  Converts a rectangle from the coordinate system of another window to coordinate system of the current window.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiwindow/convert(_:to:)-7k3l0)*