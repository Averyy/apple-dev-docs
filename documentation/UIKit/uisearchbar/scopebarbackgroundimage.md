# scopeBarBackgroundImage

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The background image for the scope bar.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
var scopeBarBackgroundImage: UIImage? { get set }
```

```objc
@property (nonatomic, strong, nullable) UIImage * scopeBarBackgroundImage;
```

## Discussion

Images that are 1 point wide or stretchable images are stretched, otherwise the image is tiled.

## See Also

### Related Documentation
- [var backgroundImage: UIImage?](./backgroundimage.md)
  The background image for the search bar.
### Customizing the scope bar appearance
- [func scopeBarButtonBackgroundImage(for: UIControl.State) -> UIImage?](./scopebarbuttonbackgroundimage%28for%29.md)
  Returns the background image for the scope bar button in a given state.
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

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uisearchbar/scopebarbackgroundimage)*