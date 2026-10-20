# setScopeBarButtonBackgroundImage(_:for:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Sets the background image for the scope bar button in a given state.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
func setScopeBarButtonBackgroundImage(_ backgroundImage: UIImage?, for state: UIControl.State)
```

```objc
- (void) setScopeBarButtonBackgroundImage:(UIImage *) backgroundImage forState:(UIControlState) state;
```

#### Discussion

For more details, see [`scopeBarButtonBackgroundImage(for:)`](./scopebarbuttonbackgroundimage%28for%29.md).

## Parameters

- `backgroundImage`: The background image for the scope bar button in `state`.
- `state`: A control state.

## See Also

### Customizing the scope bar appearance
- [var scopeBarBackgroundImage: UIImage?](./scopebarbackgroundimage.md)
  The background image for the scope bar.
- [func scopeBarButtonBackgroundImage(for: UIControl.State) -> UIImage?](./scopebarbuttonbackgroundimage%28for%29.md)
  Returns the background image for the scope bar button in a given state.
- [func scopeBarButtonDividerImage(forLeftSegmentState: UIControl.State, rightSegmentState: UIControl.State) -> UIImage?](./scopebarbuttondividerimage%28forleftsegmentstate,rightsegmentstate%29.md)
  Returns the divider image to use for a given combination of left and right segment states.
- [func setScopeBarButtonDividerImage(UIImage?, forLeftSegmentState: UIControl.State, rightSegmentState: UIControl.State)](./setscopebarbuttondividerimage%28_,forleftsegmentstate,rightsegmentstate%29.md)
  Sets the divider image to use for a given combination of left and right segment states.
- [func scopeBarButtonTitleTextAttributes(for: UIControl.State) -> [NSAttributedString.Key : Any]?](./scopebarbuttontitletextattributes%28for%29.md)
  Returns the text attributes for the search bar’s button’s title string for a given state.
- [func setScopeBarButtonTitleTextAttributes([NSAttributedString.Key : Any]?, for: UIControl.State)](./setscopebarbuttontitletextattributes%28_,for%29.md)
  Sets the text attributes for the search bar’ button’s title string for a given state.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uisearchbar/setscopebarbuttonbackgroundimage(_:for:))*