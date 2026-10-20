# fetchDataRecords(ofTypes:completionHandler:)

**Framework**: WebKit  
**Kind**: method  
**Role**: Instance Method

Fetches data records containing the given extension data types for all known extensions.

**Availability**:
- iOS 18.4+
- iPadOS 18.4+
- Mac Catalyst 18.4+
- macOS 15.4+
- visionOS 2.4+

## Declaration

```swift
func fetchDataRecords(ofTypes dataTypes: Set<WKWebExtension.DataType>, completionHandler: @escaping ([WKWebExtension.DataRecord]) -> Void)
```

```swift
func dataRecords(ofTypes dataTypes: Set<WKWebExtension.DataType>) async -> [WKWebExtension.DataRecord]
```

```objc
- (void) fetchDataRecordsOfTypes:(NSSet<NSString *> *) dataTypes completionHandler:(void (^)(NSArray<WKWebExtensionDataRecord *> *)) completionHandler;
```

#### Discussion

> **Note**: The extension does not need to be loaded to be included in the result.

## Parameters

- `dataTypes`: The extension data types to fetch records for.
- `completionHandler`: A block to invoke when the data records have been fetched.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkwebextensioncontroller/fetchdatarecords(oftypes:completionhandler:))*