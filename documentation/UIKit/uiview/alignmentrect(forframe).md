# alignmentRect(forFrame:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Returns the view’s alignment rectangle for a given frame.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
func alignmentRect(forFrame frame: CGRect) -> CGRect
```

```objc
- (CGRect) alignmentRectForFrame:(CGRect) frame;
```

## Return Value

The alignment rectangle for the specified frame.

## Discussion

The constraint-based layout system uses alignment rectangles to align views, rather than their frame. This allows custom views to be aligned based on the location of their content while still having a frame that encompasses any ornamentation they need to draw around their content, such as shadows or reflections.

The default implementation returns the view’s frame modified by the view’s [`alignmentRectInsets`](./alignmentrectinsets.md). Most custom views can use  [`alignmentRectInsets`](./alignmentrectinsets.md) to specify the location of their content within their frame. Custom views that require arbitrary transformations can override [`alignmentRect(forFrame:)`](./alignmentrect%28forframe%29.md) and [`frame(forAlignmentRect:)`](./frame%28foralignmentrect%29.md) to describe the location of their content. These two methods must always be inverses of each other.

## Parameters

- `frame`: The frame whose corresponding alignment rectangle is desired.

## See Also

### Aligning views in Auto Layout
- [func frame(forAlignmentRect: CGRect) -> CGRect](./frame%28foralignmentrect%29.md)
  Returns the view’s frame for a given alignment rectangle.
- [var alignmentRectInsets: UIEdgeInsets](./alignmentrectinsets.md)
  The insets from the view’s frame that define its alignment rectangle.
- [var forFirstBaselineLayout: UIView](./forfirstbaselinelayout.md)
  Returns a view used to satisfy first baseline constraints.
- [var forLastBaselineLayout: UIView](./forlastbaselinelayout.md)
  Returns a view used to satisfy last baseline constraints.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiview/alignmentrect(forframe:))*