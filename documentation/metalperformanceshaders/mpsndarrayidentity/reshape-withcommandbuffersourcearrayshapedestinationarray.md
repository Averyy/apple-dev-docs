# reshape(with:commandBuffer:sourceArray:shape:destinationArray:)

**Framework**: Metal Performance Shaders  
**Kind**: method

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+

## Declaration

```swift
func reshape(with encoder: (any MTLComputeCommandEncoder)?, commandBuffer cmdBuf: (any MTLCommandBuffer)?, sourceArray: MPSNDArray, shape: [NSNumber], destinationArray: MPSNDArray?) -> MPSNDArray?
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpsndarrayidentity/reshape(with:commandbuffer:sourcearray:shape:destinationarray:))*