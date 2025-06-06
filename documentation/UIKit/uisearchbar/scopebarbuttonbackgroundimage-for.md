# scopeBarButtonBackgroundImage(for:)

**Framework**: UIKit  
**Kind**: method

Returns the background image for the scope bar button in a given state.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func scopeBarButtonBackgroundImage(for state: UIControl.State) -> UIImage?
```

#### Return Value

The background image for the scope bar button in `state`.

#### Discussion

If the background image is an image returned from [`stretchableImage(withLeftCapWidth:topCapHeight:)`](uiimage/stretchableimage(withleftcapwidth:topcapheight:).md) (`UIImage`), the cap widths are calculated from that information, otherwise, the cap width is calculated by subtracting one from the image’s width then dividing by 2. The cap widths are used as the margins for text placement. To adjust the margin use the margin adjustment methods.

## Parameters

- `state`: A control state.

## See Also

- [var scopeBarBackgroundImage: UIImage?](uisearchbar/scopebarbackgroundimage.md)
  The background image for the scope bar.
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

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uisearchbar/scopebarbuttonbackgroundimage(for:))*