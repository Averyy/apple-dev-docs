# definition

**Framework**: Core Image  
**Kind**: property

Returns a filter shape object that represents the domain of definition of the image.

**Availability**:
- macOS 10.4+

## Declaration

```swift
var definition: CIFilterShape { get }
```

#### Return Value

A filter shape object.

## See Also

- [var extent: CGRect](ciimage/extent.md)
  A rectangle that specifies the extent of the image.
- [var properties: [String : Any]](ciimage/properties.md)
  A dictionary containing metadata about the image.
- [var url: URL?](ciimage/url.md)
  The URL from which the image was loaded.
- [var colorSpace: CGColorSpace?](ciimage/colorspace.md)
  The color space of the image.
- [func orientationTransform(forExifOrientation: Int32) -> CGAffineTransform](ciimage/orientationtransform(forexiforientation:).md)
  Returns the transformation needed to reorient the image to the specified orientation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/ciimage/definition)*