# CIMorphologyRectangleMaximum

**Framework**: Core Image  
**Kind**: protocol

The properties you use to configure a morphology rectangle maximum filter.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
protocol CIMorphologyRectangleMaximum : CIFilterProtocol
```

## Topics

### Instance Properties
- [var height: Float](cimorphologyrectanglemaximum/height.md)
  The height, in pixels, of the morphological structuring element.
- [var inputImage: CIImage?](cimorphologyrectanglemaximum/inputimage.md)
  The image to use as an input image.
- [var width: Float](cimorphologyrectanglemaximum/width.md)
  The width, in pixels, of the morphological structuring element.

## Relationships

### Inherits From
- [CIFilterProtocol](cifilterprotocol.md)

## See Also

- [class func morphologyRectangleMaximum() -> any CIFilter & CIMorphologyRectangleMaximum](cifilter-swift.class/morphologyrectanglemaximum.md)
  Blurs a rectangular area by enlarging contrasting pixels.
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
- [protocol CIMorphologyRectangleMinimum](cimorphologyrectangleminimum.md)
  The properties you use to configure a morphology rectangle minimum filter.
- [protocol CIMotionBlur](cimotionblur.md)
  The properties you use to configure a motion blur filter.
- [protocol CINoiseReduction](cinoisereduction.md)
  The properties you use to configure a noise reduction filter.
- [protocol CIZoomBlur](cizoomblur.md)
  The properties you use to configure a zoom blur filter.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cimorphologyrectanglemaximum)*