# encode(commandBuffer:primaryImage:secondaryImage:destinationState:destinationStateIsTemporary:)

**Framework**: Metal Performance Shaders  
**Kind**: instm

**Availability**:
- iOS 11.3+
- iPadOS 11.3+
- Mac Catalyst 13.0+
- macOS 10.13.4+
- tvOS 11.3+
- visionOS 1.0+

## Declaration

```swift
func encode(commandBuffer: any MTLCommandBuffer, primaryImage: MPSImage, secondaryImage: MPSImage, destinationState outState: AutoreleasingUnsafeMutablePointer<MPSState?>, destinationStateIsTemporary isTemporary: Bool) -> MPSImage
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpscnnbinarykernel/2947936-encode)*