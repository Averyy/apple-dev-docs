# setTintColor(_:)

**Framework**: WatchKit  
**Kind**: method  
**Role**: Instance Method

Changes the color applied to a template image.

**Availability**:
- watchOS 2.0+

## Declaration

```swift
func setTintColor(_ tintColor: UIColor?)
```

```objc
- (void) setTintColor:(UIColor *) tintColor;
```

#### Discussion

When you display a template image, use this method to set the tint color to apply to that image. With a template image, WatchKit uses only the alpha channel of the image to define a shape. To create a template image from an existing image, call the [`withRenderingMode(_:)`](../../UIKit/uiimage/withrenderingmode%28_%29.md) method on an existing [`UIImage`](../../UIKit/uiimage.md) and specify the [`UIImage.RenderingMode.alwaysTemplate`](../../UIKit/uiimage/renderingmode-swift.enum/alwaystemplate.md) rendering mode.

An image object applies the tint color only when it contains a single template image. It does not apply the tint color to animated images or images that are not configured as template images.

## Parameters

- `tintColor`: The tint color to use for a template image. Specify `nil` to use the default tint color.

## See Also

### Configuring the Image
- [func setImage(UIImage?)](./setimage%28_%29.md)
  Sets the displayed image using the specified image object.
- [func setImageData(Data?)](./setimagedata%28_%29.md)
  Sets the displayed image using a formatted data object.
- [func setImageNamed(String?)](./setimagenamed%28_%29.md)
  Sets the displayed image using a named image resource file.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkinterfaceimage/settintcolor(_:))*