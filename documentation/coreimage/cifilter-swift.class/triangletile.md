# triangleTile()

**Framework**: Core Image  
**Kind**: method

Tiles a triangular area of an image.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
class func triangleTile() -> any CIFilter & CITriangleTile
```

#### Return Value

The tiled image.

#### Discussion

This method applies the triangle tile filter to an image. The effect creates a tiled pattern from a triangular area from the input image.

The triangle tile filter uses the following properties:

The following code creates a filter that produces a triangle of the input image and tiles the result:

```swift
func triangle(inputImage: CIImage) -> CIImage {
    let triangleTile = CIFilter.triangleTile()
    triangleTile.setValue(inputImage, forKey: kCIInputImageKey)
    triangleTile.center = CGPoint(x: 2016, y: 1512)
    triangleTile.angle = 1
    triangleTile.width = 250
    return triangleTile.outputImage!
}
```

![Two photographs of a bouquet of multiple colorful flowers. The photo on the left is up close with good lighting and focus. In the photo on the right, a triangle tile filter is applied, resulting in a triangle portion of the image containing white and blue petals repeated throughout the entire image.](https://docs-assets.developer.apple.com/published/4c6b4266f6192a6dba4f4eb5fd7e0e96/media-3599891%402x.png)

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
- [class func twelvefoldReflectedTile() -> any CIFilter & CITwelvefoldReflectedTile](cifilter-swift.class/twelvefoldreflectedtile.md)
  Creates a tiled image by rotating in increments of 30 degrees.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cifilter-swift.class/triangletile())*