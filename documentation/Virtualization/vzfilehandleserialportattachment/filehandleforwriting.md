# fileHandleForWriting

**Framework**: Virtualization  
**Kind**: property

The file handle that the guest operating system uses to write data.

**Availability**:
- macOS 11.0+

## Declaration

```swift
var fileHandleForWriting: FileHandle? { get }
```

#### Discussion

When you want to receive data from the guest operating system, read data from the file handle in this property.

## See Also

- [var fileHandleForReading: FileHandle?](vzfilehandleserialportattachment/filehandleforreading.md)
  The file handle that the guest operating system uses to read data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/virtualization/vzfilehandleserialportattachment/filehandleforwriting)*