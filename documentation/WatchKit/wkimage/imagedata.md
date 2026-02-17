# imageData

**Framework**: WatchKit  
**Kind**: property

The data object containing the raw image data.

**Availability**:
- watchOS 2.0+

## Declaration

```swift
var imageData: Data? { get }
```

#### Discussion

The value in this property is set using the [`init(imageData:)`](wkimage/init(imagedata:).md) method. For image objects created using other methods, this property is `nil`.

## See Also

- [var image: UIImage?](wkimage/image.md)
  The UIKit image object
- [var imageName: String?](wkimage/imagename.md)
  The name of the image to load from the Watch app’s bundle.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkimage/imagedata)*