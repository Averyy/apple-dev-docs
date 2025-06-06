# maskedVariableBlur()

**Framework**: Core Image  
**Kind**: clm

Blurs a specified portion of an image.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
class func maskedVariableBlur() -> any CIFilter & CIMaskedVariableBlur
```

#### Return_value

The blurred image. 

#### Discussion

This method applies the masked variable blur to an image. The effect blurs the image in an area defined by the mask image. The mask image contains shades of grey that define the strength of the blur. Black colors in the mask cause no blurring, and white colors cause maximum blur.

The masked variable blur filter uses the following properties:

The following code creates a filter that adds a blur to the bottom of the input image:

```swift
func maskedVariableBlur(inputImage: CIImage) -> CIImage {
    let filter = CIFilter.maskedVariableBlur()
    filter.inputImage = inputImage
    // Create a mask that goes from white to black vertially.
    let mask = CIFilter.smoothLinearGradient()
    mask.color0 = CIColor.white
    mask.color1 = CIColor.black
    mask.point0 = CGPoint(x: 0, y: 0)
    mask.point1 = CGPoint(x:0, y: inputImage.extent.height)
    filter.mask = mask.outputImage
    filter.radius = 25
    return filter.outputImage!
}
```

![Three images, with two images on the left arranged vertically and a third image on the right vertically centered. The top left image contains a photo of the Golden Gate Bridge with a clear sky in the background. The bottom left image contains a white to black gradient with white at the bottom and black at the top. The right image shows the result of applying the masked variable blur filter using the two images on the left as inputs. The resulting image has a strong blur at the bottom that reduces to zero blur at the top.](https://docs-assets.developer.apple.com/published/bb8ebe5f2a/rendered2x-1709297511.png)

## See Also

- [class func bokehBlur() -> any CIFilter & CIBokehBlur](cifilter/3228277-bokehblur.md)
  Applies a bokeh effect to an image.
- [class func boxBlur() -> any CIFilter & CIBoxBlur](cifilter/3228278-boxblur.md)
  Applies a square-shaped blur to an area of an image.
- [class func discBlur() -> any CIFilter & CIDiscBlur](cifilter/3228311-discblur.md)
  Applies a circle-shaped blur to an area of an image.
- [class func gaussianBlur() -> any CIFilter & CIGaussianBlur](cifilter/3228331-gaussianblur.md)
  Blurs an image with a Gaussian distribution pattern.
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
- [class func noiseReduction() -> any CIFilter & CINoiseReduction](cifilter/3228372-noisereduction.md)
  Reduces noise by sharpening the edges of objects.
- [class func zoomBlur() -> any CIFilter & CIZoomBlur](cifilter/3228434-zoomblur.md)
  Creates a zoom blur centered around a single point on the image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cifilter/3228355-maskedvariableblur)*