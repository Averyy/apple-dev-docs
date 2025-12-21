# fetchAllDataStoreIdentifiers(_:)

**Framework**: WebKit  
**Kind**: method

Fetches an array of identifiers from existing data stores that have identifiers.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
class var allDataStoreIdentifiers: [UUID] { get async }
```

## Parameters

- `completionHandler`: A block to invoke with the fetched list of unique identifiers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkwebsitedatastore/fetchalldatastoreidentifiers(_:))*