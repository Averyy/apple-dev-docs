# CIPDF417CodeDescriptor

**Framework**: Core Image  
**Kind**: class

A PDF417 symbol.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
class CIPDF417CodeDescriptor
```

#### Overview

A concrete subclass of [`CIBarcodeDescriptor`](cibarcodedescriptor.md) that represents a PDF417 symbol.

PDF417 is a stacked linear barcode symbol format used predominantly in transport, ID cards, and inventory management.  Each pattern in the code comprises 4 bars and spaces, 17 units long.

## Topics

### Creating a Descriptor
- [init?(payload: Data, isCompact: Bool, rowCount: Int, columnCount: Int)](cipdf417codedescriptor/init(payload:iscompact:rowcount:columncount:).md)
  Initializes a descriptor that can be used as input to the `CIBarcodeGenerator` filter.
### Examining a Descriptor
- [var errorCorrectedPayload: Data](cipdf417codedescriptor/errorcorrectedpayload-swift.property.md)
  The error-corrected payload containing the data encoded in the PDF417 code.
- [var isCompact: Bool](cipdf417codedescriptor/iscompact-swift.property.md)
  A boolean value telling if the PDF417 code is compact.
- [var rowCount: Int](cipdf417codedescriptor/rowcount-swift.property.md)
  The number of rows in the PDF417 code.
- [var columnCount: Int](cipdf417codedescriptor/columncount-swift.property.md)
  The number of columns in the PDF417 code.

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
- [class CIDataMatrixCodeDescriptor](cidatamatrixcodedescriptor.md)
  A Data Matrix code symbol.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cipdf417codedescriptor)*