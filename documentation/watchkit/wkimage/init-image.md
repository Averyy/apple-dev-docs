# init(image:)

**Framework**: Watchkit  
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

- [convenience init(imageData: Data)](wkimage/init(imagedata:).md)
  Creates an image with the specified raw image data.
- [convenience init(imageName: String)](wkimage/init(imagename:).md)
  Creates an image by loading an image file from the Watch app bundle.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkimage/init(image:))*