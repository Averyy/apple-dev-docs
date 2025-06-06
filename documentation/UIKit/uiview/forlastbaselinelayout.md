# forLastBaselineLayout

**Framework**: UIKit  
**Kind**: property

Returns a view used to satisfy last baseline constraints.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var forLastBaselineLayout: UIView { get }
```

#### Discussion

For views with multiple rows of text, the last baseline is the baseline for the bottommost row.

When you make a constraint to a view’s [`NSLayoutConstraint.Attribute.lastBaseline`](nslayoutconstraint/attribute/lastbaseline.md) attribute, Auto Layout uses the baseline of the view returned by this method. If that view does not have a baseline, Auto Layout uses the view’s bottom edge.

Override this property to return a text-based subview (for example, [`UILabel`](uilabel.md) or a nonscrolling [`UITextView`](uitextview.md)). The returned view must be a subview of the receiver. The default implementation returns the receiving view.

## See Also

- [func alignmentRect(forFrame: CGRect) -> CGRect](uiview/alignmentrect(forframe:).md)
  Returns the view’s alignment rectangle for a given frame.
- [func frame(forAlignmentRect: CGRect) -> CGRect](uiview/frame(foralignmentrect:).md)
  Returns the view’s frame for a given alignment rectangle.
- [var alignmentRectInsets: UIEdgeInsets](uiview/alignmentrectinsets.md)
  The insets from the view’s frame that define its alignment rectangle.
- [var forFirstBaselineLayout: UIView](uiview/forfirstbaselinelayout.md)
  Returns a view used to satisfy first baseline constraints.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiview/forlastbaselinelayout)*