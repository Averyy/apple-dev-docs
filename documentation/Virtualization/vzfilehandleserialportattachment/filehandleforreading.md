# fileHandleForReading

**Framework**: Virtualization  
**Kind**: property  
**Role**: Instance Property

The file handle that the guest operating system uses to read data.

**Availability**:
- macOS 11.0+

## Declaration

```swift
var fileHandleForReading: FileHandle? { get }
```

```objc
@property (strong, readonly, nullable) NSFileHandle * fileHandleForReading;
```

## Discussion

When you want to send data to the guest operating system, write data to the file handle in this property.

## See Also

### Getting the file handles
- [var fileHandleForWriting: FileHandle?](./filehandleforwriting.md)
  The file handle that the guest operating system uses to write data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/virtualization/vzfilehandleserialportattachment/filehandleforreading)*