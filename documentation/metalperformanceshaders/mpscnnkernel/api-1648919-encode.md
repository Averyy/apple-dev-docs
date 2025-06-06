# encode(commandBuffer:sourceImage:destinationImage:)

**Framework**: Metal Performance Shaders  
**Kind**: instm

Encodes a kernel into a command buffer.  The ensuing operation proceeds out-of-place.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.0+
- macOS 10.13+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
func encode(commandBuffer: any MTLCommandBuffer, sourceImage: MPSImage, destinationImage: MPSImage)
```

#### Discussion

The `destinationImage` object may not alias the `sourceImage` object.

## Parameters

- `commandBuffer`: A valid command buffer to receive the encoded filter.
- `sourceImage`: A valid source image.
- `destinationImage`: A valid destination image to be overwritten by the results.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpscnnkernel/1648919-encode)*