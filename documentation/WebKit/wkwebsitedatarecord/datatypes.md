# dataTypes

**Framework**: WebKit  
**Kind**: property

The types of data associated with the record.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var dataTypes: Set<String> { get }
```

#### Discussion

Each record contains the set of types that the associated website stores. For a list of possible types, see [`Data Store Record Types`](data-store-record-types.md).

## See Also

- [Data Store Record Types](data-store-record-types.md)
  Explore the constants that identify the types of data that websites store.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkwebsitedatarecord/datatypes)*