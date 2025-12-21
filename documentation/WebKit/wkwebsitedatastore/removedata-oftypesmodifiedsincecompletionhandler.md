# removeData(ofTypes:modifiedSince:completionHandler:)

**Framework**: WebKit  
**Kind**: method

Removes website data that changed after the specified date.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func removeData(ofTypes dataTypes: Set<String>, modifiedSince date: Date, completionHandler: @escaping () -> Void)
```

#### Discussion

This method removes the specified data type from all records, but only if a website modified the record’s data after the specified `date`.

## Parameters

- `dataTypes`: The website data types to remove.
- `date`: The target date for the data removal. The data store removes data that a website changed after this date.
- `completionHandler`: The completion handler block to execute asynchronously after the web view removes the specified data. This block has no return value and takes no parameters.

## See Also

- [func removeData(ofTypes: Set<String>, for: [WKWebsiteDataRecord], completionHandler: () -> Void)](wkwebsitedatastore/removedata(oftypes:for:completionhandler:).md)
  Removes the specified types of website data from one or more data records.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkwebsitedatastore/removedata(oftypes:modifiedsince:completionhandler:))*