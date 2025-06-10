# init(contentsOfFileAtURL:uniformTypeIdentifier:)

**Framework**: XCTest  
**Kind**: init

Creates an attachment from the contents of an existing file on disk, with a custom UTI.

## Declaration

```swift
convenience init(contentsOfFile url: URL, uniformTypeIdentifier identifier: String)
```

#### Discussion

The attachment’s [`name`](xctattachment/name.md) property is the file name of the provided url.

> **Note**:  Use this initializer with files only. To create an attachment from a directory, use [`init(compressedContentsOfDirectoryAtURL:)`](xctattachment/init(compressedcontentsofdirectoryaturl:).md).

## Parameters

- `url`: The file URL from which data should be read to create the new attachment.
- `identifier`: A custom UTI to represent the file’s content type.

## See Also

- [convenience init(contentsOfFileAtURL: URL)](xctattachment/init(contentsoffileaturl:).md)
  Creates an attachment from the contents of an existing file on disk.
- [convenience init(compressedContentsOfDirectoryAtURL: URL)](xctattachment/init(compressedcontentsofdirectoryaturl:).md)
  Creates an attachment containing a zipped archive of an existing directory on disk.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xctest/xctattachment/init(contentsoffileaturl:uniformtypeidentifier:))*