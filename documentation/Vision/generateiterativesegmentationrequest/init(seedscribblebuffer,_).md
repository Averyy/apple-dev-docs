# init(seedScribbleBuffer:_:)

**Framework**: Vision  
**Kind**: init  
**Role**: Initializer

Instantiates with a scribble buffer.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
init(seedScribbleBuffer: CVReadOnlyPixelBuffer, _ revision: GenerateIterativeSegmentationRequest.Revision? = nil)
```

## Mentions

- [Isolating an object from a tap, box, or scribble](../segmenting-objects-with-iterative-refinement.md)

## See Also

### Creating a request
- [init(seedBox: NormalizedRect, GenerateIterativeSegmentationRequest.Revision?)](./init%28seedbox,_%29.md)
  Instantiates with a seed box.
- [init(seedPoint: NormalizedPoint, GenerateIterativeSegmentationRequest.Revision?)](./init%28seedpoint,_%29.md)
  Instantiates with a seed point.
- [GenerateIterativeSegmentationRequest.Result](./result.md)
  The result is returned as a gray mask image. It can be nil if there is nothing to segment.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/generateiterativesegmentationrequest/init(seedscribblebuffer:_:))*