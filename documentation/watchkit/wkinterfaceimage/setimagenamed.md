# setImageNamed(_:)

**Framework**: WatchKit  
**Kind**: method

Sets the displayed image using a named image resource file.

**Availability**:
- watchOS 2.0+

## Declaration

```swift
func setImageNamed(_ imageName: String?)
```

#### Discussion

This method looks for an image with the specified name on Apple Watch and displays it in the image view. If the specified image cannot be found, the image view displays no image.

When setting images, always try to use images that are sized to fit the available space. Images are rendered according to the mode and size attributes you set for the image interface object.

## Parameters

- `imageName`: The name of the image to be loaded from the Watch app’s bundle. Specify the filename of the image and include the filename extension in the name. You may specify an image file that contains multiple images running as an animation. For information on how to specify an animated image, see  .

## See Also

- [func setImage(UIImage?)](setimage(_:).md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfaceimage/setimage(_:)))
  Sets the displayed image using the specified image object.
- [func setImageData(Data?)](setimagedata(_:).md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfaceimage/setimagedata(_:)))
  Sets the displayed image using a formatted data object.
- [func setTintColor(UIColor?)](settintcolor(_:).md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfaceimage/settintcolor(_:)))
  Changes the color applied to a template image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkinterfaceimage/setimagenamed(_:))*