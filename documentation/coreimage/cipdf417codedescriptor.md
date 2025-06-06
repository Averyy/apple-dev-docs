# CIPDF417CodeDescriptor

**Framework**: Core Image  
**Kind**: cl

A concrete subclass of [`CIBarcodeDescriptor`](cibarcodedescriptor.md) that represents a PDF417 symbol.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
class CIPDF417CodeDescriptor : CIBarcodeDescriptor
```

#### Overview

PDF417 is a stacked linear barcode symbol format used predominantly in transport, ID cards, and inventory management.  Each pattern in the code comprises 4 bars and spaces, 17 units long.

## Topics

### Creating a Descriptor
- [init?(payload: Data, isCompact: Bool, rowCount: Int, columnCount: Int)](cipdf417codedescriptor/2875182-init.md)
  Initializes a descriptor that can be used as input to the `CIBarcodeGenerator` filter.
### Examining a Descriptor
- [var errorCorrectedPayload: Data](cipdf417codedescriptor/2875204-errorcorrectedpayload.md)
  The error-corrected payload containing the data encoded in the PDF417 code.
- [var isCompact: Bool](cipdf417codedescriptor/2875194-iscompact.md)
  A boolean value telling if the PDF417 code is compact.
- [var rowCount: Int](cipdf417codedescriptor/2875199-rowcount.md)
  The number of rows in the PDF417 code.
- [var columnCount: Int](cipdf417codedescriptor/2875171-columncount.md)
  The number of columns in the PDF417 code.

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
- [class CIDataMatrixCodeDescriptor](cidatamatrixcodedescriptor.md)
  A concrete subclass of [`CIBarcodeDescriptor`](cibarcodedescriptor.md) that represents a Data Matrix code symbol.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cipdf417codedescriptor)*