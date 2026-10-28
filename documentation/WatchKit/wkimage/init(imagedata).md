# init(imageData:)

**Framework**: WatchKit  
**Kind**: init  
**Role**: Initializer

Creates an image with the specified raw image data.

**Availability**:
- watchOS 2.0+

## Declaration

```swift
convenience init(imageData: Data)
```

```objc
+ (instancetype) imageWithImageData:(NSData *) imageData;
```

## Return Value

An initialized `WKImage` object.

## Discussion

Use this method when you already have raw PNG or JPG data and want to use it for an image. Using this method for raw image data is more efficient than creating an image object to encapsulate that data.

## Parameters

- `imageData`: A data object containing the image data in its native format. This parameter must not be `nil`.

## See Also

### Creating Image Objects
- [convenience init(image: UIImage)](./init%28image%29.md)
  Creates and returns an image object using the specified UIKit image.
- [convenience init(imageName: String)](./init%28imagename%29.md)
  Creates an image by loading an image file from the Watch app bundle.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkimage/init(imagedata:))*