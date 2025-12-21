# bokehBlur()

**Framework**: Core Image  
**Kind**: method

Applies a bokeh effect to an image.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
class func bokehBlur() -> any CIFilter & CIBokehBlur
```

#### Return Value

The blurred image.

#### Discussion

This method applies the bokeh blur filter to an image. The effect targets a circular area of pixels defined by the `radius` and blurs the area. The filter adds smaller intense blur rings.

The bokeh blur filter uses the following properties:

The following code creates a filter that adds a softer blur to the input image:

```swift
    func bokehBlur(inputImage: CIImage) -> CIImage? {

        let bokehBlurFilter = CIFilter.bokehBlur()
        bokehBlurFilter.inputImage = inputImage
        bokehBlurFilter.ringSize = 0.1
        bokehBlurFilter.ringAmount = 0
        bokehBlurFilter.softness = 1
        bokehBlurFilter.radius = 20
        return bokehBlurFilter.outputImage
    }
```

![Two photographs of a beach at sunset with multiple palm trees. The photo on the left is clear and crisp. In the photo on the right, a bokeh blur filter has been applied and the image is softer and looks slightly fuzzy or hazy.](https://docs-assets.developer.apple.com/published/05e232c2a39eb51f6c9a6de5ff51777e/media-3544959%402x.png)

## See Also

- [class func boxBlur() -> any CIFilter & CIBoxBlur](cifilter-swift.class/boxblur.md)
  Applies a square-shaped blur to an area of an image.
- [class func discBlur() -> any CIFilter & CIDiscBlur](cifilter-swift.class/discblur.md)
  Applies a circle-shaped blur to an area of an image.
- [class func gaussianBlur() -> any CIFilter & CIGaussianBlur](cifilter-swift.class/gaussianblur.md)
  Blurs an image with a Gaussian distribution pattern.
- [class func maskedVariableBlur() -> any CIFilter & CIMaskedVariableBlur](cifilter-swift.class/maskedvariableblur.md)
  Blurs a specified portion of an image.
- [class func median() -> any CIFilter & CIMedian](cifilter-swift.class/median.md)
  Calculates the median of an image to refine detail.
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

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cifilter-swift.class/bokehblur())*