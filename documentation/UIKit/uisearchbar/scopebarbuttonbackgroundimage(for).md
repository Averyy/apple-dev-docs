# scopeBarButtonBackgroundImage(for:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Returns the background image for the scope bar button in a given state.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
func scopeBarButtonBackgroundImage(for state: UIControl.State) -> UIImage?
```

```objc
- (UIImage *) scopeBarButtonBackgroundImageForState:(UIControlState) state;
```

#### Return Value

The background image for the scope bar button in `state`.

#### Discussion

If the background image is an image returned from [`stretchableImage(withLeftCapWidth:topCapHeight:)`](../uiimage/stretchableimage%28withleftcapwidth,topcapheight%29.md) (`UIImage`), the cap widths are calculated from that information, otherwise, the cap width is calculated by subtracting one from the image’s width then dividing by 2. The cap widths are used as the margins for text placement. To adjust the margin use the margin adjustment methods.

## Parameters

- `state`: A control state.

## See Also

### Customizing the scope bar appearance
- [var scopeBarBackgroundImage: UIImage?](./scopebarbackgroundimage.md)
  The background image for the scope bar.
- [func setScopeBarButtonBackgroundImage(UIImage?, for: UIControl.State)](./setscopebarbuttonbackgroundimage%28_,for%29.md)
  Sets the background image for the scope bar button in a given state.
- [func scopeBarButtonDividerImage(forLeftSegmentState: UIControl.State, rightSegmentState: UIControl.State) -> UIImage?](./scopebarbuttondividerimage%28forleftsegmentstate,rightsegmentstate%29.md)
  Returns the divider image to use for a given combination of left and right segment states.
- [func setScopeBarButtonDividerImage(UIImage?, forLeftSegmentState: UIControl.State, rightSegmentState: UIControl.State)](./setscopebarbuttondividerimage%28_,forleftsegmentstate,rightsegmentstate%29.md)
  Sets the divider image to use for a given combination of left and right segment states.
- [func scopeBarButtonTitleTextAttributes(for: UIControl.State) -> [NSAttributedString.Key : Any]?](./scopebarbuttontitletextattributes%28for%29.md)
  Returns the text attributes for the search bar’s button’s title string for a given state.
- [func setScopeBarButtonTitleTextAttributes([NSAttributedString.Key : Any]?, for: UIControl.State)](./setscopebarbuttontitletextattributes%28_,for%29.md)
  Sets the text attributes for the search bar’ button’s title string for a given state.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uisearchbar/scopebarbuttonbackgroundimage(for:))*