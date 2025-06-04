# init(image:)

**Framework**: WatchKit  
**Kind**: init

Creates and returns an image object using the specified UIKit image.

**Availability**:
- watchOS 2.0+

## Declaration

```swift
convenience init(image: UIImage)
```

#### Return Value

An initialized `WKImage` object.

#### Discussion

Use this method when you already have a UIKit image object and want to use it in your picker.

## Parameters

- `image`: The image object. This parameter must not be  .

## See Also

- [convenience init(imageData: Data)](init(imagedata:).md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkimage/init(imagedata:)))
  Creates an image with the specified raw image data.
- [convenience init(imageName: String)](init(imagename:).md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkimage/init(imagename:)))
  Creates an image by loading an image file from the Watch app bundle.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkimage/init(image:))*