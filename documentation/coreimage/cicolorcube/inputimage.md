# inputImage

**Framework**: Core Image  
**Kind**: property  
**Required**: Yes

The image to use as an input image.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- macOS 10.4+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
var inputImage: CIImage? { get set }
```

## See Also

- [var cubeData: Data](cicolorcube/cubedata.md)
  The cube texture data to use as a color lookup table.
- [var cubeDimension: Float](cicolorcube/cubedimension.md)
  The length, in texels, of each side of the cube texture.
- [var extrapolate: Bool](cicolorcube/extrapolate.md)
  If true, then the filter extrapolates the color cube for any RGB component values outside the range 0.0 to 1.0.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cicolorcube/inputimage)*