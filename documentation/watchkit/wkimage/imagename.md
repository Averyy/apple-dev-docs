# imageName

**Framework**: Watchkit  
**Kind**: property

The name of the image to load from the Watch app’s bundle.

**Availability**:
- watchOS 2.0+

## Declaration

```swift
var imageName: String? { get }
```

#### Discussion

The value in this property is set using the [`init(imageName:)`](wkimage/init(imagename:).md) method. For image objects created using other methods, this property is `nil`.

## See Also

- [var image: UIImage?](wkimage/image.md)
  The UIKit image object
- [var imageData: Data?](wkimage/imagedata.md)
  The data object containing the raw image data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkimage/imagename)*