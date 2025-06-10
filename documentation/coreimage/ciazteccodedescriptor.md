# CIAztecCodeDescriptor

**Framework**: Core Image  
**Kind**: class

An Aztec code symbol.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
class CIAztecCodeDescriptor
```

#### Overview

A concrete subclass of [`CIBarcodeDescriptor`](cibarcodedescriptor.md) that represents an Aztec code symbol.

Aztec code is a format of 2D barcode published as ISO/IEC 24778:2008 standard.  It encodes data in concentric square rings around a central bullseye pattern.

## Topics

### Creating a Descriptor
- [init?(payload: Data, isCompact: Bool, layerCount: Int, dataCodewordCount: Int)](ciazteccodedescriptor/init(payload:iscompact:layercount:datacodewordcount:).md)
  Initializes a descriptor that can be used as input to the `CIBarcodeGenerator` filter.
### Examining a Descriptor
- [var errorCorrectedPayload: Data](ciazteccodedescriptor/errorcorrectedpayload-swift.property.md)
  The error-corrected payload containing the data encoded in the Aztec code.
- [var isCompact: Bool](ciazteccodedescriptor/iscompact-swift.property.md)
  A Boolean value telling if the Aztec code is compact.
- [var layerCount: Int](ciazteccodedescriptor/layercount-swift.property.md)
  The number of layers embedded in the Aztec code.
- [var dataCodewordCount: Int](ciazteccodedescriptor/datacodewordcount-swift.property.md)
  The number of data codewords in the Aztec code.

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
- [class CIPDF417CodeDescriptor](cipdf417codedescriptor.md)
  A PDF417 symbol.
- [class CIDataMatrixCodeDescriptor](cidatamatrixcodedescriptor.md)
  A Data Matrix code symbol.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/ciazteccodedescriptor)*