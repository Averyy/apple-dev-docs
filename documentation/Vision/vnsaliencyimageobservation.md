# VNSaliencyImageObservation

**Framework**: Vision  
**Kind**: class

An observation that contains a grayscale heat map of important areas across an image.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
class VNSaliencyImageObservation
```

#### Overview

The heat map is a [`CVPixelBuffer`](https://developer.apple.com/documentation/CoreVideo/CVPixelBuffer) in a one-component floating-point pixel format. Its dimensions are 64 x 64 when fetched in real time, or 68 x 68 when requested in its deferred form.

## Topics

### Locating Salient Regions
- [var salientObjects: [VNRectangleObservation]?](vnsaliencyimageobservation/salientobjects.md)
  A collection of objects describing the distinct areas of the saliency heat map.

## Relationships

### Inherits From
- [VNPixelBufferObservation](vnpixelbufferobservation.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSSecureCoding](../Foundation/NSSecureCoding.md)
- [VNRequestRevisionProviding](vnrequestrevisionproviding.md)

## See Also

- [Cropping Images Using Saliency](cropping-images-using-saliency.md)
  Isolate regions in an image that are most likely to draw people’s attention.
- [Highlighting Areas of Interest in an Image Using Saliency](highlighting-areas-of-interest-in-an-image-using-saliency.md)
  Quantify and visualize where people are likely to look in an image.
- [class VNGenerateAttentionBasedSaliencyImageRequest](vngenerateattentionbasedsaliencyimagerequest.md)
  An object that produces a heat map that identifies the parts of an image most likely to draw attention.
- [class VNGenerateObjectnessBasedSaliencyImageRequest](vngenerateobjectnessbasedsaliencyimagerequest.md)
  A request that generates a heat map that identifies the parts of an image most likely to represent objects.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/vnsaliencyimageobservation)*