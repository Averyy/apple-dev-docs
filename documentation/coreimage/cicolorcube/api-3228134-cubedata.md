# cubeData

**Framework**: Core Image  
**Kind**: intfp  
**Required**: Yes

The cube texture data to use as a color lookup table.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
var cubeData: Data { get set }
```

#### Discussion

This filter maps color values in the input image to new color values using a three-dimensional color lookup table. For each RGBA pixel in the input image, the filter uses the R, G, and B component values as indices to identify a location in the table; the RGBA value at that location becomes the RGBA value of the output pixel.

Use the [`cubeData`](cicolorcube/3228134-cubedata.md) parameter to provide data formatted for use as a color lookup table, and the inputCubeDimension parameter to specify the size of the table. This data should be an array of texel values in 32-bit floating-point RGBA linear premultiplied format. The inputCubeDimension parameter identifies the size of the cube by specifying the length of one side, so the size of the array should be [`cubeDimension`](cicolorcube/3228135-cubedimension.md) cubed times the size of a single texel value. In the color table, the R component varies fastest, followed by G, then B.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cicolorcube/3228134-cubedata)*