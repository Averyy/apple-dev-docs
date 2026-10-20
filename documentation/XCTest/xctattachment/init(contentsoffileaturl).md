# init(contentsOfFileAtURL:)

**Framework**: XCTest  
**Kind**: init  
**Role**: Initializer

Creates an attachment from the contents of an existing file on disk.

## Declaration

```swift
convenience init(contentsOfFileAtURL url: URL)
```

#### Discussion

The attachment’s [`name`](./name.md) property is the file name of the provided url. The attachment’s [`uniformTypeIdentifier`](./uniformtypeidentifier.md) value is inferred from the file’s extension. A default UTI of `"public.data"` is used for files without an extension.

> **Note**:  Use this initializer with files only. To create an attachment from a directory, use [`init(compressedContentsOfDirectoryAtURL:)`](./init%28compressedcontentsofdirectoryaturl%29.md).

## Parameters

- `url`: The file URL from which data should be read to create the new attachment.

## See Also

### Creating Attachments from Files and Folders
- [convenience init(contentsOfFileAtURL: URL, uniformTypeIdentifier: String)](./init%28contentsoffileaturl,uniformtypeidentifier%29.md)
  Creates an attachment from the contents of an existing file on disk, with a custom UTI.
- [convenience init(compressedContentsOfDirectoryAtURL: URL)](./init%28compressedcontentsofdirectoryaturl%29.md)
  Creates an attachment containing a zipped archive of an existing directory on disk.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xctest/xctattachment/init(contentsoffileaturl:))*