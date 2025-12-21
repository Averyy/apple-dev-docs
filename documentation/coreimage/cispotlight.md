# CISpotLight

**Framework**: Core Image  
**Kind**: protocol

The properties you use to configure a spotlight filter.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
protocol CISpotLight : CIFilterProtocol
```

## Topics

### Instance Properties
- [var brightness: Float](cispotlight/brightness.md)
  The brightness of the spotlight.
- [var color: CIColor](cispotlight/color.md)
  The color of the spotlight.
- [var concentration: Float](cispotlight/concentration.md)
  The size of the spotlight.
- [var inputImage: CIImage?](cispotlight/inputimage.md)
  The image to use as an input image.
- [var lightPointsAt: CIVector](cispotlight/lightpointsat.md)
  The x and y position that the spotlight points at.
- [var lightPosition: CIVector](cispotlight/lightposition.md)
  The x and y position of the spotlight.

## Relationships

### Inherits From
- [CIFilterProtocol](cifilterprotocol.md)

## See Also

- [class func spotLight() -> any CIFilter & CISpotLight](cifilter-swift.class/spotlight.md)
  Highlights a definined area of the image.
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
- [protocol CIHighlightShadowAdjust](cihighlightshadowadjust.md)
  The properties you use to configure a highlight-shadow adjust filter.
- [protocol CILineOverlay](cilineoverlay.md)
  The properties you use to configure a line overlay filter.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cispotlight)*