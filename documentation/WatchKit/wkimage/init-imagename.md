# init(imageName:)

**Framework**: WatchKit  
**Kind**: init

Creates an image by loading an image file from the Watch app bundle.

**Availability**:
- watchOS 2.0+

## Declaration

```swift
convenience init(imageName: String)
```

#### Return Value

An initialized `WKImage` object.

#### Discussion

Use this method to specify an image by name. Only the image name is sent from your WatchKit extension to your Watch app, and the Watch app handles the loading of that image from its own bundle. If it cannot find the specified image, it displays no image.

## Parameters

- `imageName`: The name of the image to be loaded from the Watch app’s bundle. Specify the filename of the image and include the filename extension in the name. This parameter must not be  .

## See Also

- [convenience init(image: UIImage)](wkimage/init(image:).md)
  Creates and returns an image object using the specified UIKit image.
- [convenience init(imageData: Data)](wkimage/init(imagedata:).md)
  Creates an image with the specified raw image data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkimage/init(imagename:))*