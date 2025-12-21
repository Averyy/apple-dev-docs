# median()

**Framework**: Core Image  
**Kind**: method

Calculates the median of an image to refine detail.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
class func median() -> any CIFilter & CIMedian
```

#### Return Value

The blurred image.

#### Discussion

This method applies the median filter to an image. The effect computes the median value of colors for a group of neighboring pixels and replaces each pixel with calculated data.

The median filter uses the following properties:

The following code creates a filter that refines the detail in the input image:

```swift
    func medianBlur(inputImage: CIImage) -> CIImage? {

        let medianBlurFilter = CIFilter.median()
        medianBlurFilter.inputImage = inputImage
        return medianBlurFilter.outputImage
    }
```

![Two photographs of a beach at sunset with multiple palm trees. The photo on the left is clear. In the photo on the right, a median effect has been applied, and the image is sharper and has more detail in the leafs of the trees in the foreground.](https://docs-assets.developer.apple.com/published/c5f5eb893c740770d52e18ca370d34ba/media-3544967%402x.png)

## See Also

- [class func bokehBlur() -> any CIFilter & CIBokehBlur](cifilter-swift.class/bokehblur.md)
  Applies a bokeh effect to an image.
- [class func boxBlur() -> any CIFilter & CIBoxBlur](cifilter-swift.class/boxblur.md)
  Applies a square-shaped blur to an area of an image.
- [class func discBlur() -> any CIFilter & CIDiscBlur](cifilter-swift.class/discblur.md)
  Applies a circle-shaped blur to an area of an image.
- [class func gaussianBlur() -> any CIFilter & CIGaussianBlur](cifilter-swift.class/gaussianblur.md)
  Blurs an image with a Gaussian distribution pattern.
- [class func maskedVariableBlur() -> any CIFilter & CIMaskedVariableBlur](cifilter-swift.class/maskedvariableblur.md)
  Blurs a specified portion of an image.
- [class func morphologyGradient() -> any CIFilter & CIMorphologyGradient](cifilter-swift.class/morphologygradient.md)
  Detects and highlights edges of objects.
- [class func morphologyMaximum() -> any CIFilter & CIMorphologyMaximum](cifilter-swift.class/morphologymaximum.md)
  Blurs a circular area by enlarging contrasting pixels.
- [class func morphologyMinimum() -> any CIFilter & CIMorphologyMinimum](cifilter-swift.class/morphologyminimum.md)
  Blurs a circular area by reducing contrasting pixels.
- [class func morphologyRectangleMaximum() -> any CIFilter & CIMorphologyRectangleMaximum](cifilter-swift.class/morphologyrectanglemaximum.md)
  Blurs a rectangular area by enlarging contrasting pixels.
- [class func morphologyRectangleMinimum() -> any CIFilter & CIMorphologyRectangleMinimum](cifilter-swift.class/morphologyrectangleminimum.md)
  Blurs a rectangular area by reducing contrasting pixels.
- [class func motionBlur() -> any CIFilter & CIMotionBlur](cifilter-swift.class/motionblur.md)
  Creates motion blur on an image.
- [class func noiseReduction() -> any CIFilter & CINoiseReduction](cifilter-swift.class/noisereduction.md)
  Reduces noise by sharpening the edges of objects.
- [class func zoomBlur() -> any CIFilter & CIZoomBlur](cifilter-swift.class/zoomblur.md)
  Creates a zoom blur centered around a single point on the image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cifilter-swift.class/median())*