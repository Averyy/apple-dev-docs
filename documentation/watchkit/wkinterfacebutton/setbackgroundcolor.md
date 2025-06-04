# setBackgroundColor(_:)

**Framework**: WatchKit  
**Kind**: method

Sets the background color of the button.

**Availability**:
- watchOS 2.0+

## Declaration

```swift
func setBackgroundColor(_ color: UIColor?)
```

#### Discussion

If you specify both a background color and a full-color background image, only the image is displayed. If the image is a template image instead, the button tints the image using the background color.

## Parameters

- `color`: The fill color to use for the button’s background.

## See Also

- [func setBackgroundImage(UIImage?)](setbackgroundimage(_:).md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfacebutton/setbackgroundimage(_:)))
  Sets the button’s background image to the specified image.
- [func setBackgroundImageData(Data?)](setbackgroundimagedata(_:).md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfacebutton/setbackgroundimagedata(_:)))
  Sets the button’s background image to the image in the specified data object.
- [func setBackgroundImageNamed(String?)](setbackgroundimagenamed(_:).md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfacebutton/setbackgroundimagenamed(_:)))
  Sets the button’s background image to the image in the named resource file.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkinterfacebutton/setbackgroundcolor(_:))*