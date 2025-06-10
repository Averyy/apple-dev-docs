# errorCorrectedPayload

**Framework**: Core Image  
**Kind**: property

The error-corrected payload that comprises the Data Matrix code symbol.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
var errorCorrectedPayload: Data { get }
```

#### Discussion

The error-corrected payload contains the de-interleaved bits of the message.

Data Matrix symbols are specified by ISO/IEC 16022:2006(E).  ECC 200-type symbols will always have an even number of rows and columns.

## See Also

- [var rowCount: Int](cidatamatrixcodedescriptor/rowcount-swift.property.md)
  The number of module rows.
- [var columnCount: Int](cidatamatrixcodedescriptor/columncount-swift.property.md)
  The number of module columns.
- [var eccVersion: CIDataMatrixCodeDescriptor.ECCVersion](cidatamatrixcodedescriptor/eccversion-swift.property.md)
  The Data Matrix code ECC version.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cidatamatrixcodedescriptor/errorcorrectedpayload-swift.property)*