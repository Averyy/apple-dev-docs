# CIQRCodeDescriptor

**Framework**: Core Image  
**Kind**: cl

A concrete subclass of [`CIBarcodeDescriptor`](cibarcodedescriptor.md) that represents a square QR code symbol.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
class CIQRCodeDescriptor : CIBarcodeDescriptor
```

#### Overview

 ISO/IEC 18004 defines versions from 1 to 40, where a higher symbol version indicates a larger data-carrying capacity.

QR codes can encode text, vCard contact information, or Uniform Resource Identifiers (URI).

## Topics

### Creating a Descriptor
- [init?(payload: Data, symbolVersion: Int, maskPattern: UInt8, errorCorrectionLevel: CIQRCodeDescriptor.ErrorCorrectionLevel)](ciqrcodedescriptor/2875180-init.md)
  Initializes a descriptor that can be used as input to the `CIBarcodeGenerator` filter.
### Examining a Descriptor
- [var errorCorrectedPayload: Data](ciqrcodedescriptor/2875167-errorcorrectedpayload.md)
  The error-corrected payload containing the data encoded in the QR code.
- [var symbolVersion: Int](ciqrcodedescriptor/2875193-symbolversion.md)
  The version of the QR code.
- [var maskPattern: UInt8](ciqrcodedescriptor/2875191-maskpattern.md)
  The QR code's mask pattern.
- [var errorCorrectionLevel: CIQRCodeDescriptor.ErrorCorrectionLevel](ciqrcodedescriptor/2875196-errorcorrectionlevel.md)
  The QR code error correction level.
### Error Correction Constants
- [enum CIQRCodeDescriptor.ErrorCorrectionLevel](ciqrcodedescriptor/errorcorrectionlevel.md)
  Constants that indicate the percentage of the symbol dedicated to error correction.

## Relationships

### Inherits From
- [CIBarcodeDescriptor](cibarcodedescriptor.md)

## See Also

- [class CIBarcodeDescriptor](cibarcodedescriptor.md)
  An abstract base class that represents a machine-readable code's attributes.
- [class CIAztecCodeDescriptor](ciazteccodedescriptor.md)
  A concrete subclass of [`CIBarcodeDescriptor`](cibarcodedescriptor.md) that represents an Aztec code symbol.
- [class CIPDF417CodeDescriptor](cipdf417codedescriptor.md)
  A concrete subclass of [`CIBarcodeDescriptor`](cibarcodedescriptor.md) that represents a PDF417 symbol.
- [class CIDataMatrixCodeDescriptor](cidatamatrixcodedescriptor.md)
  A concrete subclass of [`CIBarcodeDescriptor`](cibarcodedescriptor.md) that represents a Data Matrix code symbol.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/ciqrcodedescriptor)*