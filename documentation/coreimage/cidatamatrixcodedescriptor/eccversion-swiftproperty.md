# eccVersion

**Framework**: Core Image  
**Kind**: property

The Data Matrix code ECC version.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
var eccVersion: CIDataMatrixCodeDescriptor.ECCVersion { get }
```

#### Discussion

Valid values are 000, 050, 080, 100, 140, and 200. Any symbol with an even number of rows and columns will be ECC 200.

## See Also

- [var errorCorrectedPayload: Data](cidatamatrixcodedescriptor/errorcorrectedpayload-swift.property.md)
  The error-corrected payload that comprises the Data Matrix code symbol.
- [var rowCount: Int](cidatamatrixcodedescriptor/rowcount-swift.property.md)
  The number of module rows.
- [var columnCount: Int](cidatamatrixcodedescriptor/columncount-swift.property.md)
  The number of module columns.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cidatamatrixcodedescriptor/eccversion-swift.property)*