# setBackgroundImageData(_:)

**Framework**: WatchKit  
**Kind**: method

Sets the button’s background image to the image in the specified data object.

**Availability**:
- watchOS 2.0+

## Declaration

```swift
func setBackgroundImageData(_ imageData: Data?)
```

#### Discussion

Use this method when you already have image data in the raw PNG or JPG format. This method sends the data as-is, which lets you send the data in a compressed format. Sending compressed data is often more efficient than sending a [`UIImage`](https://developer.apple.com/documentation/UIKit/UIImage) object.

## Parameters

- `imageData`: A data object containing the image data in its native format. The image is displayed behind the button’s title text. Specifying   removes the existing image. You may specify image data that contains multiple images running as an animation. The image is scaled as needed to fill the button’s content area.

## See Also

- [func setBackgroundColor(UIColor?)](setbackgroundcolor(_:).md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfacebutton/setbackgroundcolor(_:)))
  Sets the background color of the button.
- [func setBackgroundImage(UIImage?)](setbackgroundimage(_:).md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfacebutton/setbackgroundimage(_:)))
  Sets the button’s background image to the specified image.
- [func setBackgroundImageNamed(String?)](setbackgroundimagenamed(_:).md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfacebutton/setbackgroundimagenamed(_:)))
  Sets the button’s background image to the image in the named resource file.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkinterfacebutton/setbackgroundimagedata(_:))*