# columnCount

**Framework**: Core Image  
**Kind**: property

The number of columns in the PDF417 code symbol.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
var columnCount: Int { get }
```

#### Discussion

Valid column count values are from 1 to 30. This count excluded the columns used to indicate the symbol structure.

## See Also

- [var errorCorrectedPayload: Data](cipdf417codedescriptor/errorcorrectedpayload-swift.property.md)
  The error-corrected payload containing the data encoded in the PDF417 code symbol.
- [var isCompact: Bool](cipdf417codedescriptor/iscompact-swift.property.md)
  A boolean value telling if the PDF417 code is compact.
- [var rowCount: Int](cipdf417codedescriptor/rowcount-swift.property.md)
  The number of rows in the PDF417 code symbol.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cipdf417codedescriptor/columncount-swift.property)*