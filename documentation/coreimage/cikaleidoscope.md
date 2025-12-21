# CIKaleidoscope

**Framework**: Core Image  
**Kind**: protocol

The properties you use to configure a kaleidoscope filter.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
protocol CIKaleidoscope : CIFilterProtocol
```

## Topics

### Instance Properties
- [var angle: Float](cikaleidoscope/angle.md)
  The angle of the reflection.
- [var center: CGPoint](cikaleidoscope/center.md)
  The x and y position to use as the center of the effect.
- [var count: Int](cikaleidoscope/count.md)
  The number of reflections in the pattern.
- [var inputImage: CIImage?](cikaleidoscope/inputimage.md)
  The image to use as an input image.

## Relationships

### Inherits From
- [CIFilterProtocol](cifilterprotocol.md)

## See Also

- [class func kaleidoscope() -> any CIFilter & CIKaleidoscope](cifilter-swift.class/kaleidoscope.md)
  Creates a 12-way kaleidoscopic image from an image.
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
- [protocol CITriangleKaleidoscope](citrianglekaleidoscope.md)
  The properties you use to configure a triangle kaleidoscope filter.
- [protocol CITriangleTile](citriangletile.md)
  The properties you use to configure a triangle tile filter.
- [protocol CITwelvefoldReflectedTile](citwelvefoldreflectedtile.md)
  The properties you use to configure a twelvefold reflected tile filter.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cikaleidoscope)*