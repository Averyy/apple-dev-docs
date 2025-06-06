# CIAztecCodeDescriptor

**Framework**: Core Image  
**Kind**: cl

A concrete subclass of [`CIBarcodeDescriptor`](cibarcodedescriptor.md) that represents an Aztec code symbol.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
class CIAztecCodeDescriptor : CIBarcodeDescriptor
```

#### Overview

Aztec code is a format of 2D barcode published as ISO/IEC 24778:2008 standard.  It encodes data in concentric square rings around a central bullseye pattern.

## Topics

### Creating a Descriptor
- [init?(payload: Data, isCompact: Bool, layerCount: Int, dataCodewordCount: Int)](ciazteccodedescriptor/2875188-init.md)
  Initializes a descriptor that can be used as input to the `CIBarcodeGenerator` filter.
### Examining a Descriptor
- [var errorCorrectedPayload: Data](ciazteccodedescriptor/2875187-errorcorrectedpayload.md)
  The error-corrected payload containing the data encoded in the Aztec code.
- [var isCompact: Bool](ciazteccodedescriptor/2875203-iscompact.md)
  A Boolean value telling if the Aztec code is compact.
- [var layerCount: Int](ciazteccodedescriptor/2875174-layercount.md)
  The number of layers embedded in the Aztec code.
- [var dataCodewordCount: Int](ciazteccodedescriptor/2875166-datacodewordcount.md)
  The number of data codewords in the Aztec code.

## Relationships

### Inherits From
- [CIBarcodeDescriptor](cibarcodedescriptor.md)

## See Also

- [class CIBarcodeDescriptor](cibarcodedescriptor.md)
  An abstract base class that represents a machine-readable code's attributes.
- [class CIQRCodeDescriptor](ciqrcodedescriptor.md)
  A concrete subclass of [`CIBarcodeDescriptor`](cibarcodedescriptor.md) that represents a square QR code symbol.
- [class CIPDF417CodeDescriptor](cipdf417codedescriptor.md)
  A concrete subclass of [`CIBarcodeDescriptor`](cibarcodedescriptor.md) that represents a PDF417 symbol.
- [class CIDataMatrixCodeDescriptor](cidatamatrixcodedescriptor.md)
  A concrete subclass of [`CIBarcodeDescriptor`](cibarcodedescriptor.md) that represents a Data Matrix code symbol.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/ciazteccodedescriptor)*