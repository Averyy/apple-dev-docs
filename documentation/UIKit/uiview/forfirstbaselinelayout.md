# forFirstBaselineLayout

**Framework**: Uikit  
**Kind**: property

Returns a view used to satisfy first baseline constraints.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var forFirstBaselineLayout: UIView { get }
```

#### Discussion

For views with multiple rows of text, the first baseline is the baseline for the topmost row.

When you make a constraint to a view’s [`NSLayoutConstraint.Attribute.firstBaseline`](nslayoutconstraint/attribute/firstbaseline.md) attribute, Auto Layout uses the baseline of the view returned by this method. If that view does not have a baseline, Auto Layout uses the view’s top edge.

Override this property to return a text-based subview (for example, [`UILabel`](uilabel.md) or a nonscrolling [`UITextView`](uitextview.md)). The returned view must be a subview of the receiver. The default implementation returns the value contained by [`forLastBaselineLayout`](uiview/forlastbaselinelayout.md).

> **Note**:  If the same subview is appropriate for both the first and last baseline, you only need to override the [`forLastBaselineLayout`](uiview/forlastbaselinelayout.md) getter method.

## See Also

- [func alignmentRect(forFrame: CGRect) -> CGRect](uiview/alignmentrect(forframe:).md)
  Returns the view’s alignment rectangle for a given frame.
- [func frame(forAlignmentRect: CGRect) -> CGRect](uiview/frame(foralignmentrect:).md)
  Returns the view’s frame for a given alignment rectangle.
- [var alignmentRectInsets: UIEdgeInsets](uiview/alignmentrectinsets.md)
  The insets from the view’s frame that define its alignment rectangle.
- [var forLastBaselineLayout: UIView](uiview/forlastbaselinelayout.md)
  Returns a view used to satisfy last baseline constraints.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiview/forfirstbaselinelayout)*