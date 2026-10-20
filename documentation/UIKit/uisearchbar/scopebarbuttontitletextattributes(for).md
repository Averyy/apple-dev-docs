# scopeBarButtonTitleTextAttributes(for:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Returns the text attributes for the search bar’s button’s title string for a given state.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
func scopeBarButtonTitleTextAttributes(for state: UIControl.State) -> [NSAttributedString.Key : Any]?
```

```objc
- (NSDictionary<NSString *,id> *) scopeBarButtonTitleTextAttributesForState:(UIControlState) state;
```

#### Return Value

The text attributes for the search bar’ button’s title string for `state`.

The attributes may specify the font, text color, text shadow color, and text shadow offset, using the keys found in NSString UIKit Additions Reference.

## Parameters

- `state`: A control state.

## See Also

### Customizing the scope bar appearance
- [var scopeBarBackgroundImage: UIImage?](./scopebarbackgroundimage.md)
  The background image for the scope bar.
- [func scopeBarButtonBackgroundImage(for: UIControl.State) -> UIImage?](./scopebarbuttonbackgroundimage%28for%29.md)
  Returns the background image for the scope bar button in a given state.
- [func setScopeBarButtonBackgroundImage(UIImage?, for: UIControl.State)](./setscopebarbuttonbackgroundimage%28_,for%29.md)
  Sets the background image for the scope bar button in a given state.
- [func scopeBarButtonDividerImage(forLeftSegmentState: UIControl.State, rightSegmentState: UIControl.State) -> UIImage?](./scopebarbuttondividerimage%28forleftsegmentstate,rightsegmentstate%29.md)
  Returns the divider image to use for a given combination of left and right segment states.
- [func setScopeBarButtonDividerImage(UIImage?, forLeftSegmentState: UIControl.State, rightSegmentState: UIControl.State)](./setscopebarbuttondividerimage%28_,forleftsegmentstate,rightsegmentstate%29.md)
  Sets the divider image to use for a given combination of left and right segment states.
- [func setScopeBarButtonTitleTextAttributes([NSAttributedString.Key : Any]?, for: UIControl.State)](./setscopebarbuttontitletextattributes%28_,for%29.md)
  Sets the text attributes for the search bar’ button’s title string for a given state.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uisearchbar/scopebarbuttontitletextattributes(for:))*