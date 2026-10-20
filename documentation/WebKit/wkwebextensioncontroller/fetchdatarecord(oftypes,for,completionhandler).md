# fetchDataRecord(ofTypes:for:completionHandler:)

**Framework**: WebKit  
**Kind**: method  
**Role**: Instance Method

Fetches a data record containing the given extension data types for a specific known web extension context.

**Availability**:
- iOS 18.4+
- iPadOS 18.4+
- Mac Catalyst 18.4+
- macOS 15.4+
- visionOS 2.4+

## Declaration

```swift
func fetchDataRecord(ofTypes dataTypes: Set<WKWebExtension.DataType>, for extensionContext: WKWebExtensionContext, completionHandler: @escaping (WKWebExtension.DataRecord?) -> Void)
```

```swift
func dataRecord(ofTypes dataTypes: Set<WKWebExtension.DataType>, for extensionContext: WKWebExtensionContext) async -> WKWebExtension.DataRecord?
```

```objc
- (void) fetchDataRecordOfTypes:(NSSet<NSString *> *) dataTypes forExtensionContext:(WKWebExtensionContext *) extensionContext completionHandler:(void (^)(WKWebExtensionDataRecord *)) completionHandler;
```

#### Discussion

> **Note**: The extension does not need to be loaded to be included in the result.

## Parameters

- `dataTypes`: The extension data types to fetch records for.
- `extensionContext`: The specific web extension context to fetch records for.
- `completionHandler`: A block to invoke when the data record has been fetched.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkwebextensioncontroller/fetchdatarecord(oftypes:for:completionhandler:))*