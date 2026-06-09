# GenerateSelectedObjectSegmentationRequest

**Framework**: Vision  
**Kind**: struct

Generates a segmentation mask based on the provided points, rectangle, mask or scribble The request supports a maximum of 14 points or 12 points and a box

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
struct GenerateSelectedObjectSegmentationRequest
```

## Topics

### Initializers
- [init(GenerateSelectedObjectSegmentationRequest.Revision?, frameAnalysisSpacing: CMTime?)](generateselectedobjectsegmentationrequest/init(_:frameanalysisspacing:).md)
  Initializer
### Instance Properties
- [var box: NormalizedRect?](generateselectedobjectsegmentationrequest/box.md)
  The bounding box for the segmentation request.
- [var excludedPoints: [NormalizedPoint]](generateselectedobjectsegmentationrequest/excludedpoints.md)
  Points that are excluded from the desired segmentation
- [var includedPoints: [NormalizedPoint]](generateselectedobjectsegmentationrequest/includedpoints.md)
  Points that are part of the desired segmentation
- [var mask: CVReadOnlyPixelBuffer?](generateselectedobjectsegmentationrequest/mask.md)
  A segmentation mask.
- [let revision: GenerateSelectedObjectSegmentationRequest.Revision](generateselectedobjectsegmentationrequest/revision-swift.property.md)
  The request’s configured revision.
- [var scribble: CVReadOnlyPixelBuffer?](generateselectedobjectsegmentationrequest/scribble.md)
  A scribble buffer of the object to be masked.
### Instance Methods
- [func downloadWithProgress() throws -> DownloadableAssetsProgress](generateselectedobjectsegmentationrequest/downloadwithprogress.md)
### Type Properties
- [static let allSupportedRevisions: [GenerateSelectedObjectSegmentationRequest.Revision]](generateselectedobjectsegmentationrequest/allsupportedrevisions.md)
  The collection all currently-supported public and private revisions for `GenerateSelectedObjectSegmentationRequest`.
- [static let supportedRevisions: [GenerateSelectedObjectSegmentationRequest.Revision]](generateselectedobjectsegmentationrequest/supportedrevisions.md)
  The revisions supported by `GenerateSelectedObjectSegmentationRequest`.
### Enumerations
- [GenerateSelectedObjectSegmentationRequest.Revision](generateselectedobjectsegmentationrequest/revision-swift.enum.md)

## Relationships

### Conforms To
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [DownloadableAssetsRequest](downloadableassetsrequest.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [ImageProcessingRequest](imageprocessingrequest.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
- [StatefulRequest](statefulrequest.md)
- [VisionRequest](visionrequest.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/generateselectedobjectsegmentationrequest)*