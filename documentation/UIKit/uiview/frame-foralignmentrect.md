# frame(forAlignmentRect:)

**Framework**: UIKit  
**Kind**: method

Returns the view’s frame for a given alignment rectangle.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func frame(forAlignmentRect alignmentRect: CGRect) -> CGRect
```

#### Return Value

The frame for the specified alignment rectangle

#### Discussion

The constraint-based layout system uses alignment rectangles to align views, rather than their frame. This allows custom views to be aligned based on the location of their content while still having a frame that encompasses any ornamentation they need to draw around their content, such as shadows or reflections.

The default implementation returns `alignmentRect` modified by the view’s [`alignmentRectInsets`](uiview/alignmentrectinsets.md). Most custom views can override [`alignmentRectInsets`](uiview/alignmentrectinsets.md) to specify the location of their content within their frame. Custom views that require arbitrary transformations can override [`alignmentRect(forFrame:)`](uiview/alignmentrect(forframe:).md) and [`frame(forAlignmentRect:)`](uiview/frame(foralignmentrect:).md) to describe the location of their content. These two methods must always be inverses of each other.

## Parameters

- `alignmentRect`: The alignment rectangle whose corresponding frame is desired.

## See Also

- [func alignmentRect(forFrame: CGRect) -> CGRect](uiview/alignmentrect(forframe:).md)
  Returns the view’s alignment rectangle for a given frame.
- [var alignmentRectInsets: UIEdgeInsets](uiview/alignmentrectinsets.md)
  The insets from the view’s frame that define its alignment rectangle.
- [var forFirstBaselineLayout: UIView](uiview/forfirstbaselinelayout.md)
  Returns a view used to satisfy first baseline constraints.
- [var forLastBaselineLayout: UIView](uiview/forlastbaselinelayout.md)
  Returns a view used to satisfy last baseline constraints.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiview/frame(foralignmentrect:))*