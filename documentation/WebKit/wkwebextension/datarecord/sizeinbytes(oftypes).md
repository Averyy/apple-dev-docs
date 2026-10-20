# sizeInBytes(ofTypes:)

**Framework**: WebKit  
**Kind**: method  
**Role**: Instance Method

Retrieves the size in bytes of the specific data types in this data record.

**Availability**:
- iOS 18.4+
- iPadOS 18.4+
- Mac Catalyst 18.4+
- macOS 15.4+
- visionOS 2.4+

## Declaration

```swift
func sizeInBytes(ofTypes dataTypes: Set<WKWebExtension.DataType>) -> Int
```

```objc
- (NSUInteger) sizeInBytesOfTypes:(NSSet<NSString *> *) dataTypes;
```

## Parameters

- `dataTypes`: The set of data types to measure the size for.

## See Also

### Related Documentation
- [var totalSizeInBytes: Int](./totalsizeinbytes.md)
  The total size in bytes of all data types contained in this data record.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkwebextension/datarecord/sizeinbytes(oftypes:))*