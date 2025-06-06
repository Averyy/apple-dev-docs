# fetchDataRecords(ofTypes:completionHandler:)

**Framework**: Webkit  
**Kind**: method

Fetches data records containing the given extension data types for all known extensions.

**Availability**:
- iOS 18.4+
- iPadOS 18.4+
- Mac Catalyst 18.4+
- macOS 15.4+
- visionOS 2.4+

## Declaration

```swift
@MainActor
func dataRecords(ofTypes dataTypes: Set<WKWebExtension.DataType>) async -> [WKWebExtension.DataRecord]
```

#### Discussion

> **Note**: The extension does not need to be loaded to be included in the result.

The extension does not need to be loaded to be included in the result.

## Parameters

- `dataTypes`: The extension data types to fetch records for.
- `completionHandler`: A block to invoke when the data records have been fetched.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkwebextensioncontroller/fetchdatarecords(oftypes:completionhandler:))*