# CIZoomBlur

**Framework**: Core Image  
**Kind**: protocol

The properties you use to configure a zoom blur filter.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
protocol CIZoomBlur : CIFilterProtocol
```

## Topics

### Instance Properties
- [var amount: Float](cizoomblur/amount.md)
  The zoom-in amount.
- [var center: CGPoint](cizoomblur/center.md)
  The center of the effect, as x and y coordinates.
- [var inputImage: CIImage?](cizoomblur/inputimage.md)
  The image to use as an input image.

## Relationships

### Inherits From
- [CIFilterProtocol](cifilterprotocol.md)

## See Also

- [class func zoomBlur() -> any CIFilter & CIZoomBlur](cifilter-swift.class/zoomblur.md)
  Creates a zoom blur centered around a single point on the image.
- [protocol CIBokehBlur](cibokehblur.md)
  The properties you use to configure a bokeh blur filter.
- [protocol CIBoxBlur](ciboxblur.md)
  The properties you use to configure a box blur filter.
- [protocol CIDiscBlur](cidiscblur.md)
  The properties you use to configure a disc blur filter.
- [protocol CIGaussianBlur](cigaussianblur.md)
  The properties you use to configure a Gaussian blur filter.
- [protocol CIMaskedVariableBlur](cimaskedvariableblur.md)
  The properties you use to configure a masked variable blur filter.
- [protocol CIMedian](cimedian.md)
  The properties you use to configure a median filter.
- [protocol CIMorphologyGradient](cimorphologygradient.md)
  The properties you use to configure a morphology gradient filter.
- [protocol CIMorphologyMaximum](cimorphologymaximum.md)
  The properties you use to configure a morphology maximum filter.
- [protocol CIMorphologyMinimum](cimorphologyminimum.md)
  The properties you use to configure a morphology minimum filter.
- [protocol CIMorphologyRectangleMaximum](cimorphologyrectanglemaximum.md)
  The properties you use to configure a morphology rectangle maximum filter.
- [protocol CIMorphologyRectangleMinimum](cimorphologyrectangleminimum.md)
  The properties you use to configure a morphology rectangle minimum filter.
- [protocol CIMotionBlur](cimotionblur.md)
  The properties you use to configure a motion blur filter.
- [protocol CINoiseReduction](cinoisereduction.md)
  The properties you use to configure a noise reduction filter.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cizoomblur)*