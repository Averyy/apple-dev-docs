# encodeBatch(commandBuffer:sourceImages:destinationStates:destinationStateIsTemporary:)

**Framework**: Metal Performance Shaders  
**Kind**: method

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
func encodeBatch(commandBuffer: any MTLCommandBuffer, sourceImages sourceImageBatches: [[MPSImage]], destinationStates outState: AutoreleasingUnsafeMutablePointer<NSArray?>, destinationStateIsTemporary isTemporary: Bool) -> [MPSImage]
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpscnnmultiarykernel/encodebatch(commandbuffer:sourceimages:destinationstates:destinationstateistemporary:))*