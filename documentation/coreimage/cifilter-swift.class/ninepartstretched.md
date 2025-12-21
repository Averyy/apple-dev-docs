# ninePartStretched()

**Framework**: Core Image  
**Kind**: method

Distorts an image by stretching it between two breakpoints.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
class func ninePartStretched() -> any CIFilter & CINinePartStretched
```

#### Return Value

The distorted image.

#### Discussion

This method applies the nine-part stretched filter to an image. This effect distorts an image by stretching an image to the breakpoint properties while distorting the image based on the grow amount.

The nine-part stretched filter uses the following properties:

The following code creates a filter that results in a significantly warped image:

```swift
func ninePartStretch(inputImage: CIImage) -> CIImage {
    let filter = CIFilter.ninePartStretched()
    filter.inputImage = inputImage
    filter.setDefaults()
    filter.breakpoint0 = CGPoint(x: 200, y: 200)
    filter.breakpoint1 = CGPoint(x: inputImage.extent.size.width-200, y: inputImage.extent.size.height - 200)
    filter.growAmount = CGPoint(x: 500, y: 500)
    return filter.outputImage!
}
```

![Two images arranged horizontally. The left image contains a photograph of three hydrangea flowers with dark leaves in the background. An area inset by 200 pixels from all sides is highlighted using a rectangle. The image on the right shows the result of applying the nine part stretched filter. The area within the red rectangle has been stretched making the image larger. The areas outside of the rectangle have been warped to match the stretched area.](https://docs-assets.developer.apple.com/published/1c46d64e7f107e3d4cadd6f729e972b0/media-4407340%402x.png)

## See Also

- [class func bumpDistortion() -> any CIFilter & CIBumpDistortion](cifilter-swift.class/bumpdistortion.md)
  Distorts an image with a concave or convex bump.
- [class func bumpDistortionLinear() -> any CIFilter & CIBumpDistortionLinear](cifilter-swift.class/bumpdistortionlinear.md)
  Linearly distorts an image with a concave or convex bump.
- [class func circleSplashDistortion() -> any CIFilter & CICircleSplashDistortion](cifilter-swift.class/circlesplashdistortion.md)
  Distorts an image with radiating circles to the periphery of the image.
- [class func circularWrap() -> any CIFilter & CICircularWrap](cifilter-swift.class/circularwrap.md)
  Distorts an image by increasing the distance of the center of the image.
- [class func displacementDistortion() -> any CIFilter & CIDisplacementDistortion](cifilter-swift.class/displacementdistortion.md)
  Applies the grayscale values of the second image to the first image.
- [class func droste() -> any CIFilter & CIDroste](cifilter-swift.class/droste.md)
  Stylizes an image with the Droste effect.
- [class func glassDistortion() -> any CIFilter & CIGlassDistortion](cifilter-swift.class/glassdistortion.md)
  Distorts an image by applying a glass-like texture.
- [class func glassLozenge() -> any CIFilter & CIGlassLozenge](cifilter-swift.class/glasslozenge.md)
  Creates a lozenge-shaped lens and distorts the image.
- [class func holeDistortion() -> any CIFilter & CIHoleDistortion](cifilter-swift.class/holedistortion.md)
  Distorts an image with a circular area that pushes the image outward.
- [class func lightTunnel() -> any CIFilter & CILightTunnel](cifilter-swift.class/lighttunnel.md)
  Distorts an image by generating a light tunnel.
- [class func ninePartTiled() -> any CIFilter & CINinePartTiled](cifilter-swift.class/nineparttiled.md)
  Distorts an image by tiling portions of it.
- [class func pinchDistortion() -> any CIFilter & CIPinchDistortion](cifilter-swift.class/pinchdistortion.md)
  Distorts an image by creating a pinch effect with stronger distortion in the center.
- [class func stretchCrop() -> any CIFilter & CIStretchCrop](cifilter-swift.class/stretchcrop.md)
  Distorts an image by stretching or cropping to fit a specified size.
- [class func torusLensDistortion() -> any CIFilter & CITorusLensDistortion](cifilter-swift.class/toruslensdistortion.md)
  Creates a torus-shaped lens to distort the image.
- [class func twirlDistortion() -> any CIFilter & CITwirlDistortion](cifilter-swift.class/twirldistortion.md)
  Distorts an image by rotating pixels around a center point.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cifilter-swift.class/ninepartstretched())*