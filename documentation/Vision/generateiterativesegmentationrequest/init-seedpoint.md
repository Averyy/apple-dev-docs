# init(seedPoint:_:)

**Framework**: Vision  
**Kind**: init

Instantiates with a seed point.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
init(seedPoint: NormalizedPoint, _ revision: GenerateIterativeSegmentationRequest.Revision? = nil)
```

#### Discussion

No result will be produced if the point is outside the `regionOfInterest`. By default, the `regionOfInterest` is the whole image. This point is counted toward the total number of points that can be added.

## See Also

- [init(seedBox: NormalizedRect, GenerateIterativeSegmentationRequest.Revision?)](generateiterativesegmentationrequest/init(seedbox:_:).md)
  Instantiates with a seed box.
- [init(seedScribbleBuffer: CVReadOnlyPixelBuffer, GenerateIterativeSegmentationRequest.Revision?)](generateiterativesegmentationrequest/init(seedscribblebuffer:_:).md)
  Instantiates with a scribble buffer.
- [GenerateIterativeSegmentationRequest.Result](generateiterativesegmentationrequest/result.md)
  The result is returned as a gray mask image. It can be nil if there is nothing to segment.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/generateiterativesegmentationrequest/init(seedpoint:_:))*