# temporaryResultStateBatch(commandBuffer:sourceImage:sourceStates:destinationImage:)

**Framework**: Metal Performance Shaders  
**Kind**: method

**Availability**:
- iOS 11.3+
- iPadOS 11.3+
- Mac Catalyst 13.0+
- macOS 10.13.4+
- tvOS 11.3+
- visionOS 1.0+

## Declaration

```swift
func temporaryResultStateBatch(commandBuffer: any MTLCommandBuffer, sourceImage: [MPSImage], sourceStates: [[MPSCNNConvolutionGradientState]]?, destinationImage: [MPSImage]) -> [MPSCNNConvolutionTransposeGradientState]?
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpscnnconvolutiontranspose/temporaryresultstatebatch(commandbuffer:sourceimage:sourcestates:destinationimage:))*