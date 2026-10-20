# readBytes(withExactLength:)

**Framework**: Virtualization  
**Kind**: method  
**Role**: Instance Method

Reads the number of bytes you specify from the read buffers and return result as a data object.

**Availability**:
- macOS 27.0+

## Declaration

```swift
func readBytes(withExactLength exactLength: Int) throws -> Data
```

```objc
- (NSData *) readBytesWithExactLength:(NSUInteger) exactLength error:(NSError **) error;
```

#### Return Value

An [`NSData`](../../Foundation/nsdata.md) object filled with the memory that the framework read, or `nil` if the read failed.

#### Discussion

Memory is copied into the newly allocated buffer represented by the returned NSData object.

## Parameters

- `exactLength`: Number of bytes to read from the read buffers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/virtualization/vzvirtioqueueelement/readbytes(withexactlength:))*