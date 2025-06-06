# setTintColor(_:)

**Framework**: Watchkit  
**Kind**: method

Changes the color applied to a template image.

**Availability**:
- watchOS 2.0+

## Declaration

```swift
func setTintColor(_ tintColor: UIColor?)
```

#### Discussion

When you display a template image, use this method to set the tint color to apply to that image. With a template image, WatchKit uses only the alpha channel of the image to define a shape. To create a template image from an existing image, call the [`withRenderingMode(_:)`](https://developer.apple.com/documentation/UIKit/UIImage/withRenderingMode(_:)) method on an existing [`UIImage`](https://developer.apple.com/documentation/UIKit/UIImage) and specify the [`UIImage.RenderingMode.alwaysTemplate`](https://developer.apple.com/documentation/UIKit/UIImage/RenderingMode-swift.enum/alwaysTemplate) rendering mode.

An image object applies the tint color only when it contains a single template image. It does not apply the tint color to animated images or images that are not configured as template images.

## Parameters

- `tintColor`: The tint color to use for a template image. Specify   to use the default tint color.

## See Also

- [func setImage(UIImage?)](wkinterfaceimage/setimage(_:).md)
  Sets the displayed image using the specified image object.
- [func setImageData(Data?)](wkinterfaceimage/setimagedata(_:).md)
  Sets the displayed image using a formatted data object.
- [func setImageNamed(String?)](wkinterfaceimage/setimagenamed(_:).md)
  Sets the displayed image using a named image resource file.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkinterfaceimage/settintcolor(_:))*