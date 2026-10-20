# init(fileHandle:)

**Framework**: Virtualization  
**Kind**: init  
**Role**: Initializer

Creates the attachment from a file handle that contains a connected datagram socket.

**Availability**:
- macOS 11.0+

## Declaration

```swift
init(fileHandle: FileHandle)
```

```objc
- (instancetype) initWithFileHandle:(NSFileHandle *) fileHandle;
```

#### Return Value

An attachment object for the specified file handle.

## Parameters

- `fileHandle`: A file handle to a connected datagram socket.


---

*[View on Apple Developer](https://developer.apple.com/documentation/virtualization/vzfilehandlenetworkdeviceattachment/init(filehandle:))*