# setScopeBarButtonDividerImage(_:forLeftSegmentState:rightSegmentState:)

**Framework**: UIKit  
**Kind**: method

Sets the divider image to use for a given combination of left and right segment states.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func setScopeBarButtonDividerImage(_ dividerImage: UIImage?, forLeftSegmentState leftState: UIControl.State, rightSegmentState rightState: UIControl.State)
```

#### Discussion

To customize the segmented control appearance you need to provide divider images to go between two unselected segments (`leftSegmentState:UIControlStateNormal rightSegmentState:UIControlStateNormal`), selected on the left and unselected on the right (`leftSegmentState:UIControlStateSelected rightSegmentState:UIControlStateNormal`), and unselected on the left and selected on the right (`leftSegmentState:UIControlStateNormal rightSegmentState:UIControlStateSelected`).

## Parameters

- `dividerImage`: The divider image to use for the combination of   and  .
- `leftState`: The state may be   or  .
- `rightState`: The state may be   or  .

## See Also

- [var scopeBarBackgroundImage: UIImage?](uisearchbar/scopebarbackgroundimage.md)
  The background image for the scope bar.
- [func scopeBarButtonBackgroundImage(for: UIControl.State) -> UIImage?](uisearchbar/scopebarbuttonbackgroundimage(for:).md)
  Returns the background image for the scope bar button in a given state.
- [func setScopeBarButtonBackgroundImage(UIImage?, for: UIControl.State)](uisearchbar/setscopebarbuttonbackgroundimage(_:for:).md)
  Sets the background image for the scope bar button in a given state.
- [func scopeBarButtonDividerImage(forLeftSegmentState: UIControl.State, rightSegmentState: UIControl.State) -> UIImage?](uisearchbar/scopebarbuttondividerimage(forleftsegmentstate:rightsegmentstate:).md)
  Returns the divider image to use for a given combination of left and right segment states.
- [func scopeBarButtonTitleTextAttributes(for: UIControl.State) -> [NSAttributedString.Key : Any]?](uisearchbar/scopebarbuttontitletextattributes(for:).md)
  Returns the text attributes for the search bar’s button’s title string for a given state.
- [func setScopeBarButtonTitleTextAttributes([NSAttributedString.Key : Any]?, for: UIControl.State)](uisearchbar/setscopebarbuttontitletextattributes(_:for:).md)
  Sets the text attributes for the search bar’ button’s title string for a given state.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uisearchbar/setscopebarbuttondividerimage(_:forleftsegmentstate:rightsegmentstate:))*