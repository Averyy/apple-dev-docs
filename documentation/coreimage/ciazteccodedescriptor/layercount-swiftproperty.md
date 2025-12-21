# layerCount

**Framework**: Core Image  
**Kind**: property

The number of data layers in the Aztec code symbol.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
var layerCount: Int { get }
```

#### Discussion

Combined with [`isCompact`](ciazteccodedescriptor/iscompact-swift.property.md), the number of data layers determines the number of
modules in the Aztec Code symbol. Valid values range from 1 to 32. Compact symbols can have up to 4 data layers.

The number of data layers also determines the number of bits in each data codeword of the message carried by the Aztec Code symbol.

## See Also

- [var errorCorrectedPayload: Data](ciazteccodedescriptor/errorcorrectedpayload-swift.property.md)
  The error-corrected payload that comprises the the Aztec code symbol.
- [var isCompact: Bool](ciazteccodedescriptor/iscompact-swift.property.md)
  A Boolean value telling if the Aztec code is compact.
- [var dataCodewordCount: Int](ciazteccodedescriptor/datacodewordcount-swift.property.md)
  The number of non-error-correction codewords carried by the Aztec code symbol.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/ciazteccodedescriptor/layercount-swift.property)*