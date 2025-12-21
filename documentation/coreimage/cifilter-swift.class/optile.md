# opTile()

**Framework**: Core Image  
**Kind**: method

Produces an effect that mimics a style of visual art that uses optical illusions.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
class func opTile() -> any CIFilter & CIOpTile
```

#### Return Value

The tiled image.

#### Discussion

This filter extracts a tile from the image, applies any specified scaling and rotation, and then assembles the image again to give an optical illusion effect.

The optical illusion tile filter uses the following properties:

The following code creates a filter that results in a distorted image with less detail:

```swift
func op(inputImage: CIImage) -> CIImage {
    let opTile = CIFilter.opTile()
    opTile.inputImage = inputImage
    opTile.center = CGPoint(x: 150, y: 150)
    opTile.scale = 2.80
    opTile.angle = 0
    opTile.width = 65
    return opTile.outputImage!
}
```

![Two photographs. The one on the left is of a bouquet of colorful flowers up close with good lighting and focus. In the photo on the right, an op tile filter is applied, resulting in the image becoming a set of square tiles that contain slightly different portions of the image to create the illusion of movement.](https://docs-assets.developer.apple.com/published/ae9c49b06b4997d465af3c19b875ba8b/media-3599881%402x.png)

## See Also

- [class func affineClamp() -> any CIFilter & CIAffineClamp](cifilter-swift.class/affineclamp.md)
  Performs a transform on the image and extends the image edges to infinity.
- [class func affineTile() -> any CIFilter & CIAffineTile](cifilter-swift.class/affinetile.md)
  Performs a transform on the image and tiles the result.
- [class func eightfoldReflectedTile() -> any CIFilter & CIEightfoldReflectedTile](cifilter-swift.class/eightfoldreflectedtile.md)
  Creates an eight-way reflected pattern.
- [class func fourfoldReflectedTile() -> any CIFilter & CIFourfoldReflectedTile](cifilter-swift.class/fourfoldreflectedtile.md)
  Creates a four-way reflected pattern.
- [class func fourfoldRotatedTile() -> any CIFilter & CIFourfoldRotatedTile](cifilter-swift.class/fourfoldrotatedtile.md)
  Creates a tiled image by rotating a tile in increments of 90 degrees.
- [class func fourfoldTranslatedTile() -> any CIFilter & CIFourfoldTranslatedTile](cifilter-swift.class/fourfoldtranslatedtile.md)
  Creates a tiled image by applying four translation operations.
- [class func glideReflectedTile() -> any CIFilter & CIGlideReflectedTile](cifilter-swift.class/glidereflectedtile.md)
  Tiles an image by rotating and reflecting a tile from the image.
- [class func kaleidoscope() -> any CIFilter & CIKaleidoscope](cifilter-swift.class/kaleidoscope.md)
  Creates a 12-way kaleidoscopic image from an image.
- [class func parallelogramTile() -> any CIFilter & CIParallelogramTile](cifilter-swift.class/parallelogramtile.md)
  Warps the image to create a parallelogram and tiles the result.
- [class func perspectiveTile() -> any CIFilter & CIPerspectiveTile](cifilter-swift.class/perspectivetile.md)
  Tiles an image by adjusting the perspective of the image.
- [class func sixfoldReflectedTile() -> any CIFilter & CISixfoldReflectedTile](cifilter-swift.class/sixfoldreflectedtile.md)
  Produces a tiled image from a source image by applying a six-way reflected symmetry.
- [class func sixfoldRotatedTile() -> any CIFilter & CISixfoldRotatedTile](cifilter-swift.class/sixfoldrotatedtile.md)
  Creates a tiled image by rotating in increments of 60 degrees.
- [class func triangleKaleidoscope() -> any CIFilter & CITriangleKaleidoscope](cifilter-swift.class/trianglekaleidoscope.md)
  Create a triangular kaleidoscope effect and then tiles the result.
- [class func triangleTile() -> any CIFilter & CITriangleTile](cifilter-swift.class/triangletile.md)
  Tiles a triangular area of an image.
- [class func twelvefoldReflectedTile() -> any CIFilter & CITwelvefoldReflectedTile](cifilter-swift.class/twelvefoldreflectedtile.md)
  Creates a tiled image by rotating in increments of 30 degrees.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cifilter-swift.class/optile())*