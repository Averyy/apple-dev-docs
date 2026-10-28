# topAnchor

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

A layout anchor representing the top edge of the view’s frame.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var topAnchor: NSLayoutYAxisAnchor { get }
```

```objc
@property (nonatomic, strong, readonly) NSLayoutYAxisAnchor * topAnchor;
```

## Discussion

Use this anchor to create constraints with the view’s top edge. You can combine this anchor only with other [`NSLayoutYAxisAnchor`](../nslayoutyaxisanchor.md) anchors. For more information, see [`NSLayoutAnchor`](../nslayoutanchor.md).

## See Also

### Creating constraints using layout anchors
- [var bottomAnchor: NSLayoutYAxisAnchor](./bottomanchor.md)
  A layout anchor representing the bottom edge of the view’s frame.
- [var centerXAnchor: NSLayoutXAxisAnchor](./centerxanchor.md)
  A layout anchor representing the horizontal center of the view’s frame.
- [var centerYAnchor: NSLayoutYAxisAnchor](./centeryanchor.md)
  A layout anchor representing the vertical center of the view’s frame.
- [var firstBaselineAnchor: NSLayoutYAxisAnchor](./firstbaselineanchor.md)
  A layout anchor representing the baseline for the topmost line of text in the view.
- [var heightAnchor: NSLayoutDimension](./heightanchor.md)
  A layout anchor representing the height of the view’s frame.
- [var lastBaselineAnchor: NSLayoutYAxisAnchor](./lastbaselineanchor.md)
  A layout anchor representing the baseline for the bottommost line of text in the view.
- [var leadingAnchor: NSLayoutXAxisAnchor](./leadinganchor.md)
  A layout anchor representing the leading edge of the view’s frame.
- [var leftAnchor: NSLayoutXAxisAnchor](./leftanchor.md)
  A layout anchor representing the left edge of the view’s frame.
- [var rightAnchor: NSLayoutXAxisAnchor](./rightanchor.md)
  A layout anchor representing the right edge of the view’s frame.
- [var trailingAnchor: NSLayoutXAxisAnchor](./trailinganchor.md)
  A layout anchor representing the trailing edge of the view’s frame.
- [var widthAnchor: NSLayoutDimension](./widthanchor.md)
  A layout anchor representing the width of the view’s frame.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiview/topanchor)*