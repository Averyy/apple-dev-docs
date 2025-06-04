# init(imageData:)

**Framework**: WatchKit  
**Kind**: init

Creates an image with the specified raw image data.

**Availability**:
- watchOS 2.0+

## Declaration

```swift
convenience init(imageData: Data)
```

#### Return Value

An initialized `WKImage` object.

#### Discussion

Use this method when you already have raw PNG or JPG data and want to use it for an image. Using this method for raw image data is more efficient than creating an image object to encapsulate that data.

## Parameters

- `imageData`: A data object containing the image data in its native format. This parameter must not be  .

## See Also

- [convenience init(image: UIImage)](init(image:).md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkimage/init(image:)))
  Creates and returns an image object using the specified UIKit image.
- [convenience init(imageName: String)](init(imagename:).md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkimage/init(imagename:)))
  Creates an image by loading an image file from the Watch app bundle.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkimage/init(imagedata:))*