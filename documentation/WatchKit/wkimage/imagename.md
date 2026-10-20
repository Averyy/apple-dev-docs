# imageName

**Framework**: WatchKit  
**Kind**: property  
**Role**: Instance Property

The name of the image to load from the Watch app’s bundle.

**Availability**:
- watchOS 2.0+

## Declaration

```swift
var imageName: String? { get }
```

```objc
@property (readonly, nullable) NSString * imageName;
```

#### Discussion

The value in this property is set using the [`init(imageName:)`](./init%28imagename%29.md) method. For image objects created using other methods, this property is `nil`.

## See Also

### Getting the Image Data
- [var image: UIImage?](./image.md)
  The UIKit image object
- [var imageData: Data?](./imagedata.md)
  The data object containing the raw image data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkimage/imagename)*