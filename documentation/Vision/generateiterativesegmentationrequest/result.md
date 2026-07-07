# GenerateIterativeSegmentationRequest.Result

**Framework**: Vision  
**Kind**: typealias

The result is returned as a gray mask image. It can be nil if there is nothing to segment.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
typealias Result = PixelBufferObservation?
```

## See Also

- [init(seedBox: NormalizedRect, GenerateIterativeSegmentationRequest.Revision?)](generateiterativesegmentationrequest/init(seedbox:_:).md)
  Instantiates with a seed box.
- [init(seedPoint: NormalizedPoint, GenerateIterativeSegmentationRequest.Revision?)](generateiterativesegmentationrequest/init(seedpoint:_:).md)
  Instantiates with a seed point.
- [init(seedScribbleBuffer: CVReadOnlyPixelBuffer, GenerateIterativeSegmentationRequest.Revision?)](generateiterativesegmentationrequest/init(seedscribblebuffer:_:).md)
  Instantiates with a scribble buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/generateiterativesegmentationrequest/result)*