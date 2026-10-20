# init(url:append:)

**Framework**: Virtualization  
**Kind**: init  
**Role**: Initializer

Creates a file-based serial port attachment object.

**Availability**:
- macOS 11.0+

## Declaration

```swift
init(url: URL, append shouldAppend: Bool) throws
```

```objc
- (instancetype) initWithURL:(NSURL *) url append:(BOOL) shouldAppend error:(NSError **) error;
```

#### Return Value

A file-based serial port attachment on success, or `nil` if initialization failed.

## Parameters

- `url`: The URL of a file on the local file system. The specified file must be writable by the virtual machine.
- `shouldAppend`: A Boolean that indicates whether the virtual machine opens the file in append mode. Specify [`true`](../../Swift/true.md) to append data to the file, and specify [`false`](../../Swift/false.md) to replace the contents of the file with any new data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/virtualization/vzfileserialportattachment/init(url:append:)-37g72)*