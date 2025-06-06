# sizeThatFits(_:)

**Framework**: UIKit  
**Kind**: method

Asks the view to calculate and return the size that best fits the specified size.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
@MainActor
func sizeThatFits(_ size: CGSize) -> CGSize
```

#### Return Value

A new size that fits the receiver’s subviews.

#### Discussion

The default implementation of this method returns the existing size of the view. Subclasses can override this method to return a custom value based on the desired layout of any subviews. For example, a [`UISwitch`](uiswitch.md) object returns a fixed size value that represents the standard size of a switch view, and a [`UIImageView`](uiimageview.md) object returns the size of the image it is currently displaying.

This method does not resize the receiver.

## Parameters

- `size`: The size for which the view should calculate its best-fitting size.

## See Also

- [var frame: CGRect](uiview/frame.md)
  The frame rectangle, which describes the view’s location and size in its superview’s coordinate system.
- [var bounds: CGRect](uiview/bounds.md)
  The bounds rectangle, which describes the view’s location and size in its own coordinate system.
- [var contentMode: UIView.ContentMode](uiview/contentmode-swift.property.md)
  A flag used to determine how a view lays out its content when its bounds change.
- [UIView.ContentMode](uiview/contentmode-swift.enum.md)
  Options to specify how a view adjusts its content when its size changes.
- [func sizeToFit()](uiview/sizetofit.md)
  Resizes and moves the receiver view so it just encloses its subviews.
- [var autoresizesSubviews: Bool](uiview/autoresizessubviews.md)
  A Boolean value that determines whether the receiver automatically resizes its subviews when its bounds change.
- [var autoresizingMask: UIView.AutoresizingMask](uiview/autoresizingmask-swift.property.md)
  An integer bit mask that determines how the receiver resizes itself when its superview’s bounds change.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiview/sizethatfits(_:))*