# setShadowImage(_:forToolbarPosition:)

**Framework**: UIKit  
**Kind**: method

Sets the image to use for the toolbar shadow in a given position.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func setShadowImage(_ shadowImage: UIImage?, forToolbarPosition topOrBottom: UIBarPosition)
```

#### Discussion

When the `shadowImage` parameter is `nil`, the default shadow will be used. When non-`nil`, the `shadowImage` property is a custom shadow image to show instead of the default. Using the `topOrBottom` parameter, you can set a different shadow for toolbars at the top and bottom of the view. For a custom shadow image to be shown, a custom background image must also be set with the [`setBackgroundImage(_:forToolbarPosition:barMetrics:)`](uitoolbar/setbackgroundimage(_:fortoolbarposition:barmetrics:).md) method. If the default background image is used, then the default shadow image will be used regardless of the value of the `shadowImage` parameter.

## Parameters

- `shadowImage`: The image to use for the toolbar shadow in the position specified by  .
- `topOrBottom`: A toolbar position constant. You can use this parameter to indicate whether the   is intended for a toolbar at the top or bottom of the view.

## See Also

- [func shadowImage(forToolbarPosition: UIBarPosition) -> UIImage?](uitoolbar/shadowimage(fortoolbarposition:).md)
  Returns the image to use for the toolbar shadow in a given position.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitoolbar/setshadowimage(_:fortoolbarposition:))*