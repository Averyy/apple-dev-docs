# fileHandleForWriting

**Framework**: Virtualization  
**Kind**: property  
**Role**: Instance Property

The file handle that the guest operating system uses to write data.

**Availability**:
- macOS 11.0+

## Declaration

```swift
var fileHandleForWriting: FileHandle? { get }
```

```objc
@property (strong, readonly, nullable) NSFileHandle * fileHandleForWriting;
```

## Discussion

When you want to receive data from the guest operating system, read data from the file handle in this property.

## See Also

### Getting the file handles
- [var fileHandleForReading: FileHandle?](./filehandleforreading.md)
  The file handle that the guest operating system uses to read data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/virtualization/vzfilehandleserialportattachment/filehandleforwriting)*