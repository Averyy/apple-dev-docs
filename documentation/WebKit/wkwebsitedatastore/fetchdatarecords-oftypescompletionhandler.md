# fetchDataRecords(ofTypes:completionHandler:)

**Framework**: Webkit  
**Kind**: method

Fetches the specified types of records from the data store.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func dataRecords(ofTypes dataTypes: Set<String>) async -> [WKWebsiteDataRecord]
```

#### Discussion

Call this method to retrieve information about the types of data that the website saves. The returned records don’t include the data itself, but contain information that you can convey to the user. For example, you might use the returned data records to display the cookies a website uses, or to show which websites cache data.

## Parameters

- `dataTypes`: The types of records to fetch. For a list of all possible types, see  . To specify all types, specify the set returned by the   method.
- `completionHandler`: The completion handler block to execute asynchronously with the results. This block has no return value and takes the following parameter:

## See Also

- [class func allWebsiteDataTypes() -> Set<String>](wkwebsitedatastore/allwebsitedatatypes.md)
  Returns the set of all the available data types.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkwebsitedatastore/fetchdatarecords(oftypes:completionhandler:))*