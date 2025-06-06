# rightAnchor

**Framework**: UIKit  
**Kind**: property

A layout anchor representing the right edge of the view’s frame.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var rightAnchor: NSLayoutXAxisAnchor { get }
```

#### Discussion

Use this anchor to create constraints with the view’s right edge. You can combine this anchor only with a subset of the [`NSLayoutXAxisAnchor`](nslayoutxaxisanchor.md) anchors. You can combine a [`UIView`](uiview.md) with another `rightAnchor`, a `leftAnchor`, or a `centerXAnchor`. For more information, see [`NSLayoutAnchor`](nslayoutanchor.md).

## See Also

- [var bottomAnchor: NSLayoutYAxisAnchor](uiview/bottomanchor.md)
  A layout anchor representing the bottom edge of the view’s frame.
- [var centerXAnchor: NSLayoutXAxisAnchor](uiview/centerxanchor.md)
  A layout anchor representing the horizontal center of the view’s frame.
- [var centerYAnchor: NSLayoutYAxisAnchor](uiview/centeryanchor.md)
  A layout anchor representing the vertical center of the view’s frame.
- [var firstBaselineAnchor: NSLayoutYAxisAnchor](uiview/firstbaselineanchor.md)
  A layout anchor representing the baseline for the topmost line of text in the view.
- [var heightAnchor: NSLayoutDimension](uiview/heightanchor.md)
  A layout anchor representing the height of the view’s frame.
- [var lastBaselineAnchor: NSLayoutYAxisAnchor](uiview/lastbaselineanchor.md)
  A layout anchor representing the baseline for the bottommost line of text in the view.
- [var leadingAnchor: NSLayoutXAxisAnchor](uiview/leadinganchor.md)
  A layout anchor representing the leading edge of the view’s frame.
- [var leftAnchor: NSLayoutXAxisAnchor](uiview/leftanchor.md)
  A layout anchor representing the left edge of the view’s frame.
- [var topAnchor: NSLayoutYAxisAnchor](uiview/topanchor.md)
  A layout anchor representing the top edge of the view’s frame.
- [var trailingAnchor: NSLayoutXAxisAnchor](uiview/trailinganchor.md)
  A layout anchor representing the trailing edge of the view’s frame.
- [var widthAnchor: NSLayoutDimension](uiview/widthanchor.md)
  A layout anchor representing the width of the view’s frame.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiview/rightanchor)*