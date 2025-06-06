# perspectiveTile()

**Framework**: Core Image  
**Kind**: clm

Tiles an image by adjusting the perspective of the image.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
class func perspectiveTile() -> any CIFilter & CIPerspectiveTile
```

#### Return_value

The tiled image.

#### Discussion

This method applies the perspective tile filter to an image. The effect adjusts the perspective of the image and then tiles the result.

The perspective tile filter uses the following properties:

The following code creates a filter that tiles the image and adjusts the perspective to add depth:

```swift
func perspective(inputImage: CIImage) -> CIImage {
    let perspectiveTile = CIFilter.perspectiveTile()
    perspectiveTile.inputImage = inputImage
    perspectiveTile.topLeft = CGPoint(x: 118, y: 484)
    perspectiveTile.topRight = CGPoint(x: 646, y: 507)
    perspectiveTile.bottomLeft = CGPoint(x: 548, y: 140)
    perspectiveTile.bottomRight = CGPoint(x: 155, y: 153)
    return perspectiveTile.outputImage!
}
```

![Two photographs. The photo on the left is of a bouquet of colorful flowers up close with good lighting and focus. In the photo on the right, a perspective tile filter is applied, resulting in the entire image becoming tiled and distorted.](https://docs-assets.developer.apple.com/published/7980cd0b9a/rendered2x-1590519581.png)

## See Also

- [class func affineClamp() -> any CIFilter & CIAffineClamp](cifilter/3228265-affineclamp.md)
  Performs a transform on the image and extends the image edges to infinity.
- [class func affineTile() -> any CIFilter & CIAffineTile](cifilter/3228266-affinetile.md)
  Performs a transform on the image and tiles the result.
- [class func eightfoldReflectedTile() -> any CIFilter & CIEightfoldReflectedTile](cifilter/3228322-eightfoldreflectedtile.md)
  Creates an eight-way reflected pattern.
- [class func fourfoldReflectedTile() -> any CIFilter & CIFourfoldReflectedTile](cifilter/3228327-fourfoldreflectedtile.md)
  Creates a four-way reflected pattern.
- [class func fourfoldRotatedTile() -> any CIFilter & CIFourfoldRotatedTile](cifilter/3228328-fourfoldrotatedtile.md)
  Creates a tiled image by rotating a tile in increments of 90 degrees.
- [class func fourfoldTranslatedTile() -> any CIFilter & CIFourfoldTranslatedTile](cifilter/3228329-fourfoldtranslatedtile.md)
  Creates a tiled image by applying four translation operations.
- [class func glideReflectedTile() -> any CIFilter & CIGlideReflectedTile](cifilter/3228333-glidereflectedtile.md)
  Tiles an image by rotating and reflecting a tile from the image.
- [class func kaleidoscope() -> any CIFilter & CIKaleidoscope](cifilter/3228343-kaleidoscope.md)
  Creates a 12-way kaleidoscopic image from an image.
- [class func opTile() -> any CIFilter & CIOpTile](cifilter/3228373-optile.md)
  Produces an effect that mimics a style of visual art that uses optical illusions.
- [class func parallelogramTile() -> any CIFilter & CIParallelogramTile](cifilter/3228379-parallelogramtile.md)
  Warps the image to create a parallelogram and tiles the result.
- [class func sixfoldReflectedTile() -> any CIFilter & CISixfoldReflectedTile](cifilter/3228405-sixfoldreflectedtile.md)
  Produces a tiled image from a source image by applying a six-way reflected symmetry.
- [class func sixfoldRotatedTile() -> any CIFilter & CISixfoldRotatedTile](cifilter/3228406-sixfoldrotatedtile.md)
  Creates a tiled image by rotating in increments of 60 degrees.
- [class func triangleKaleidoscope() -> any CIFilter & CITriangleKaleidoscope](cifilter/3228425-trianglekaleidoscope.md)
  Create a triangular kaleidoscope effect and then tiles the result.
- [class func triangleTile() -> any CIFilter & CITriangleTile](cifilter/3228426-triangletile.md)
  Tiles a triangular area of an image.
- [class func twelvefoldReflectedTile() -> any CIFilter & CITwelvefoldReflectedTile](cifilter/3228427-twelvefoldreflectedtile.md)
  Creates a tiled image by rotating in increments of 30 degrees. 


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cifilter/3228381-perspectivetile)*