# systemLayoutSizeFitting(_:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Returns the optimal size of the view based on its current constraints.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
func systemLayoutSizeFitting(_ targetSize: CGSize) -> CGSize
```

```objc
- (CGSize) systemLayoutSizeFittingSize:(CGSize) targetSize;
```

#### Return Value

The optimal size for the view.

#### Discussion

This method returns a size value for the view that optimally satisfies the view’s current constraints and is as close to the value in the `targetSize` parameter as possible. This method does not actually change the size of the view.

## Parameters

- `targetSize`: The size that you prefer for the view. To obtain a view that is as small as possible, specify the constant [`layoutFittingCompressedSize`](./layoutfittingcompressedsize.md). To obtain a view that is as large as possible, specify the constant [`layoutFittingExpandedSize`](./layoutfittingexpandedsize.md).

## See Also

### Measuring in Auto Layout
- [func systemLayoutSizeFitting(CGSize, withHorizontalFittingPriority: UILayoutPriority, verticalFittingPriority: UILayoutPriority) -> CGSize](./systemlayoutsizefitting%28_,withhorizontalfittingpriority,verticalfittingpriority%29.md)
  Returns the optimal size of the view based on its constraints and the specified fitting priorities.
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

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiview/systemlayoutsizefitting(_:))*