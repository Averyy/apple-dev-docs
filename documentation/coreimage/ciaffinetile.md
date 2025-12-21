# CIAffineTile

**Framework**: Core Image  
**Kind**: protocol

The properties you use to configure an affine tile filter.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
protocol CIAffineTile : CIFilterProtocol
```

## Topics

### Instance Properties
- [var inputImage: CIImage?](ciaffinetile/inputimage.md)
  The image to use as an input image.
- [var transform: CGAffineTransform](ciaffinetile/transform.md)
  The transform to apply to the image.

## Relationships

### Inherits From
- [CIFilterProtocol](cifilterprotocol.md)

## See Also

- [class func affineTile() -> any CIFilter & CIAffineTile](cifilter-swift.class/affinetile.md)
  Performs a transform on the image and tiles the result.
- [protocol CIAffineClamp](ciaffineclamp.md)
  The properties you use to configure an affine clamp filter.
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
- [protocol CITriangleKaleidoscope](citrianglekaleidoscope.md)
  The properties you use to configure a triangle kaleidoscope filter.
- [protocol CITriangleTile](citriangletile.md)
  The properties you use to configure a triangle tile filter.
- [protocol CITwelvefoldReflectedTile](citwelvefoldreflectedtile.md)
  The properties you use to configure a twelvefold reflected tile filter.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/ciaffinetile)*