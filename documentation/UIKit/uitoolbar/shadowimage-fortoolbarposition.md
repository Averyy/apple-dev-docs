# shadowImage(forToolbarPosition:)

**Framework**: UIKit  
**Kind**: method

Returns the image to use for the toolbar shadow in a given position.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func shadowImage(forToolbarPosition topOrBottom: UIBarPosition) -> UIImage?
```

#### Return Value

The image to use for the toolbar shadow in the position specified by `topOrBottom`.

#### Discussion

The default value is `nil`, which corresponds to the default shadow image being used. When non-`nil`, the return value represents the shadow that is used on the toolbar in the position specified by the `topOrBottom` parameter.

## Parameters

- `topOrBottom`: A toolbar position constant. You can use this parameter to indicate whether the shadow image returned is intended for use in a toolbar at the top or bottom of the view.

## See Also

- [func setShadowImage(UIImage?, forToolbarPosition: UIBarPosition)](uitoolbar/setshadowimage(_:fortoolbarposition:).md)
  Sets the image to use for the toolbar shadow in a given position.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitoolbar/shadowimage(fortoolbarposition:))*