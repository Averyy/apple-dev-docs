# removeData(ofTypes:for:completionHandler:)

**Framework**: WebKit  
**Kind**: method  
**Role**: Instance Method

Removes the specified types of website data from one or more data records.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- visionOS 1.0+

## Declaration

```swift
func removeData(ofTypes dataTypes: Set<String>, for dataRecords: [WKWebsiteDataRecord], completionHandler: @escaping @MainActor @Sendable () -> Void)
```

```swift
func removeData(ofTypes dataTypes: Set<String>, for dataRecords: [WKWebsiteDataRecord]) async
```

```objc
- (void) removeDataOfTypes:(NSSet<NSString *> *) dataTypes forDataRecords:(NSArray<WKWebsiteDataRecord *> *) dataRecords completionHandler:(void (^)(void)) completionHandler;
```

## Parameters

- `dataTypes`: The website data types to remove from the records.
- `dataRecords`: The records that contain the data.
- `completionHandler`: The completion handler block to execute asynchronously after the web view removes the specified data. This block has no return value and takes no parameters.

## See Also

### Removing specific types of data
- [func removeData(ofTypes: Set<String>, modifiedSince: Date, completionHandler: () -> Void)](./removedata%28oftypes,modifiedsince,completionhandler%29.md)
  Removes website data that changed after the specified date.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkwebsitedatastore/removedata(oftypes:for:completionhandler:))*