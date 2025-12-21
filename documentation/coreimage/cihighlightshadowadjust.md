# CIHighlightShadowAdjust

**Framework**: Core Image  
**Kind**: protocol

The properties you use to configure a highlight-shadow adjust filter.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
protocol CIHighlightShadowAdjust : CIFilterProtocol
```

## Topics

### Instance Properties
- [var highlightAmount: Float](cihighlightshadowadjust/highlightamount.md)
  The amount of adjustment to the highlights in the image.
- [var inputImage: CIImage?](cihighlightshadowadjust/inputimage.md)
  The image to use as an input image.
- [var radius: Float](cihighlightshadowadjust/radius.md)
  The shadow highlight radius.
- [var shadowAmount: Float](cihighlightshadowadjust/shadowamount.md)
  The amount of adjustment to the shadows in the image.

## Relationships

### Inherits From
- [CIFilterProtocol](cifilterprotocol.md)

## See Also

- [class func highlightShadowAdjust() -> any CIFilter & CIHighlightShadowAdjust](cifilter-swift.class/highlightshadowadjust.md)
  Adjusts the highlights of colors to reduce shadows.
- [protocol CIBlendWithMask](ciblendwithmask.md)
  The properties you use to configure a blend with mask filter.
- [protocol CIBloom](cibloom.md)
  The properties you use to configure a bloom filter.
- [protocol CICannyEdgeDetector](cicannyedgedetector.md)
- [protocol CIComicEffect](cicomiceffect.md)
  The properties you use to configure a comic effect filter.
- [protocol CICoreMLModel](cicoremlmodel.md)
  The properties you use to configure a Core ML model filter.
- [protocol CICrystallize](cicrystallize.md)
  The properties you use to configure a crystalize filter.
- [protocol CIDepthOfField](cidepthoffield.md)
  The properties you use to configure a depth-of-field filter.
- [protocol CIEdgeWork](ciedgework.md)
  The properties you use to configure an edge-work filter.
- [protocol CIEdges](ciedges.md)
  The properties you use to configure an edges filter.
- [protocol CIGaborGradients](cigaborgradients.md)
  The properties you use to configure a Gabor gradients filter.
- [protocol CIGloom](cigloom.md)
  The properties you use to configure a gloom filter.
- [protocol CIHeightFieldFromMask](ciheightfieldfrommask.md)
  The properties you use to configure a height-field-from-mask filter.
- [protocol CIHexagonalPixellate](cihexagonalpixellate.md)
  The properties you use to configure a hexagonal pixellate filter.
- [protocol CILineOverlay](cilineoverlay.md)
  The properties you use to configure a line overlay filter.
- [protocol CIMix](cimix.md)
  The properties you use to configure a mix filter.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cihighlightshadowadjust)*