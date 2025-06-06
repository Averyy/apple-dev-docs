# image

**Framework**: Watchkit  
**Kind**: property

The UIKit image object

**Availability**:
- watchOS 2.0+

## Declaration

```swift
var image: UIImage? { get }
```

#### Discussion

The value in this property is set using the [`init(image:)`](wkimage/init(image:).md) method. For image objects created using other methods, this property is `nil`.

## See Also

- [var imageData: Data?](wkimage/imagedata.md)
  The data object containing the raw image data.
- [var imageName: String?](wkimage/imagename.md)
  The name of the image to load from the Watch app’s bundle.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkimage/image)*