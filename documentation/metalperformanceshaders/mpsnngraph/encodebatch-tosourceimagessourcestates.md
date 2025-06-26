# encodeBatch(to:sourceImages:sourceStates:)

**Framework**: Metal Performance Shaders  
**Kind**: method

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.0+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
func encodeBatch(to commandBuffer: any MTLCommandBuffer, sourceImages: [[MPSImage]], sourceStates: [[MPSState]]?) -> [MPSImage]?
```

## See Also

- [func encode(to: any MTLCommandBuffer, sourceImages: [MPSImage]) -> MPSImage?](mpsnngraph/encode(to:sourceimages:).md)
- [func encode(to: any MTLCommandBuffer, sourceImages: [MPSImage], sourceStates: [MPSState]?, intermediateImages: NSMutableArray?, destinationStates: NSMutableArray?) -> MPSImage?](mpsnngraph/encode(to:sourceimages:sourcestates:intermediateimages:destinationstates:).md)
- [class MPSState](mpsstate.md)
  An opaque data container for large storage in MPS CNN filters.
- [class MPSNNBinaryGradientState](mpsnnbinarygradientstate.md)
  A class representing the state of a gradient binary kernel when it was encoded.
- [class MPSNNGradientState](mpsnngradientstate.md)
  A class representing the state of a gradient kernel when it was encoded.
- [func executeAsync(withSourceImages: [MPSImage], completionHandler: MPSNNGraphCompletionHandler) -> MPSImage](mpsnngraph/executeasync(withsourceimages:completionhandler:).md)
- [typealias MPSNNGraphCompletionHandler](mpsnngraphcompletionhandler.md)
  A notification when an asynchronous graph execution has finished.
- [func encodeBatch(to: any MTLCommandBuffer, sourceImages: [[MPSImage]], sourceStates: [[MPSState]]?, intermediateImages: NSMutableArray?, destinationStates: NSMutableArray?) -> [MPSImage]?](mpsnngraph/encodebatch(to:sourceimages:sourcestates:intermediateimages:destinationstates:).md)
- [func readCountForSourceImage(at: Int) -> Int](mpsnngraph/readcountforsourceimage(at:).md)
- [func readCountForSourceState(at: Int) -> Int](mpsnngraph/readcountforsourcestate(at:).md)
- [func reloadFromDataSources()](mpsnngraph/reloadfromdatasources.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpsnngraph/encodebatch(to:sourceimages:sourcestates:))*