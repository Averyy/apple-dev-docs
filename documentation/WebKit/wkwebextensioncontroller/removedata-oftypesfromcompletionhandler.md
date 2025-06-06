# removeData(ofTypes:from:completionHandler:)

**Framework**: Webkit  
**Kind**: method

Removes extension data of the given types for the given data records.

**Availability**:
- iOS 18.4+
- iPadOS 18.4+
- Mac Catalyst 18.4+
- macOS 15.4+
- visionOS 2.4+

## Declaration

```swift
@MainActor
func removeData(ofTypes dataTypes: Set<WKWebExtension.DataType>, from dataRecords: [WKWebExtension.DataRecord]) async
```

## Parameters

- `dataTypes`: The extension data types that should be removed.
- `dataRecords`: The extension data records to delete data from.
- `completionHandler`: A block to invoke when the data has been removed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkwebextensioncontroller/removedata(oftypes:from:completionhandler:))*