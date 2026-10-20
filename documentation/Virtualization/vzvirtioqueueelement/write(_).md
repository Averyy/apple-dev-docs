# write(_:)

**Framework**: Virtualization  
**Kind**: method  
**Role**: Instance Method

Writes the memory represented by the data object you provide into the write buffers.

**Availability**:
- macOS 27.0+

## Declaration

```swift
func write(_ data: Data) throws
```

```objc
- (BOOL) writeData:(NSData *) data error:(NSError **) error;
```

## Parameters

- `data`: The [`NSData`](../../Foundation/nsdata.md) object that represents the memory the framework uses to the write buffers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/virtualization/vzvirtioqueueelement/write(_:))*