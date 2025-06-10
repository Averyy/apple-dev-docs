# CIDataMatrixCodeDescriptor

**Framework**: Core Image  
**Kind**: class

A Data Matrix code symbol.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
class CIDataMatrixCodeDescriptor
```

#### Overview

A concrete subclass of [`CIBarcodeDescriptor`](cibarcodedescriptor.md) that represents a Data Matrix code symbol.

Data Matrix codes are two-dimensional barcodes comprising black and white cells arranged in a square or rectangular matrix pattern.  They can encode text or numeric data.

## Topics

### Creating a Descriptor
- [init?(payload: Data, rowCount: Int, columnCount: Int, eccVersion: CIDataMatrixCodeDescriptor.ECCVersion)](cidatamatrixcodedescriptor/init(payload:rowcount:columncount:eccversion:).md)
  Initializes a descriptor that can be used as input to the `CIBarcodeGenerator` filter.
### Examining a Descriptor
- [var errorCorrectedPayload: Data](cidatamatrixcodedescriptor/errorcorrectedpayload-swift.property.md)
  The error-corrected payload that comprises the Data Matrix code symbol.
- [var rowCount: Int](cidatamatrixcodedescriptor/rowcount-swift.property.md)
  The number of module rows.
- [var columnCount: Int](cidatamatrixcodedescriptor/columncount-swift.property.md)
  The number of module columns.
- [var eccVersion: CIDataMatrixCodeDescriptor.ECCVersion](cidatamatrixcodedescriptor/eccversion-swift.property.md)
  The Data Matrix code ECC version.
### Error Correction Constants
- [CIDataMatrixCodeDescriptor.ECCVersion](cidatamatrixcodedescriptor/eccversion-swift.enum.md)
  Constants concerning Data Matrix code ECC version.

## Relationships

### Inherits From
- [CIBarcodeDescriptor](cibarcodedescriptor.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSSecureCoding](../Foundation/NSSecureCoding.md)

## See Also

- [class CIBarcodeDescriptor](cibarcodedescriptor.md)
  An abstract base class that represents a machine-readable code’s attributes.
- [class CIQRCodeDescriptor](ciqrcodedescriptor.md)
  A square QR code symbol.
- [class CIAztecCodeDescriptor](ciazteccodedescriptor.md)
  An Aztec code symbol.
- [class CIPDF417CodeDescriptor](cipdf417codedescriptor.md)
  A PDF417 symbol.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cidatamatrixcodedescriptor)*