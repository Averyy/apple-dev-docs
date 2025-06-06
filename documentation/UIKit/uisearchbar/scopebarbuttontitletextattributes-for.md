# scopeBarButtonTitleTextAttributes(for:)

**Framework**: UIKit  
**Kind**: method

Returns the text attributes for the search bar’s button’s title string for a given state.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func scopeBarButtonTitleTextAttributes(for state: UIControl.State) -> [NSAttributedString.Key : Any]?
```

#### Return Value

The text attributes for the search bar’ button’s title string for `state`.

The attributes may specify the font, text color, text shadow color, and text shadow offset, using the keys found in NSString UIKit Additions Reference.

## Parameters

- `state`: A control state.

## See Also

- [var scopeBarBackgroundImage: UIImage?](uisearchbar/scopebarbackgroundimage.md)
  The background image for the scope bar.
- [func scopeBarButtonBackgroundImage(for: UIControl.State) -> UIImage?](uisearchbar/scopebarbuttonbackgroundimage(for:).md)
  Returns the background image for the scope bar button in a given state.
- [func setScopeBarButtonBackgroundImage(UIImage?, for: UIControl.State)](uisearchbar/setscopebarbuttonbackgroundimage(_:for:).md)
  Sets the background image for the scope bar button in a given state.
- [func scopeBarButtonDividerImage(forLeftSegmentState: UIControl.State, rightSegmentState: UIControl.State) -> UIImage?](uisearchbar/scopebarbuttondividerimage(forleftsegmentstate:rightsegmentstate:).md)
  Returns the divider image to use for a given combination of left and right segment states.
- [func setScopeBarButtonDividerImage(UIImage?, forLeftSegmentState: UIControl.State, rightSegmentState: UIControl.State)](uisearchbar/setscopebarbuttondividerimage(_:forleftsegmentstate:rightsegmentstate:).md)
  Sets the divider image to use for a given combination of left and right segment states.
- [func setScopeBarButtonTitleTextAttributes([NSAttributedString.Key : Any]?, for: UIControl.State)](uisearchbar/setscopebarbuttontitletextattributes(_:for:).md)
  Sets the text attributes for the search bar’ button’s title string for a given state.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uisearchbar/scopebarbuttontitletextattributes(for:))*