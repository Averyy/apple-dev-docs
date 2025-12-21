# zoomBlur()

**Framework**: Core Image  
**Kind**: method

Creates a zoom blur centered around a single point on the image.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
class func zoomBlur() -> any CIFilter & CIZoomBlur
```

#### Return Value

The blurred image.

#### Discussion

This method applies the zoom blur filter to an image. This effect mimics the zoom of a camera when capturing the image.

The zoom blur filter uses the following properties:

The following code creates a filter that adds a zoom blur to the input image:

```swift
    func zoomBlur(inputImage: CIImage) -> CIImage? {

        let zoomBlurFilter = CIFilter.zoomBlur()
        zoomBlurFilter.inputImage = inputImage
        zoomBlurFilter.amount = 5
        zoomBlurFilter.center = CGPoint(x: 150, y: 150)
        return zoomBlurFilter.outputImage
    }
```

![Two photographs of a beach at sunset with multiple palm trees. The photo on the left is clear and crisp. In photo on the right, a zoom blur filter has been applied resulting in a distorted and fuzzy image.](https://docs-assets.developer.apple.com/published/778dded0e09c49a62b4d88af457e50dd/media-3544962%402x.png)

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cifilter-swift.class/zoomblur())*