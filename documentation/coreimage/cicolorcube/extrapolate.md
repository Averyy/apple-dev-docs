# extrapolate

**Framework**: Core Image  
**Kind**: property  
**Required**: Yes

If true, then the filter extrapolates the color cube for any RGB component values outside the range 0.0 to 1.0.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
var extrapolate: Bool { get set }
```

## See Also

- [var cubeData: Data](cicolorcube/cubedata.md)
  The cube texture data to use as a color lookup table.
- [var cubeDimension: Float](cicolorcube/cubedimension.md)
  The length, in texels, of each side of the cube texture.
- [var inputImage: CIImage?](cicolorcube/inputimage.md)
  The image to use as an input image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cicolorcube/extrapolate)*