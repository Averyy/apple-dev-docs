# fileHandleForReading

**Framework**: Virtualization  
**Kind**: property

The file handle that the guest operating system uses to read data.

**Availability**:
- macOS 11.0+

## Declaration

```swift
var fileHandleForReading: FileHandle? { get }
```

#### Discussion

When you want to send data to the guest operating system, write data to the file handle in this property.

## See Also

- [var fileHandleForWriting: FileHandle?](vzfilehandleserialportattachment/filehandleforwriting.md)
  The file handle that the guest operating system uses to write data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/virtualization/vzfilehandleserialportattachment/filehandleforreading)*