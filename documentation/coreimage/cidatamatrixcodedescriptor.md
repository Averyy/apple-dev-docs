# CIDataMatrixCodeDescriptor

**Framework**: Core Image  
**Kind**: cl

A concrete subclass of [`CIBarcodeDescriptor`](cibarcodedescriptor.md) that represents a Data Matrix code symbol.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
class CIDataMatrixCodeDescriptor : CIBarcodeDescriptor
```

#### Overview

Data Matrix codes are two-dimensional barcodes comprising black and white cells arranged in a square or rectangular matrix pattern.  They can encode text or numeric data.

## Topics

### Creating a Descriptor
- [init?(payload: Data, rowCount: Int, columnCount: Int, eccVersion: CIDataMatrixCodeDescriptor.ECCVersion)](cidatamatrixcodedescriptor/2875201-init.md)
  Initializes a descriptor that can be used as input to the `CIBarcodeGenerator` filter.
### Examining a Descriptor
- [var errorCorrectedPayload: Data](cidatamatrixcodedescriptor/2875173-errorcorrectedpayload.md)
  The error-corrected payload that comprises the Data Matrix code symbol.
- [var rowCount: Int](cidatamatrixcodedescriptor/2875200-rowcount.md)
  The number of module rows.
- [var columnCount: Int](cidatamatrixcodedescriptor/2875202-columncount.md)
  The number of module columns.
- [var eccVersion: CIDataMatrixCodeDescriptor.ECCVersion](cidatamatrixcodedescriptor/2875170-eccversion.md)
  The Data Matrix code ECC version.
### Error Correction Constants
- [enum CIDataMatrixCodeDescriptor.ECCVersion](cidatamatrixcodedescriptor/eccversion.md)
  Constants concerning Data Matrix code ECC version.

## Relationships

### Inherits From
- [CIBarcodeDescriptor](cibarcodedescriptor.md)

## See Also

- [class CIBarcodeDescriptor](cibarcodedescriptor.md)
  An abstract base class that represents a machine-readable code's attributes.
- [class CIQRCodeDescriptor](ciqrcodedescriptor.md)
  A concrete subclass of [`CIBarcodeDescriptor`](cibarcodedescriptor.md) that represents a square QR code symbol.
- [class CIAztecCodeDescriptor](ciazteccodedescriptor.md)
  A concrete subclass of [`CIBarcodeDescriptor`](cibarcodedescriptor.md) that represents an Aztec code symbol.
- [class CIPDF417CodeDescriptor](cipdf417codedescriptor.md)
  A concrete subclass of [`CIBarcodeDescriptor`](cibarcodedescriptor.md) that represents a PDF417 symbol.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cidatamatrixcodedescriptor)*