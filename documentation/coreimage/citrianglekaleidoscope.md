# CITriangleKaleidoscope

**Framework**: Core Image  
**Kind**: protocol

The properties you use to configure a triangle kaleidoscope filter.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
protocol CITriangleKaleidoscope : CIFilterProtocol
```

## Topics

### Instance Properties
- [var decay: Float](citrianglekaleidoscope/decay.md)
  A value that determines how fast the color fades from the center triangle.
- [var inputImage: CIImage?](citrianglekaleidoscope/inputimage.md)
  The image to use as an input image.
- [var point: CGPoint](citrianglekaleidoscope/point.md)
  The x and y position to use as the center of the triangular area in the input image.
- [var rotation: Float](citrianglekaleidoscope/rotation.md)
  The rotation angle of the triangle.
- [var size: Float](citrianglekaleidoscope/size.md)
  The size, in pixels, of the triangle.

## Relationships

### Inherits From
- [CIFilterProtocol](cifilterprotocol.md)

## See Also

- [class func triangleKaleidoscope() -> any CIFilter & CITriangleKaleidoscope](cifilter-swift.class/trianglekaleidoscope.md)
  Create a triangular kaleidoscope effect and then tiles the result.
- [protocol CIAffineClamp](ciaffineclamp.md)
  The properties you use to configure an affine clamp filter.
- [protocol CIAffineTile](ciaffinetile.md)
  The properties you use to configure an affine tile filter.
- [protocol CIEightfoldReflectedTile](cieightfoldreflectedtile.md)
  The properties you use to configure an eightfold reflected tile filter.
- [protocol CIFourfoldReflectedTile](cifourfoldreflectedtile.md)
  The properties you use to configure a fourfold reflected tile filter.
- [protocol CIFourfoldRotatedTile](cifourfoldrotatedtile.md)
  The properties you use to configure a fourfold rotated tile filter.
- [protocol CIFourfoldTranslatedTile](cifourfoldtranslatedtile.md)
  The properties you use to configure a fourfold translated tile filter.
- [protocol CIGlideReflectedTile](ciglidereflectedtile.md)
  The properties you use to configure a glide reflected tile filter.
- [protocol CIKaleidoscope](cikaleidoscope.md)
  The properties you use to configure a kaleidoscope filter.
- [protocol CIOpTile](cioptile.md)
  The properties you use to configure an optical tile filter.
- [protocol CIParallelogramTile](ciparallelogramtile.md)
  The properties you use to configure a parallelogram tile filter.
- [protocol CIPerspectiveTile](ciperspectivetile.md)
  The properties you use to configure a perspective tile filter.
- [protocol CISixfoldReflectedTile](cisixfoldreflectedtile.md)
  The properties you use to configure a sixfold reflected tile filter.
- [protocol CISixfoldRotatedTile](cisixfoldrotatedtile.md)
  The properties you use to configure a sixfold rotated tile filter.
- [protocol CITriangleTile](citriangletile.md)
  The properties you use to configure a triangle tile filter.
- [protocol CITwelvefoldReflectedTile](citwelvefoldreflectedtile.md)
  The properties you use to configure a twelvefold reflected tile filter.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/citrianglekaleidoscope)*