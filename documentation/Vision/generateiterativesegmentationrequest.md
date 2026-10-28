# GenerateIterativeSegmentationRequest

**Framework**: Vision  
**Kind**: class  
**Role**: Class

A request that generates a segmentation mask from points, a rectangle, or a scribble.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
final class GenerateIterativeSegmentationRequest
```

## Mentions

- [Isolating an object from a tap, box, or scribble](./segmenting-objects-with-iterative-refinement.md)

## Overview

Initialize with a seed point, a seed rectangle, or a seed scribble buffer to generate the initial segmentation mask. Then add points to iteratively refine the segmentation mask. The request supports a maximum of 13 points when seeded with a point or scribble, or 11 points when seeded with a box.

## Topics

### Creating a request
- [init(seedBox: NormalizedRect, GenerateIterativeSegmentationRequest.Revision?)](./generateiterativesegmentationrequest/init%28seedbox,_%29.md)
  Instantiates with a seed box.
- [init(seedPoint: NormalizedPoint, GenerateIterativeSegmentationRequest.Revision?)](./generateiterativesegmentationrequest/init%28seedpoint,_%29.md)
  Instantiates with a seed point.
- [init(seedScribbleBuffer: CVReadOnlyPixelBuffer, GenerateIterativeSegmentationRequest.Revision?)](./generateiterativesegmentationrequest/init%28seedscribblebuffer,_%29.md)
  Instantiates with a scribble buffer.
- [GenerateIterativeSegmentationRequest.Result](./generateiterativesegmentationrequest/result.md)
  The result is returned as a gray mask image. It can be nil if there is nothing to segment.
### Updating the mask
- [func addExcludedPoint(NormalizedPoint) throws](./generateiterativesegmentationrequest/addexcludedpoint%28_%29.md)
  Refines the mask with a point that is excluded from the desired segmentation. Throws an error if the total number of added points exceeds the limit. (13 points when seedPoint or seedScribbleBuffer was used, or 11 points when seedBox was used)
- [func addIncludedPoint(NormalizedPoint) throws](./generateiterativesegmentationrequest/addincludedpoint%28_%29.md)
  Refines the mask with a point that is part of the desired segmentation. Throws an error if the total number of added points exceeds the limit. (13 points when seedPoint or seedScribbleBuffer was used, or 11 points when seedBox was used)
### Accessing the quality level
- [var qualityLevel: GenerateIterativeSegmentationRequest.QualityLevel](./generateiterativesegmentationrequest/qualitylevel-swift.property.md)
  Controls the resolution of the produced mask.
- [GenerateIterativeSegmentationRequest.QualityLevel](./generateiterativesegmentationrequest/qualitylevel-swift.enum.md)
  The resolution and quality of the segmentation mask the request produces.
### Getting the revision
- [let revision: GenerateIterativeSegmentationRequest.Revision](./generateiterativesegmentationrequest/revision-swift.property.md)
  The request’s configured revision.
- [GenerateIterativeSegmentationRequest.Revision](./generateiterativesegmentationrequest/revision-swift.enum.md)
- [static let supportedRevisions: [GenerateIterativeSegmentationRequest.Revision]](./generateiterativesegmentationrequest/supportedrevisions.md)
  The revisions supported by [`GenerateIterativeSegmentationRequest`](./generateiterativesegmentationrequest.md).
### Comparing the request
- [static func == (GenerateIterativeSegmentationRequest, GenerateIterativeSegmentationRequest) -> Bool](./generateiterativesegmentationrequest/eqeq%28_,_%29.md)
  Returns a Boolean value indicating whether two instances are equal.

## Relationships

### Conforms To
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [DownloadableAssetsRequest](./downloadableassetsrequest.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [ImageProcessingRequest](./imageprocessingrequest.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)
- [VisionRequest](./visionrequest.md)

## See Also

### Image segmentation and subject lifting
- [Isolating an object from a tap, box, or scribble](./segmenting-objects-with-iterative-refinement.md)
  Generate and refine a mask that isolates an object in an image based on a person’s selection.
- [Segmenting objects using taps, scribbles or rectangles](./segmenting-objects-using-taps-scribbles-or-rectangles.md)
  Select objects or regions in a photo using taps, scribbles, or rectangle selection, and generate a segmentation mask using the iterative segmentation API.
- [struct GenerateForegroundInstanceMaskRequest](./generateforegroundinstancemaskrequest.md)
  A request that generates an instance mask of noticeable objects to separate from the background.
- [struct GeneratePersonInstanceMaskRequest](./generatepersoninstancemaskrequest.md)
  A request that produces a mask of individual people it finds in the input image.
- [class GeneratePersonSegmentationRequest](./generatepersonsegmentationrequest.md)
  A request that produces a matte image for a person it finds in the input image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/generateiterativesegmentationrequest)*