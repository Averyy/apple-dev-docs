# allWebsiteDataTypes()

**Framework**: Webkit  
**Kind**: method

Returns the set of all the available data types.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- visionOS 1.0+

## Declaration

```swift
@MainActor
class func allWebsiteDataTypes() -> Set<String>
```

#### Discussion

Potential values in the set are [`WKWebsiteDataRecord`](wkwebsitedatarecord.md) constants.

## See Also

- [func fetchDataRecords(ofTypes: Set<String>, completionHandler: ([WKWebsiteDataRecord]) -> Void)](wkwebsitedatastore/fetchdatarecords(oftypes:completionhandler:).md)
  Fetches the specified types of records from the data store.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkwebsitedatastore/allwebsitedatatypes())*