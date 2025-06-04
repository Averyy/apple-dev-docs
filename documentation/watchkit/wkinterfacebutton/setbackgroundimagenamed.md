# setBackgroundImageNamed(_:)

**Framework**: WatchKit  
**Kind**: method

Sets the button’s background image to the image in the named resource file.

**Availability**:
- watchOS 2.0+

## Declaration

```swift
func setBackgroundImageNamed(_ imageName: String?)
```

#### Discussion

This method looks for an image with the specified name in the Watch app’s bundle and uses it as the background image for the button. (In watchOS 1, the button also searches the image cache for an image with the specified name.) If the specified image cannot be found, the button displays no background image.

When the image is a template image, the button tints that image using the current background color. The button does not use the background color for full-color images.

## Parameters

- `imageName`: The name of the image to load from the Watch app’s bundle. For images in the bundle, specify the filename of the image and include the filename extension in the name. The image is displayed behind the button’s title text. You may specify an image file that contains multiple images running as an animation. The image is scaled as needed to fill the button’s content area.

## See Also

- [func setBackgroundColor(UIColor?)](setbackgroundcolor(_:).md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfacebutton/setbackgroundcolor(_:)))
  Sets the background color of the button.
- [func setBackgroundImage(UIImage?)](setbackgroundimage(_:).md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfacebutton/setbackgroundimage(_:)))
  Sets the button’s background image to the specified image.
- [func setBackgroundImageData(Data?)](setbackgroundimagedata(_:).md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfacebutton/setbackgroundimagedata(_:)))
  Sets the button’s background image to the image in the specified data object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkinterfacebutton/setbackgroundimagenamed(_:))*