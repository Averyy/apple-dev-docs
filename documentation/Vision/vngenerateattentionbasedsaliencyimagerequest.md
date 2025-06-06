# VNGenerateAttentionBasedSaliencyImageRequest

**Framework**: Vision  
**Kind**: class

An object that produces a heat map that identifies the parts of an image most likely to draw attention.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
class VNGenerateAttentionBasedSaliencyImageRequest
```

## Topics

### Accessing the Results
- [var results: [VNSaliencyImageObservation]?](vngenerateattentionbasedsaliencyimagerequest/results.md)
  The results of the image saliency request.
### Identifying Request Revisions
- [let VNGenerateAttentionBasedSaliencyImageRequestRevision1: Int](vngenerateattentionbasedsaliencyimagerequestrevision1.md)
  A constant for specifying revision 1 of the image saliency request.

## Relationships

### Inherits From
- [VNImageBasedRequest](vnimagebasedrequest.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [Cropping Images Using Saliency](cropping-images-using-saliency.md)
  Isolate regions in an image that are most likely to draw people’s attention.
- [Highlighting Areas of Interest in an Image Using Saliency](highlighting-areas-of-interest-in-an-image-using-saliency.md)
  Quantify and visualize where people are likely to look in an image.
- [class VNGenerateObjectnessBasedSaliencyImageRequest](vngenerateobjectnessbasedsaliencyimagerequest.md)
  A request that generates a heat map that identifies the parts of an image most likely to represent objects.
- [class VNSaliencyImageObservation](vnsaliencyimageobservation.md)
  An observation that contains a grayscale heat map of important areas across an image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/vngenerateattentionbasedsaliencyimagerequest)*