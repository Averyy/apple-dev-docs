# extent

**Framework**: Core Image  
**Kind**: instp

A rectangle that specifies the extent of the image.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- macOS 10.4+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var extent: CGRect { get }
```

#### Discussion

This rectangle specifies the extent of the image in working space coordinates.

## See Also

- [var definition: CIFilterShape](ciimage/1437804-definition.md)
  Returns a filter shape object that represents the domain of definition of the image.
- [var properties: [String : Any]](ciimage/1437733-properties.md)
  A dictionary containing metadata about the image.
- [var url: URL?](ciimage/1438195-url.md)
  The URL from which the image was loaded.
- [var colorSpace: CGColorSpace?](ciimage/1437750-colorspace.md)
  The color space of the image.
- [func orientationTransform(forExifOrientation: Int32) -> CGAffineTransform](ciimage/1437930-orientationtransform.md)
  Returns the transformation needed to reorient the image to the specified orientation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/ciimage/1437996-extent)*