# noiseReduction()

**Framework**: Core Image  
**Kind**: clm

Reduces noise by sharpening the edges of objects.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
class func noiseReduction() -> any CIFilter & CINoiseReduction
```

#### Return_value

The blurred image. 

#### Discussion

This method applies the noise reduction filter to an image. The effect calculates changes in luminance below the noise level and locally blurs the area. Values above the threshold are determined to be edges, and become sharpened.

The morphology noise reduction filter uses the following properties:

The following code creates a filter that reduces noise in the input image:

```swift
    func noiseReduction(inputImage: CIImage) -> CIImage? {

        let noiseReductionfilter = CIFilter.noiseReduction()
        noiseReductionfilter.inputImage = inputImage
        noiseReductionfilter.noiseLevel = 0.2
        noiseReductionfilter.sharpness = 0.4
        return noiseReductionfilter.outputImage
    }
```

![Two photographs of a beach at sunset with multiple palm trees. The photo on the left is in focus. In the photo on the right, a noise reduction filter has been applied, and the edges of the objects such as the palm fronds have more sharpness and detail.](https://docs-assets.developer.apple.com/published/48cc46db0f/rendered2x-1582929037.png)

## See Also

- [class func bokehBlur() -> any CIFilter & CIBokehBlur](cifilter/3228277-bokehblur.md)
  Applies a bokeh effect to an image.
- [class func boxBlur() -> any CIFilter & CIBoxBlur](cifilter/3228278-boxblur.md)
  Applies a square-shaped blur to an area of an image.
- [class func discBlur() -> any CIFilter & CIDiscBlur](cifilter/3228311-discblur.md)
  Applies a circle-shaped blur to an area of an image.
- [class func gaussianBlur() -> any CIFilter & CIGaussianBlur](cifilter/3228331-gaussianblur.md)
  Blurs an image with a Gaussian distribution pattern.
- [class func maskedVariableBlur() -> any CIFilter & CIMaskedVariableBlur](cifilter/3228355-maskedvariableblur.md)
  Blurs a specified portion of an image.
- [class func median() -> any CIFilter & CIMedian](cifilter/3228358-median.md)
  Calculates the median of an image to refine detail.
- [class func morphologyGradient() -> any CIFilter & CIMorphologyGradient](cifilter/3228364-morphologygradient.md)
  Detects and highlights edges of objects.
- [class func morphologyMaximum() -> any CIFilter & CIMorphologyMaximum](cifilter/3228365-morphologymaximum.md)
  Blurs a circular area by enlarging contrasting pixels.
- [class func morphologyMinimum() -> any CIFilter & CIMorphologyMinimum](cifilter/3228366-morphologyminimum.md)
  Blurs a circular area by reducing contrasting pixels.
- [class func morphologyRectangleMaximum() -> any CIFilter & CIMorphologyRectangleMaximum](cifilter/3228367-morphologyrectanglemaximum.md)
  Blurs a rectangular area by enlarging contrasting pixels.
- [class func morphologyRectangleMinimum() -> any CIFilter & CIMorphologyRectangleMinimum](cifilter/3228368-morphologyrectangleminimum.md)
  Blurs a rectangular area by reducing contrasting pixels.
- [class func motionBlur() -> any CIFilter & CIMotionBlur](cifilter/3228369-motionblur.md)
  Creates motion blur on an image.
- [class func zoomBlur() -> any CIFilter & CIZoomBlur](cifilter/3228434-zoomblur.md)
  Creates a zoom blur centered around a single point on the image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cifilter/3228372-noisereduction)*