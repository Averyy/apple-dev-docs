# firstBaselineAnchor

**Framework**: UIKit  
**Kind**: property

A layout anchor representing the baseline for the topmost line of text in the view.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var firstBaselineAnchor: NSLayoutYAxisAnchor { get }
```

## Mentions

- [Configuring and displaying symbol images in your UI](configuring-and-displaying-symbol-images-in-your-ui.md)

#### Discussion

For views with multiple lines of text, this anchor represents the baseline of the top row of text. Use this anchor to create constraints with this baseline. You can combine this anchor only with other [`NSLayoutYAxisAnchor`](nslayoutyaxisanchor.md) anchors. For more information, see [`NSLayoutAnchor`](nslayoutanchor.md).

## See Also

- [var bottomAnchor: NSLayoutYAxisAnchor](uiview/bottomanchor.md)
  A layout anchor representing the bottom edge of the view’s frame.
- [var centerXAnchor: NSLayoutXAxisAnchor](uiview/centerxanchor.md)
  A layout anchor representing the horizontal center of the view’s frame.
- [var centerYAnchor: NSLayoutYAxisAnchor](uiview/centeryanchor.md)
  A layout anchor representing the vertical center of the view’s frame.
- [var heightAnchor: NSLayoutDimension](uiview/heightanchor.md)
  A layout anchor representing the height of the view’s frame.
- [var lastBaselineAnchor: NSLayoutYAxisAnchor](uiview/lastbaselineanchor.md)
  A layout anchor representing the baseline for the bottommost line of text in the view.
- [var leadingAnchor: NSLayoutXAxisAnchor](uiview/leadinganchor.md)
  A layout anchor representing the leading edge of the view’s frame.
- [var leftAnchor: NSLayoutXAxisAnchor](uiview/leftanchor.md)
  A layout anchor representing the left edge of the view’s frame.
- [var rightAnchor: NSLayoutXAxisAnchor](uiview/rightanchor.md)
  A layout anchor representing the right edge of the view’s frame.
- [var topAnchor: NSLayoutYAxisAnchor](uiview/topanchor.md)
  A layout anchor representing the top edge of the view’s frame.
- [var trailingAnchor: NSLayoutXAxisAnchor](uiview/trailinganchor.md)
  A layout anchor representing the trailing edge of the view’s frame.
- [var widthAnchor: NSLayoutDimension](uiview/widthanchor.md)
  A layout anchor representing the width of the view’s frame.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiview/firstbaselineanchor)*