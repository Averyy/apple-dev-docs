# morphologyMinimum()

**Framework**: Core Image  
**Kind**: clm

Blurs a circular area by reducing contrasting pixels.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
class func morphologyMinimum() -> any CIFilter & CIMorphologyMinimum
```

#### Return_value

The blurred image. 

#### Discussion

This method applies the morphology minimum filter to an image. The effect targets a circular section of the image, calculating the median color values to find colors that make up more than half the working area. Using this calculation, the effect reduces the pixels with contrasting colors to take up less of the working area. The effect is then repeated throughout the image.

The morphology minimum filter uses the following properties:

The following code creates a filter that adds a blur that adds darkness to the input image:

```swift
    func morphologyMinimum(inputImage: CIImage) -> CIImage? {

        let morphologyMinimumFilter = CIFilter.morphologyMinimum()
        morphologyMinimumFilter.inputImage = inputImage
        morphologyMinimumFilter.radius = 5
        return morphologyMinimumFilter.outputImage
    }
```

![Two photographs of a beach at sunset with multiple palm trees. The photo on the left is clear and crisp. In the photo on the right, a morphology minimum blur has been applied, making the image hazy and the edges of the palm trees darker and less distinct.](https://docs-assets.developer.apple.com/published/23cdafe9e4/rendered2x-1582929037.png)

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
- [class func morphologyRectangleMaximum() -> any CIFilter & CIMorphologyRectangleMaximum](cifilter/3228367-morphologyrectanglemaximum.md)
  Blurs a rectangular area by enlarging contrasting pixels.
- [class func morphologyRectangleMinimum() -> any CIFilter & CIMorphologyRectangleMinimum](cifilter/3228368-morphologyrectangleminimum.md)
  Blurs a rectangular area by reducing contrasting pixels.
- [class func motionBlur() -> any CIFilter & CIMotionBlur](cifilter/3228369-motionblur.md)
  Creates motion blur on an image.
- [class func noiseReduction() -> any CIFilter & CINoiseReduction](cifilter/3228372-noisereduction.md)
  Reduces noise by sharpening the edges of objects.
- [class func zoomBlur() -> any CIFilter & CIZoomBlur](cifilter/3228434-zoomblur.md)
  Creates a zoom blur centered around a single point on the image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cifilter/3228366-morphologyminimum)*