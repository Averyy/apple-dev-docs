# init(seedBox:_:)

**Framework**: Vision  
**Kind**: init  
**Role**: Initializer

Instantiates with a seed box.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
init(seedBox: NormalizedRect, _ revision: GenerateIterativeSegmentationRequest.Revision? = nil)
```

## Mentions

- [Isolating an object from a tap, box, or scribble](../segmenting-objects-with-iterative-refinement.md)

#### Discussion

No result will be produced if the box is outside the `regionOfInterest`. By default, the `regionOfInterest` is the whole image.

## See Also

### Creating a request
- [init(seedPoint: NormalizedPoint, GenerateIterativeSegmentationRequest.Revision?)](./init%28seedpoint,_%29.md)
  Instantiates with a seed point.
- [init(seedScribbleBuffer: CVReadOnlyPixelBuffer, GenerateIterativeSegmentationRequest.Revision?)](./init%28seedscribblebuffer,_%29.md)
  Instantiates with a scribble buffer.
- [GenerateIterativeSegmentationRequest.Result](./result.md)
  The result is returned as a gray mask image. It can be nil if there is nothing to segment.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/generateiterativesegmentationrequest/init(seedbox:_:))*