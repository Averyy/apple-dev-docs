# affineClamp()

**Framework**: Core Image  
**Kind**: method

Performs a transform on the image and extends the image edges to infinity.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
class func affineClamp() -> any CIFilter & CIAffineClamp
```

#### Return Value

The tiled image.

#### Discussion

This method applies the affine clamp filter to an image. This effect performs similarly to the affine transform filter except that it produces an infinite image. You can use this filter when you need to blur an image but you want to avoid a soft, black fringe along the edges.

The affine clamp filter uses the following properties:

The following code creates a filter that produces a cropped image with colored edges to fill the rest of the image:

```swift
func affineClamp(inputImage: CIImage) -> CIImage {
    let affineClamp = CIFilter.affineClamp()
    affineClamp.inputImage = inputImage
    affineClamp.transform = CGAffineTransform(a: 1.0, b: 0.0, c: 0.0, d: 1.0, tx: 0.0, ty: 0.0)
    return affineClamp.outputImage!
}
```

![Two photographs of a bouquet of multiple colorful flowers. The photo on the left is up close with good lighting and focus. In the photo on the right, an affine clamp filter is applied, resulting in the edges of the image colors stretching to the edge of the photo.](https://docs-assets.developer.apple.com/published/03ddcecfe2c0da965c6781a0b50c97f7/media-3624745%402x.png)

## See Also

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
- [class func opTile() -> any CIFilter & CIOpTile](cifilter-swift.class/optile.md)
  Produces an effect that mimics a style of visual art that uses optical illusions.
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

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cifilter-swift.class/affineclamp())*