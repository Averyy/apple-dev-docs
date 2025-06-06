# removeData(ofTypes:for:completionHandler:)

**Framework**: Webkit  
**Kind**: method

Removes the specified types of website data from one or more data records.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func removeData(ofTypes dataTypes: Set<String>, for dataRecords: [WKWebsiteDataRecord]) async
```

#### Discussion

> **Note**:  You can call this method from synchronous code using a completion handler, as shown on this page, or you can call it as an asynchronous method that has the following declaration: ```swift
func removeData(ofTypes dataTypes: Set<String>, for dataRecords: [WKWebsiteDataRecord]) async
``` For information about concurrency and asynchronous code in Swift, see [`Calling Objective-C APIs Asynchronously`](https://developer.apple.com/documentation/Swift/calling-objective-c-apis-asynchronously).

 You can call this method from synchronous code using a completion handler, as shown on this page, or you can call it as an asynchronous method that has the following declaration:

```swift
func removeData(ofTypes dataTypes: Set<String>, for dataRecords: [WKWebsiteDataRecord]) async
```

For information about concurrency and asynchronous code in Swift, see [`Calling Objective-C APIs Asynchronously`](https://developer.apple.com/documentation/Swift/calling-objective-c-apis-asynchronously).

## Parameters

- `dataTypes`: The website data types to remove from the records.
- `dataRecords`: The records that contain the data.
- `completionHandler`: The completion handler block to execute asynchronously after the web view removes the specified data. This block has no return value and takes no parameters.

## See Also

- [func removeData(ofTypes: Set<String>, modifiedSince: Date, completionHandler: () -> Void)](wkwebsitedatastore/removedata(oftypes:modifiedsince:completionhandler:).md)
  Removes website data that changed after the specified date.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkwebsitedatastore/removedata(oftypes:for:completionhandler:))*