# image

**Framework**: WatchKit  
**Kind**: property

The UIKit image object

**Availability**:
- watchOS 2.0+

## Declaration

```swift
var image: UIImage? { get }
```

#### Discussion

The value in this property is set using the [`init(image:)`](https://developer.apple.com/documentation/watchkit/wkimage/init(image:)) method. For image objects created using other methods, this property is `nil`.

## See Also

- [var imageData: Data?](imagedata.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkimage/imagedata))
  The data object containing the raw image data.
- [var imageName: String?](imagename.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkimage/imagename))
  The name of the image to load from the Watch app’s bundle.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkimage/image)*