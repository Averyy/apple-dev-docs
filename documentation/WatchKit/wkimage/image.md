# image

**Framework**: WatchKit  
**Kind**: property  
**Role**: Instance Property

The UIKit image object

**Availability**:
- watchOS 2.0+

## Declaration

```swift
var image: UIImage? { get }
```

```objc
@property (readonly, nullable) UIImage * image;
```

#### Discussion

The value in this property is set using the [`init(image:)`](./init%28image%29.md) method. For image objects created using other methods, this property is `nil`.

## See Also

### Getting the Image Data
- [var imageData: Data?](./imagedata.md)
  The data object containing the raw image data.
- [var imageName: String?](./imagename.md)
  The name of the image to load from the Watch app’s bundle.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkimage/image)*