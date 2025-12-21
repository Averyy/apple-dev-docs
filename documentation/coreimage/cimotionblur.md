# CIMotionBlur

**Framework**: Core Image  
**Kind**: protocol

The properties you use to configure a motion blur filter.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
protocol CIMotionBlur : CIFilterProtocol
```

## Topics

### Instance Properties
- [var angle: Float](cimotionblur/angle.md)
  The angle of the motion, in radians, that determines which direction the blur smears.
- [var inputImage: CIImage?](cimotionblur/inputimage.md)
  The image to use as an input image.
- [var radius: Float](cimotionblur/radius.md)
  The radius of the blur, in pixels.

## Relationships

### Inherits From
- [CIFilterProtocol](cifilterprotocol.md)

## See Also

- [class func motionBlur() -> any CIFilter & CIMotionBlur](cifilter-swift.class/motionblur.md)
  Creates motion blur on an image.
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
- [protocol CINoiseReduction](cinoisereduction.md)
  The properties you use to configure a noise reduction filter.
- [protocol CIZoomBlur](cizoomblur.md)
  The properties you use to configure a zoom blur filter.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cimotionblur)*