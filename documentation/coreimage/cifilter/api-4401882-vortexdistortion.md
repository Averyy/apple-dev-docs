# vortexDistortion()

**Framework**: Core Image  
**Kind**: clm

Distorts an image by using a vortex effect created by rotating pixels around a point.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 17.5+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
class func vortexDistortion() -> any CIFilter & CIVortexDistortion
```

#### Return_value

The distorted image.

#### Discussion

This method applies the vortex distortion filter to an image. This effect distorts an image by rotating pixels around the defined center to simulate a vortex. You can specify the number of rotations to control the strength of the effect.

The vortex distortion filter uses the following properties:

The following code creates a filter that results in a small vortex effect:

```swift
func vortexDistort(inputImage: CIImage) -> CIImage {
    let filter = CIFilter.vortexDistortion()
    filter.inputImage = inputImage
    filter.radius = 700
    filter.angle = 56.54866776461628
    filter.center = CGPoint(x: 1124, y: 778)
    return filter.outputImage!
}
```

![Two images next to each other. The image on the left contains a black-and-white checkerboard pattern. The image on the right has the vortex distortion filter applied. The center of the image appears to be tightly twisted with the amount of twist decreasing very quickly towards the edge of the image.](https://docs-assets.developer.apple.com/published/7d5d05ff4e/rendered2x-1707383505.png)

## See Also

- [class func bumpDistortion() -> any CIFilter & CIBumpDistortion](cifilter/4401850-bumpdistortion.md)
  Distorts an image with a concave or convex bump.
- [class func bumpDistortionLinear() -> any CIFilter & CIBumpDistortionLinear](cifilter/4401851-bumpdistortionlinear.md)
  Linearly distorts an image with a concave or convex bump.
- [class func circleSplashDistortion() -> any CIFilter & CICircleSplashDistortion](cifilter/4401853-circlesplashdistortion.md)
  Distorts an image with radiating circles to the periphery of the image.
- [class func circularWrap() -> any CIFilter & CICircularWrap](cifilter/4401854-circularwrap.md)
  Distorts an image by increasing the distance of the center of the image.
- [class func displacementDistortion() -> any CIFilter & CIDisplacementDistortion](cifilter/4401863-displacementdistortion.md)
  Applies the grayscale values of the second image to the first image.
- [class func droste() -> any CIFilter & CIDroste](cifilter/4401864-droste.md)
  Stylizes an image with the Droste effect.
- [class func glassDistortion() -> any CIFilter & CIGlassDistortion](cifilter/4401865-glassdistortion.md)
  Distorts an image by applying a glass-like texture.
- [class func glassLozenge() -> any CIFilter & CIGlassLozenge](cifilter/4401866-glasslozenge.md)
  Creates a lozenge-shaped lens and distorts the image.
- [class func holeDistortion() -> any CIFilter & CIHoleDistortion](cifilter/4401867-holedistortion.md)
  Distorts an image with a circular area that pushes the image outward.
- [class func lightTunnel() -> any CIFilter & CILightTunnel](cifilter/4401868-lighttunnel.md)
  Distorts an image by generating a light tunnel.
- [class func ninePartStretched() -> any CIFilter & CINinePartStretched](cifilter/4401871-ninepartstretched.md)
  Distorts an image by stretching it between two breakpoints.
- [class func ninePartTiled() -> any CIFilter & CINinePartTiled](cifilter/4401872-nineparttiled.md)
  Distorts an image by tiling portions of it.
- [class func pinchDistortion() -> any CIFilter & CIPinchDistortion](cifilter/4401874-pinchdistortion.md)
  Distorts an image by creating a pinch effect with stronger distortion in the center.
- [class func stretchCrop() -> any CIFilter & CIStretchCrop](cifilter/4401877-stretchcrop.md)
  Distorts an image by stretching or cropping to fit a specified size.
- [class func torusLensDistortion() -> any CIFilter & CITorusLensDistortion](cifilter/4401879-toruslensdistortion.md)
  Creates a torus-shaped lens to distort the image.
- [class func twirlDistortion() -> any CIFilter & CITwirlDistortion](cifilter/4401880-twirldistortion.md)
  Distorts an image by rotating pixels around a center point.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cifilter/4401882-vortexdistortion)*