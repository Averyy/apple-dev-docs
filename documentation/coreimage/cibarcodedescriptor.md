# CIBarcodeDescriptor

**Framework**: Core Image  
**Kind**: class

An abstract base class that represents a machine-readable code’s attributes.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
class CIBarcodeDescriptor
```

#### Overview

Subclasses encapsulate the formal specification and fields specific to a code type. Each subclass is sufficient to recreate the unique symbol exactly as seen or used with a custom parser.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Inherited By
- [CIAztecCodeDescriptor](ciazteccodedescriptor.md)
- [CIDataMatrixCodeDescriptor](cidatamatrixcodedescriptor.md)
- [CIPDF417CodeDescriptor](cipdf417codedescriptor.md)
- [CIQRCodeDescriptor](ciqrcodedescriptor.md)
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

- [class CIQRCodeDescriptor](ciqrcodedescriptor.md)
  A concrete subclass of the Core Image Barcode Descriptor that represents a square QR code symbol.
- [class CIAztecCodeDescriptor](ciazteccodedescriptor.md)
  A concrete subclass the Core Image Barcode Descriptor that represents an Aztec code symbol.
- [class CIPDF417CodeDescriptor](cipdf417codedescriptor.md)
  A concrete subclass of Core Image Barcode Descriptor that represents a PDF417 symbol.
- [class CIDataMatrixCodeDescriptor](cidatamatrixcodedescriptor.md)
  A concrete subclass the Core Image Barcode Descriptor that represents an Data Matrix code symbol.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cibarcodedescriptor)*