# GenerateIterativeSegmentationRequest.Result

**Framework**: Vision  
**Kind**: typealias  
**Role**: Type Alias

The result is returned as a gray mask image. It can be nil if there is nothing to segment.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
typealias Result = PixelBufferObservation?
```

## See Also

### Creating a request
- [init(seedBox: NormalizedRect, GenerateIterativeSegmentationRequest.Revision?)](./init%28seedbox,_%29.md)
  Instantiates with a seed box.
- [init(seedPoint: NormalizedPoint, GenerateIterativeSegmentationRequest.Revision?)](./init%28seedpoint,_%29.md)
  Instantiates with a seed point.
- [init(seedScribbleBuffer: CVReadOnlyPixelBuffer, GenerateIterativeSegmentationRequest.Revision?)](./init%28seedscribblebuffer,_%29.md)
  Instantiates with a scribble buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/generateiterativesegmentationrequest/result)*