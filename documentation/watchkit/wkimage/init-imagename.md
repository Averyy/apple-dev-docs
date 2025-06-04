# init(imageName:)

**Framework**: Watchkit  
**Kind**: init

Creates an image by loading an image file from the Watch app bundle.

**Availability**:
- watchOS 2.0+

## Declaration

```swift
convenience init(imageName: String)
```

## Overview

An initialized `WKImage` object.

## Parameters

- `imageName`: The name of the image to be loaded from the Watch app’s bundle. Specify the filename of the image and include the filename extension in the name. This parameter must not be  .

## Discussion

Use this method to specify an image by name. Only the image name is sent from your WatchKit extension to your Watch app, and the Watch app handles the loading of that image from its own bundle. If it cannot find the specified image, it displays no image.

## See Also

- [convenience init(image: UIImage)](init(image:).md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkimage/init(image:)))
- [convenience init(imageData: Data)](init(imagedata:).md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkimage/init(imagedata:)))


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkimage/init(imagename:))*