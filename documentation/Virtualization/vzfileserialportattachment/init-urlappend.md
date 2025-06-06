# init(url:append:)

**Framework**: Virtualization  
**Kind**: init

Creates a file-based serial port attachment object.

**Availability**:
- macOS 11.0+

## Declaration

```swift
init(url: URL, append shouldAppend: Bool) throws
```

#### Return Value

A file-based serial port attachment on success, or `nil` if initialization failed.

## Parameters

- `url`: The URL of a file on the local file system. The specified file must be writable by the virtual machine.
- `shouldAppend`: A Boolean that indicates whether the virtual machine opens the file in append mode. Specify   to append data to the file, and specify   to replace the contents of the file with any new data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/virtualization/vzfileserialportattachment/init(url:append:))*