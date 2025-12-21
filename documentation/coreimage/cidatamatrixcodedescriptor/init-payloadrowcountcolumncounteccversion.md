# init(payload:rowCount:columnCount:eccVersion:)

**Framework**: Core Image  
**Kind**: init

Initializes a Data Matrix code descriptor for the given payload and parameters.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
init?(payload errorCorrectedPayload: Data, rowCount: Int, columnCount: Int, eccVersion: CIDataMatrixCodeDescriptor.ECCVersion)
```

#### Return Value

 An initialized [`CIAztecCodeDescriptor`](ciazteccodedescriptor.md) instance or `nil` if the parameters are invalid

## Parameters

- `errorCorrectedPayload`: The data to encode in the Data Matrix code symbol.
- `rowCount`: The number of rows in the Data Matrix code symbol.
- `columnCount`: The number of columns in the Data Matrix code symbol.
- `eccVersion`: The   for the Data Matrix code symbol.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cidatamatrixcodedescriptor/init(payload:rowcount:columncount:eccversion:))*