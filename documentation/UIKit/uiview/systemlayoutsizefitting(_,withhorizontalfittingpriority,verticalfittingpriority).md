# systemLayoutSizeFitting(_:withHorizontalFittingPriority:verticalFittingPriority:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Returns the optimal size of the view based on its constraints and the specified fitting priorities.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
func systemLayoutSizeFitting(_ targetSize: CGSize, withHorizontalFittingPriority horizontalFittingPriority: UILayoutPriority, verticalFittingPriority: UILayoutPriority) -> CGSize
```

```objc
- (CGSize) systemLayoutSizeFittingSize:(CGSize) targetSize withHorizontalFittingPriority:(UILayoutPriority) horizontalFittingPriority verticalFittingPriority:(UILayoutPriority) verticalFittingPriority;
```

## Return Value

The optimal size for the view based on the provided constraint priorities.

## Discussion

Use this method when you want to prioritize the view’s constraints when determining the best possible size of the view.  This method does not actually change the size of the view.

## Parameters

- `targetSize`: The size that you prefer for the view. To obtain a view that is as small as possible, specify the constant [`layoutFittingCompressedSize`](./layoutfittingcompressedsize.md). To obtain a view that is as large as possible, specify the constant [`layoutFittingExpandedSize`](./layoutfittingexpandedsize.md).
- `horizontalFittingPriority`: The priority for horizontal constraints. Specify [`fittingSizeLevel`](../uilayoutpriority/fittingsizelevel.md) to get a width that is as close as possible to the width value of `targetSize`.
- `verticalFittingPriority`: The priority for vertical constraints. Specify [`fittingSizeLevel`](../uilayoutpriority/fittingsizelevel.md) to get a height that is as close as possible to the height value of `targetSize`.

## See Also

### Measuring in Auto Layout
- [func systemLayoutSizeFitting(CGSize) -> CGSize](./systemlayoutsizefitting%28_%29.md)
  Returns the optimal size of the view based on its current constraints.
- [var intrinsicContentSize: CGSize](./intrinsiccontentsize.md)
  The natural size for the receiving view, considering only properties of the view itself.
- [func invalidateIntrinsicContentSize()](./invalidateintrinsiccontentsize%28%29.md)
  Invalidates the view’s intrinsic content size.
- [func contentCompressionResistancePriority(for: NSLayoutConstraint.Axis) -> UILayoutPriority](./contentcompressionresistancepriority%28for%29.md)
  Returns the priority with which a view resists being made smaller than its intrinsic size.
- [func setContentCompressionResistancePriority(UILayoutPriority, for: NSLayoutConstraint.Axis)](./setcontentcompressionresistancepriority%28_,for%29.md)
  Sets the priority with which a view resists being made smaller than its intrinsic size.
- [func contentHuggingPriority(for: NSLayoutConstraint.Axis) -> UILayoutPriority](./contenthuggingpriority%28for%29.md)
  Returns the priority with which a view resists being made larger than its intrinsic size.
- [func setContentHuggingPriority(UILayoutPriority, for: NSLayoutConstraint.Axis)](./setcontenthuggingpriority%28_,for%29.md)
  Sets the priority with which a view resists being made larger than its intrinsic size.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiview/systemlayoutsizefitting(_:withhorizontalfittingpriority:verticalfittingpriority:))*