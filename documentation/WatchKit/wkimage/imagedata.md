# imageData

**Framework**: WatchKit  
**Kind**: property  
**Role**: Instance Property

The data object containing the raw image data.

**Availability**:
- watchOS 2.0+

## Declaration

```swift
var imageData: Data? { get }
```

```objc
@property (readonly, nullable) NSData * imageData;
```

#### Discussion

The value in this property is set using the [`init(imageData:)`](./init%28imagedata%29.md) method. For image objects created using other methods, this property is `nil`.

## See Also

### Getting the Image Data
- [var image: UIImage?](./image.md)
  The UIKit image object
- [var imageName: String?](./imagename.md)
  The name of the image to load from the Watch app’s bundle.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkimage/imagedata)*