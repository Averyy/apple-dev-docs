# setBackgroundImage(_:)

**Framework**: Watchkit  
**Kind**: method

Sets the button’s background image to the specified image.

**Availability**:
- watchOS 2.0+

## Declaration

```swift
func setBackgroundImage(_ image: UIImage?)
```

## Overview

If `image` is a template image, the button tints that image using the current background color. The button does not use the background color for full-color images.

## Parameters

- `image`: The image to be displayed behind the button’s title text. The image is displayed behind the button’s title text. Specifying   removes the existing image. You may specify an image object that contains multiple images running as an animation. The image is scaled as needed to fill the button’s content area.

## See Also

- [func setBackgroundColor(UIColor?)](setbackgroundcolor(_:).md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfacebutton/setbackgroundcolor(_:)))
- [func setBackgroundImageData(Data?)](setbackgroundimagedata(_:).md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfacebutton/setbackgroundimagedata(_:)))
- [func setBackgroundImageNamed(String?)](setbackgroundimagenamed(_:).md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfacebutton/setbackgroundimagenamed(_:)))


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkinterfacebutton/setbackgroundimage(_:))*