# PMDataFormat

**Framework**: Application Services  
**Kind**: struct  
**Role**: Structure

Constants that specify the format of the data representation created with the functions [`PMPageFormatCreateDataRepresentation(_:_:_:)`](./api-1464227-pmpageformatcreatedatarepresenta.md) and [`PMPrintSettingsCreateDataRepresentation(_:_:_:)`](./api-1464570-pmprintsettingscreatedatareprese.md).

**Availability**:
- macOS 10.5+

## Declaration

```swift
struct PMDataFormat
```

```c
typedef enum PMDataFormat : unsigned int {
    ...
} PMDataFormat;
```

## Topics

### Constants
- [var kPMDataFormatXMLDefault: PMDataFormat](./kpmdataformatxmldefault.md)
- [var kPMDataFormatXMLMinimal: PMDataFormat](./kpmdataformatxmlminimal.md)
- [var kPMDataFormatXMLCompressed: PMDataFormat](./kpmdataformatxmlcompressed.md)
### Initializers
- [init(UInt32)](./pmdataformat/api-1462724-init.md)
- [init(rawValue: UInt32)](./pmdataformat/api-1459732-init.md)
### Instance Properties
- [var rawValue: UInt32](./pmdataformat/api-1459960-rawvalue.md)

## Relationships

### Conforms To
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/applicationservices/pmdataformat)*