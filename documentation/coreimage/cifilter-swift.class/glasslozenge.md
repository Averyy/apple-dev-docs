# glassLozenge()

**Framework**: Core Image  
**Kind**: method

Creates a lozenge-shaped lens and distorts the image.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
class func glassLozenge() -> any CIFilter & CIGlassLozenge
```

#### Return Value

The distorted image.

#### Discussion

This method applies the glass lozenge filter to an image. This effect distorts an image by creating a lozenge shape placed over the input image.

The absolute threshold filter uses the following properties:

The following code creates a filter that results in a large glass lozenge distorting the image:

```swift
func glassLozenge(inputImage: CIImage) -> CIImage {
    let filter = CIFilter.glassLozenge()
    filter.inputImage = inputImage
    filter.refraction = 1.7
    filter.point0 = CGPoint(x: 150, y: 1050)
    filter.point1 = CGPoint(x: 3050, y: 150)
    return filter.outputImage!
}
```

![Two images next to each other. The left image contains a photograph of three hydrangea flowers with leaves in the background. In the right image, the glass lozenge filter has been applied. It appears as if the glass pill shape has been placed on top of the image.](https://docs-assets.developer.apple.com/published/d51913b583599c768538cad7c75283d4/media-4407280%402x.png)

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
- [class func torusLensDistortion() -> any CIFilter & CITorusLensDistortion](cifilter-swift.class/toruslensdistortion.md)
  Creates a torus-shaped lens to distort the image.
- [class func twirlDistortion() -> any CIFilter & CITwirlDistortion](cifilter-swift.class/twirldistortion.md)
  Distorts an image by rotating pixels around a center point.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cifilter-swift.class/glasslozenge())*