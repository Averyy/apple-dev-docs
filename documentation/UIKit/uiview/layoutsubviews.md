# layoutSubviews()

**Framework**: UIKit  
**Kind**: method

Lays out subviews.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
@MainActor
func layoutSubviews()
```

#### Discussion

The default implementation of this method does nothing on iOS 5.1 and earlier. Otherwise, the default implementation uses any constraints you’ve set to determine the size and position of any subviews.

Subclasses can override this method as needed to perform more precise layout of their subviews. You should override this method only if the autoresizing and constraint-based behaviors of the subviews don’t offer the behavior you want. You can use your implementation to set the frame rectangles of your subviews directly.

You shouldn’t call this method directly. If you want to force a layout update, call the [`setNeedsLayout()`](uiview/setneedslayout().md) method instead to do so prior to the next drawing update. If you want to update the layout of your views immediately, call the [`layoutIfNeeded()`](uiview/layoutifneeded().md) method.

In iOS 18 and later, UIKit supports automatic trait tracking inside this method for traits from this view’s `traitCollection`. For more information, see [`Automatic trait tracking`](automatic-trait-tracking.md).

## See Also

- [func updateConstraints()](uiview/updateconstraints.md)
  Updates constraints for the view.
- [func draw(CGRect)](uiview/draw(_:).md)
  Draws the view’s image within the passed-in rectangle.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiview/layoutsubviews())*