# setBackgroundImageData(_:)

**Framework**: Watchkit  
**Kind**: method

Changes the background image of the group container to the image in the specified data object.

**Availability**:
- watchOS 2.0+

## Declaration

```swift
func setBackgroundImageData(_ imageData: Data?)
```

## Overview

Use this method when you already have image data in the raw PNG or JPG format. This method sends the data as-is, which lets you send the data in a compressed format. Sending compressed data is often more efficient than sending a [`UIImage`](https://developer.apple.com/documentation/UIKit/UIImage) object.

## Parameters

- `imageData`: A data object containing the image data in its native format. Specifying   removes the existing image, causing the watch interface to display nothing in the space previously occupied by the image.

## See Also

- [func setBackgroundColor(UIColor?)](setbackgroundcolor(_:).md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfacegroup/setbackgroundcolor(_:)))
- [func setBackgroundImage(UIImage?)](setbackgroundimage(_:).md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfacegroup/setbackgroundimage(_:)))
- [func setBackgroundImageNamed(String?)](setbackgroundimagenamed(_:).md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfacegroup/setbackgroundimagenamed(_:)))


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkinterfacegroup/setbackgroundimagedata(_:))*