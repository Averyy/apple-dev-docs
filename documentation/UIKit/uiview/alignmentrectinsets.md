# alignmentRectInsets

**Framework**: UIKit  
**Kind**: property

The insets from the view’s frame that define its alignment rectangle.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var alignmentRectInsets: UIEdgeInsets { get }
```

#### Discussion

The default value of this property is an [`UIEdgeInsets`](uiedgeinsets.md) structure with zero values. Custom views that draw ornamentation around their content should use this property to return insets that align with the edges of the content, excluding the ornamentation. This allows the constraint-based layout system to align views based on their content, rather than just their frame.

Custom views whose content location can’t be expressed by a simple set of insets should override [`alignmentRect(forFrame:)`](uiview/alignmentrect(forframe:).md) and [`frame(forAlignmentRect:)`](uiview/frame(foralignmentrect:).md) to describe their custom transform between alignment rectangle and frame.

## See Also

- [func alignmentRect(forFrame: CGRect) -> CGRect](uiview/alignmentrect(forframe:).md)
  Returns the view’s alignment rectangle for a given frame.
- [func frame(forAlignmentRect: CGRect) -> CGRect](uiview/frame(foralignmentrect:).md)
  Returns the view’s frame for a given alignment rectangle.
- [var forFirstBaselineLayout: UIView](uiview/forfirstbaselinelayout.md)
  Returns a view used to satisfy first baseline constraints.
- [var forLastBaselineLayout: UIView](uiview/forlastbaselinelayout.md)
  Returns a view used to satisfy last baseline constraints.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiview/alignmentrectinsets)*