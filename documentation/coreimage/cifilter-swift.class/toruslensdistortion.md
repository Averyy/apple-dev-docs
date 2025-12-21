# torusLensDistortion()

**Framework**: Core Image  
**Kind**: method

Creates a torus-shaped lens to distort the image.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
class func torusLensDistortion() -> any CIFilter & CITorusLensDistortion
```

#### Return Value

The distorted image.

#### Discussion

This method applies the torus lens distortion filter to an image. This effect distorts an image by creating a torus-shaped object, placing it over the input image, and applying the refraction.

The torus lens distortion filter uses the following properties:

The following code creates a filter that results in a torus-shaped object placed over the image:

```swift
func torusLens(inputImage: CIImage) -> CIImage {
    let filter = CIFilter.torusLensDistortion()
    filter.inputImage = inputImage
    filter.radius = 620
    filter.refraction = 1.7
    filter.center = CGPoint(x: 1791, y: 1344)
    filter.width = 360
    return filter.outputImage!
}
```

![Two images next to each other. The image on the left contains a black-and-white checkerboard pattern. The image on the right has the torus lens distortion filter applied. The image appears to have a ring of distortion around the center.](https://docs-assets.developer.apple.com/published/25b1ca525e15f37ef1e9efdba9f207a2/media-4407288%402x.png)

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
- [class func ninePartStretched() -> any CIFilter & CINinePartStretched](cifilter-swift.class/ninepartstretched.md)
  Distorts an image by stretching it between two breakpoints.
- [class func ninePartTiled() -> any CIFilter & CINinePartTiled](cifilter-swift.class/nineparttiled.md)
  Distorts an image by tiling portions of it.
- [class func pinchDistortion() -> any CIFilter & CIPinchDistortion](cifilter-swift.class/pinchdistortion.md)
  Distorts an image by creating a pinch effect with stronger distortion in the center.
- [class func stretchCrop() -> any CIFilter & CIStretchCrop](cifilter-swift.class/stretchcrop.md)
  Distorts an image by stretching or cropping to fit a specified size.
- [class func twirlDistortion() -> any CIFilter & CITwirlDistortion](cifilter-swift.class/twirldistortion.md)
  Distorts an image by rotating pixels around a center point.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cifilter-swift.class/toruslensdistortion())*