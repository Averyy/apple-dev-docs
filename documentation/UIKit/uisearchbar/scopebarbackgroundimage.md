# scopeBarBackgroundImage

**Framework**: UIKit  
**Kind**: property

The background image for the scope bar.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var scopeBarBackgroundImage: UIImage? { get set }
```

#### Discussion

Images that are 1 point wide or stretchable images are stretched, otherwise the image is tiled.

## See Also

- [var backgroundImage: UIImage?](uisearchbar/backgroundimage.md)
  The background image for the search bar.
- [func scopeBarButtonBackgroundImage(for: UIControl.State) -> UIImage?](uisearchbar/scopebarbuttonbackgroundimage(for:).md)
  Returns the background image for the scope bar button in a given state.
- [func setScopeBarButtonBackgroundImage(UIImage?, for: UIControl.State)](uisearchbar/setscopebarbuttonbackgroundimage(_:for:).md)
  Sets the background image for the scope bar button in a given state.
- [func scopeBarButtonDividerImage(forLeftSegmentState: UIControl.State, rightSegmentState: UIControl.State) -> UIImage?](uisearchbar/scopebarbuttondividerimage(forleftsegmentstate:rightsegmentstate:).md)
  Returns the divider image to use for a given combination of left and right segment states.
- [func setScopeBarButtonDividerImage(UIImage?, forLeftSegmentState: UIControl.State, rightSegmentState: UIControl.State)](uisearchbar/setscopebarbuttondividerimage(_:forleftsegmentstate:rightsegmentstate:).md)
  Sets the divider image to use for a given combination of left and right segment states.
- [func scopeBarButtonTitleTextAttributes(for: UIControl.State) -> [NSAttributedString.Key : Any]?](uisearchbar/scopebarbuttontitletextattributes(for:).md)
  Returns the text attributes for the search bar’s button’s title string for a given state.
- [func setScopeBarButtonTitleTextAttributes([NSAttributedString.Key : Any]?, for: UIControl.State)](uisearchbar/setscopebarbuttontitletextattributes(_:for:).md)
  Sets the text attributes for the search bar’ button’s title string for a given state.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uisearchbar/scopebarbackgroundimage)*