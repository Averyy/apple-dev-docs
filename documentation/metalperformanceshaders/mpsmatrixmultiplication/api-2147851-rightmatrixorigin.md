# rightMatrixOrigin

**Framework**: Metal Performance Shaders  
**Kind**: instp

The origin of the right input matrix.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.0+
- macOS 10.13+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
var rightMatrixOrigin: MTLOrigin { get set }
```

#### Discussion

The origin, relative to `(0,0)`, at which to start reading values. If a different origin is desired, you must modify this property before encoding the matrix multiplication kernel. The default value is `(0,0,0)` (the `z` value must always be 0).

## See Also

- [var leftMatrixOrigin: MTLOrigin](mpsmatrixmultiplication/2147846-leftmatrixorigin.md)
  The origin of the left input matrix.
- [var resultMatrixOrigin: MTLOrigin](mpsmatrixmultiplication/2147847-resultmatrixorigin.md)
  The origin of the result matrix.
- [var batchSize: Int](mpsmatrixmultiplication/2873082-batchsize.md)
- [var batchStart: Int](mpsmatrixmultiplication/2873081-batchstart.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpsmatrixmultiplication/2147851-rightmatrixorigin)*