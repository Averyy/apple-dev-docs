# encode(commandBuffer:leftMatrix:rightMatrix:resultMatrix:)

**Framework**: Metal Performance Shaders  
**Kind**: instm

Encodes a matrix multiplication kernel to a command buffer.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.0+
- macOS 10.13+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
func encode(commandBuffer: any MTLCommandBuffer, leftMatrix: MPSMatrix, rightMatrix: MPSMatrix, resultMatrix: MPSMatrix)
```

#### Discussion

The following constraints apply to the sizes of the matrices depending on the transposition operations and the sizes requested at initialization time, as well as the origins at the time this method is called:

- The left input matrix must be large enough to hold an array of size `resultRows x interiorColumns` elements, beginning at the value of the [`leftMatrixOrigin`](mpsmatrixmultiplication/2147846-leftmatrixorigin.md) property.
- The right input matrix must be large enough to hold an array of size `interiorColumns x resultColumns` elements, beginning at the value of the [`rightMatrixOrigin`](mpsmatrixmultiplication/2147851-rightmatrixorigin.md) property.
- The result matrix must be large enough to hold an array of size `resultRows x resultColumns` elements, beginning at the value of the [`resultMatrixOrigin`](mpsmatrixmultiplication/2147847-resultmatrixorigin.md) property.

## Parameters

- `commandBuffer`: The command buffer that will receive the encoded kernel.
- `leftMatrix`: The left input matrix.
- `rightMatrix`: The right input matrix.
- `resultMatrix`: The addend matrix which will also be overwritten by the operation result.

## See Also

- [init(device: any MTLDevice, transposeLeft: Bool, transposeRight: Bool, resultRows: Int, resultColumns: Int, interiorColumns: Int, alpha: Double, beta: Double)](mpsmatrixmultiplication/2147845-init.md)
  Initializes a matrix multiplication kernel.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpsmatrixmultiplication/2147848-encode)*