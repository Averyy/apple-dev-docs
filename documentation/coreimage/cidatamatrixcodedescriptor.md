# CIDataMatrixCodeDescriptor

**Framework**: Core Image  
**Kind**: class

A concrete subclass the Core Image Barcode Descriptor that represents an Data Matrix code symbol.

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

A Data Matrix code symbol is a 2D barcode format defined by the ISO/IEC 16022:2006(E) standard. It encodes data in square or rectangular symbol with solid lines on the left and bottom sides

## Topics

### Creating a Descriptor
- [init?(payload: Data, rowCount: Int, columnCount: Int, eccVersion: CIDataMatrixCodeDescriptor.ECCVersion)](cidatamatrixcodedescriptor/init(payload:rowcount:columncount:eccversion:).md)
  Initializes a Data Matrix code descriptor for the given payload and parameters.
### Examining a Descriptor
- [var errorCorrectedPayload: Data](cidatamatrixcodedescriptor/errorcorrectedpayload-swift.property.md)
  The error-corrected payload containing the data encoded in the Data Matrix code symbol.
- [var rowCount: Int](cidatamatrixcodedescriptor/rowcount-swift.property.md)
  The number of rows in the Data Matrix code symbol.
- [var columnCount: Int](cidatamatrixcodedescriptor/columncount-swift.property.md)
  The number of columns in the Data Matrix code symbol.
- [var eccVersion: CIDataMatrixCodeDescriptor.ECCVersion](cidatamatrixcodedescriptor/eccversion-swift.property.md)
  The error correction version of the Data Matrix code symbol.
### Error Correction Constants
- [CIDataMatrixCodeDescriptor.ECCVersion](cidatamatrixcodedescriptor/eccversion-swift.enum.md)
  Constants indicating the Data Matrix code ECC version.

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
  A concrete subclass of the Core Image Barcode Descriptor that represents a square QR code symbol.
- [class CIAztecCodeDescriptor](ciazteccodedescriptor.md)
  A concrete subclass the Core Image Barcode Descriptor that represents an Aztec code symbol.
- [class CIPDF417CodeDescriptor](cipdf417codedescriptor.md)
  A concrete subclass of Core Image Barcode Descriptor that represents a PDF417 symbol.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cidatamatrixcodedescriptor)*