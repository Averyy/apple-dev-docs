# allWebsiteDataTypes()

**Framework**: WebKit  
**Kind**: method  
**Role**: Type Method

Returns the set of all the available data types.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- visionOS 1.0+

## Declaration

```swift
class func allWebsiteDataTypes() -> Set<String>
```

```objc
+ (NSSet<NSString *> *) allWebsiteDataTypes;
```

#### Discussion

Potential values in the set are [`WKWebsiteDataRecord`](../wkwebsitedatarecord.md) constants.

## See Also

### Retrieving specific types of data
- [func fetchDataRecords(ofTypes: Set<String>, completionHandler: ([WKWebsiteDataRecord]) -> Void)](./fetchdatarecords%28oftypes,completionhandler%29.md)
  Fetches the specified types of records from the data store.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkwebsitedatastore/allwebsitedatatypes())*