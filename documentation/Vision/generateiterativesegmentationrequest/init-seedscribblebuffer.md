# init(seedScribbleBuffer:_:)

**Framework**: Vision  
**Kind**: init

Instantiates with a scribble buffer.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
init(seedScribbleBuffer: CVReadOnlyPixelBuffer, _ revision: GenerateIterativeSegmentationRequest.Revision? = nil)
```

## See Also

- [init(seedBox: NormalizedRect, GenerateIterativeSegmentationRequest.Revision?)](generateiterativesegmentationrequest/init(seedbox:_:).md)
  Instantiates with a seed box.
- [init(seedPoint: NormalizedPoint, GenerateIterativeSegmentationRequest.Revision?)](generateiterativesegmentationrequest/init(seedpoint:_:).md)
  Instantiates with a seed point.
- [GenerateIterativeSegmentationRequest.Result](generateiterativesegmentationrequest/result.md)
  The result is returned as a gray mask image. It can be nil if there is nothing to segment.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/generateiterativesegmentationrequest/init(seedscribblebuffer:_:))*