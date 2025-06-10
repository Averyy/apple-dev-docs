# sizeInBytes(ofTypes:)

**Framework**: WebKit  
**Kind**: method

Retrieves the size in bytes of the specific data types in this data record.

**Availability**:
- iOS 18.4+
- iPadOS 18.4+
- Mac Catalyst 18.4+
- macOS 15.4+
- visionOS 2.4+

## Declaration

```swift
@MainActor
func sizeInBytes(ofTypes dataTypes: Set<WKWebExtension.DataType>) -> Int
```

## Parameters

- `dataTypes`: The set of data types to measure the size for.

## See Also

- [var totalSizeInBytes: Int](wkwebextension/datarecord/totalsizeinbytes.md)
  The total size in bytes of all data types contained in this data record.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkwebextension/datarecord/sizeinbytes(oftypes:))*