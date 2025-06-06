# CIBarcodeDescriptor

**Framework**: Core Image  
**Kind**: cl

An abstract base class that represents a machine-readable code's attributes.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
class CIBarcodeDescriptor : NSObject
```

#### Overview

Subclasses encapsulate the formal specification and fields specific to a code type.  Each subclass is sufficient to recreate the unique symbol exactly as seen or used with a custom parser.

```occ
- (CIImage*) imageFromBarcodeDescriptor:(CIBarcodeDescriptor*)descriptor
{
    NSDictionary* inputParams = @{
                                  @"inputBarcodeDescriptor" : descriptor
                                  };
    CIFilter* barcodeCreationFilter = [CIFilter filterWithName:@"CIBarcodeGenerator" withInputParameters:inputParams];
    CIImage* outputImage = barcodeCreationFilter.outputImage;
    return outputImage;
}
```

## Relationships

### Inherits From
- [NSObject](../objectivec/nsobject-swift.class.md)
### Conforms To
- [NSCopying](../foundation/nscopying.md)
- [NSSecureCoding](../foundation/nssecurecoding.md)

## See Also

- [class CIQRCodeDescriptor](ciqrcodedescriptor.md)
  A concrete subclass of [`CIBarcodeDescriptor`](cibarcodedescriptor.md) that represents a square QR code symbol.
- [class CIAztecCodeDescriptor](ciazteccodedescriptor.md)
  A concrete subclass of [`CIBarcodeDescriptor`](cibarcodedescriptor.md) that represents an Aztec code symbol.
- [class CIPDF417CodeDescriptor](cipdf417codedescriptor.md)
  A concrete subclass of [`CIBarcodeDescriptor`](cibarcodedescriptor.md) that represents a PDF417 symbol.
- [class CIDataMatrixCodeDescriptor](cidatamatrixcodedescriptor.md)
  A concrete subclass of [`CIBarcodeDescriptor`](cibarcodedescriptor.md) that represents a Data Matrix code symbol.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cibarcodedescriptor)*