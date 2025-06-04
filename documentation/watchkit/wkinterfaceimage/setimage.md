# setImage(_:)

**Framework**: WatchKit  
**Kind**: method

Sets the displayed image using the specified image object.

**Availability**:
- watchOS 2.0+

## Declaration

```swift
func setImage(_ image: UIImage?)
```

#### Discussion

This method changes the image being displayed. Use this method to assign either a static image or an animated image that you created using the [`animatedImage(with:duration:)`](https://developer.apple.com/documentation/UIKit/UIImage/animatedImage(with:duration:)) method.

When setting images, always try to use images that are sized to fit the available space. Images are rendered according to the mode and size attributes you set for the image interface object.

## Parameters

- `image`: The image to be displayed. Specifying   removes the existing image, causing the watch interface to display nothing in the space previously occupied by the image. You may specify a template image or an animated image sequence for this parameter.  For information on how to specify an animated image, see  .

## See Also

- [App Programming Guide for watchOS](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/General/Conceptual/WatchKitProgrammingGuide/index.html#//apple_ref/doc/uid/TP40014969)
- [func setImageData(Data?)](setimagedata(_:).md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfaceimage/setimagedata(_:)))
  Sets the displayed image using a formatted data object.
- [func setImageNamed(String?)](setimagenamed(_:).md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfaceimage/setimagenamed(_:)))
  Sets the displayed image using a named image resource file.
- [func setTintColor(UIColor?)](settintcolor(_:).md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfaceimage/settintcolor(_:)))
  Changes the color applied to a template image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkinterfaceimage/setimage(_:))*