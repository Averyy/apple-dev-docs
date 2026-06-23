# GenerateIterativeSegmentationRequest

**Framework**: Vision  
**Kind**: class

Generates a segmentation mask based on the provided points, rectangle, or scribble The request supports a maximum of 13 points or 11 points and a box

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
final class GenerateIterativeSegmentationRequest
```

## Topics

### Initializers
- [init(seedBox: NormalizedRect, GenerateIterativeSegmentationRequest.Revision?)](generateiterativesegmentationrequest/init(seedbox:_:).md)
  Instantiates with a seed box.
- [init(seedPoint: NormalizedPoint, GenerateIterativeSegmentationRequest.Revision?)](generateiterativesegmentationrequest/init(seedpoint:_:).md)
  Instantiates with a seed point.
- [init(seedScribbleBuffer: CVReadOnlyPixelBuffer, GenerateIterativeSegmentationRequest.Revision?)](generateiterativesegmentationrequest/init(seedscribblebuffer:_:).md)
  Instantiates with a scribble buffer.
### Instance Properties
- [var qualityLevel: GenerateIterativeSegmentationRequest.QualityLevel](generateiterativesegmentationrequest/qualitylevel-swift.property.md)
  Controls the resolution of the produced mask.
- [let revision: GenerateIterativeSegmentationRequest.Revision](generateiterativesegmentationrequest/revision-swift.property.md)
  The request’s configured revision.
### Instance Methods
- [func addExcludedPoint(NormalizedPoint) throws](generateiterativesegmentationrequest/addexcludedpoint(_:).md)
  Refines the mask with a point that is excluded from the desired segmentation. Throws an error if the total number of added points exceeded the limitation. (13 points when seedPoint or seedScribbleBuffer were used or 11 points when seedBox was used)
- [func addIncludedPoint(NormalizedPoint) throws](generateiterativesegmentationrequest/addincludedpoint(_:).md)
  Refines the mask with a point that is part of the desired segmentation. Throws an error if the total number of added points exceeded the limitation. (13 points when seedPoint or seedScribbleBuffer were used or 11 points when seedBox was used)
### Type Aliases
- [GenerateIterativeSegmentationRequest.Result](generateiterativesegmentationrequest/result.md)
  Result is returned as a gray mask image. It can be nil if there is nothing to segment.
### Type Properties
- [static let allSupportedRevisions: [GenerateIterativeSegmentationRequest.Revision]](generateiterativesegmentationrequest/allsupportedrevisions.md)
  The collection all currently-supported public and private revisions for `GenerateIterativeSegmentationRequest`.
- [static let supportedRevisions: [GenerateIterativeSegmentationRequest.Revision]](generateiterativesegmentationrequest/supportedrevisions.md)
  The revisions supported by `GenerateIterativeSegmentationRequest`.
### Enumerations
- [GenerateIterativeSegmentationRequest.QualityLevel](generateiterativesegmentationrequest/qualitylevel-swift.enum.md)
- [GenerateIterativeSegmentationRequest.Revision](generateiterativesegmentationrequest/revision-swift.enum.md)

## Relationships

### Conforms To
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [DownloadableAssetsRequest](downloadableassetsrequest.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [ImageProcessingRequest](imageprocessingrequest.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
- [VisionRequest](visionrequest.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/generateiterativesegmentationrequest)*