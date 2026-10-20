# scopeBarButtonDividerImage(forLeftSegmentState:rightSegmentState:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Returns the divider image to use for a given combination of left and right segment states.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
func scopeBarButtonDividerImage(forLeftSegmentState leftState: UIControl.State, rightSegmentState rightState: UIControl.State) -> UIImage?
```

```objc
- (UIImage *) scopeBarButtonDividerImageForLeftSegmentState:(UIControlState) leftState rightSegmentState:(UIControlState) rightState;
```

#### Return Value

The divider image to use for the combination of `leftState` and `rightState`.

#### Discussion

For more details, see [`setScopeBarButtonDividerImage(_:forLeftSegmentState:rightSegmentState:)`](./setscopebarbuttondividerimage%28_,forleftsegmentstate,rightsegmentstate%29.md)

## Parameters

- `leftState`: The state of the left segment for which to provide the divider image.

  The state may be [`normal`](../uicontrol/state-swift.struct/normal.md) or [`selected`](../uicontrol/state-swift.struct/selected.md).
- `rightState`: The state of the right segment for which to provide the divider image.

  The state may be [`normal`](../uicontrol/state-swift.struct/normal.md) or [`selected`](../uicontrol/state-swift.struct/selected.md).

## See Also

### Customizing the scope bar appearance
- [var scopeBarBackgroundImage: UIImage?](./scopebarbackgroundimage.md)
  The background image for the scope bar.
- [func scopeBarButtonBackgroundImage(for: UIControl.State) -> UIImage?](./scopebarbuttonbackgroundimage%28for%29.md)
  Returns the background image for the scope bar button in a given state.
- [func setScopeBarButtonBackgroundImage(UIImage?, for: UIControl.State)](./setscopebarbuttonbackgroundimage%28_,for%29.md)
  Sets the background image for the scope bar button in a given state.
- [func setScopeBarButtonDividerImage(UIImage?, forLeftSegmentState: UIControl.State, rightSegmentState: UIControl.State)](./setscopebarbuttondividerimage%28_,forleftsegmentstate,rightsegmentstate%29.md)
  Sets the divider image to use for a given combination of left and right segment states.
- [func scopeBarButtonTitleTextAttributes(for: UIControl.State) -> [NSAttributedString.Key : Any]?](./scopebarbuttontitletextattributes%28for%29.md)
  Returns the text attributes for the search bar’s button’s title string for a given state.
- [func setScopeBarButtonTitleTextAttributes([NSAttributedString.Key : Any]?, for: UIControl.State)](./setscopebarbuttontitletextattributes%28_,for%29.md)
  Sets the text attributes for the search bar’ button’s title string for a given state.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uisearchbar/scopebarbuttondividerimage(forleftsegmentstate:rightsegmentstate:))*