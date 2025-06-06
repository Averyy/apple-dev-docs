# circleSplashDistortion()

**Framework**: Core Image  
**Kind**: clm

Distorts an image with radiating circles to the periphery of the image.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 17.5+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
class func circleSplashDistortion() -> any CIFilter & CICircleSplashDistortion
```

#### Return_value

The distorted image.

#### Discussion

This method applies the circle splash distortion filter to an image. This effect distorts the pixels starting at the circumference of a circle and emanating outward.

The circle splash distortion filter uses the following properties:

The following code creates a filter that results in a ripple effect applied to the image:

```swift
func circularSplash(inputImage: CIImage) -> CIImage {
    let filter = CIFilter.circleSplashDistortion()
    filter.inputImage = inputImage
    filter.center = CGPoint(x: 50.0, y: 50.0)
    filter.radius = 2.0
    return filter.outputImage!
}
```

![On the left, an image with a checkerboard pattern. On the right, the same image but with a circle splash distortion applied. The center of the image contains a checkerboard pattern with larger squares than the original. This is surrounded by stretched black and white stripes radiating out to the edge of the image.](https://docs-assets.developer.apple.com/published/a4b803bfe5/rendered2x-1707304254.png)

## See Also

- [class func bumpDistortion() -> any CIFilter & CIBumpDistortion](cifilter/4401850-bumpdistortion.md)
  Distorts an image with a concave or convex bump.
- [class func bumpDistortionLinear() -> any CIFilter & CIBumpDistortionLinear](cifilter/4401851-bumpdistortionlinear.md)
  Linearly distorts an image with a concave or convex bump.
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
- [class func vortexDistortion() -> any CIFilter & CIVortexDistortion](cifilter/4401882-vortexdistortion.md)
  Distorts an image by using a vortex effect created by rotating pixels around a point.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cifilter/4401853-circlesplashdistortion)*