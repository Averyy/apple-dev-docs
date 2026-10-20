# SKIndexType

**Framework**: Core Services  
**Kind**: struct  
**Role**: Structure

Specifies the category of an index.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.3+

## Declaration

```swift
struct SKIndexType
```

```c
typedef enum SKIndexType : unsigned int {
    ...
} SKIndexType;
```

## Topics

### Constants
- [var kSKIndexUnknown: SKIndexType](./kskindexunknown.md)
  Specifies an unknown index type.
- [var kSKIndexInverted: SKIndexType](./kskindexinverted.md)
  Specifies an inverted index, mapping terms to documents.
- [var kSKIndexVector: SKIndexType](./kskindexvector.md)
  Specifies a vector index, mapping documents to terms.
- [var kSKIndexInvertedVector: SKIndexType](./kskindexinvertedvector.md)
  Specifies an index type with all the capabilities of an inverted and a vector index.
### Initializers
- [init(UInt32)](./skindextype/api-1443295-init.md)
- [init(rawValue: UInt32)](./skindextype/api-1442314-init.md)
### Instance Properties
- [var rawValue: UInt32](./skindextype/api-1450496-rawvalue.md)

## Relationships

### Conforms To
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/skindextype)*