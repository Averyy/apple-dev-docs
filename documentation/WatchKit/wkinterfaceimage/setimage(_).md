# setImage(_:)

**Framework**: WatchKit  
**Kind**: method  
**Role**: Instance Method

Sets the displayed image using the specified image object.

**Availability**:
- watchOS 2.0+

## Declaration

```swift
func setImage(_ image: UIImage?)
```

```objc
- (void) setImage:(UIImage *) image;
```

#### Discussion

This method changes the image being displayed. Use this method to assign either a static image or an animated image that you created using the [`animatedImage(with:duration:)`](../../UIKit/uiimage/animatedimage%28with,duration%29.md) method.

When setting images, always try to use images that are sized to fit the available space. Images are rendered according to the mode and size attributes you set for the image interface object.

## Parameters

- `image`: The image to be displayed. Specifying `nil` removes the existing image, causing the watch interface to display nothing in the space previously occupied by the image. You may specify a template image or an animated image sequence for this parameter.  For information on how to specify an animated image, see [Animating a Series of Images](../wkinterfaceimage.md#Animating-a-Series-of-Images).

## See Also

### Related Documentation
- [App Programming Guide for watchOS](https://developer.apple.com/library/archive/documentation/General/Conceptual/WatchKitProgrammingGuide/index.html#//apple_ref/doc/uid/TP40014969)
### Configuring the Image
- [func setImageData(Data?)](./setimagedata%28_%29.md)
  Sets the displayed image using a formatted data object.
- [func setImageNamed(String?)](./setimagenamed%28_%29.md)
  Sets the displayed image using a named image resource file.
- [func setTintColor(UIColor?)](./settintcolor%28_%29.md)
  Changes the color applied to a template image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkinterfaceimage/setimage(_:))*