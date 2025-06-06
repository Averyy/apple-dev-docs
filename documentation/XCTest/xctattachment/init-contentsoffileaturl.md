# init(contentsOfFileAtURL:)

**Framework**: Xctest  
**Kind**: init

Creates an attachment from the contents of an existing file on disk.

## Declaration

```swift
convenience init(contentsOfFile url: URL)
```

#### Discussion

The attachment’s [`name`](xctattachment/name.md) property is the file name of the provided url. The attachment’s [`uniformTypeIdentifier`](xctattachment/uniformtypeidentifier.md) value is inferred from the file’s extension. A default UTI of `"public.data"` is used for files without an extension.

> **Note**:  Use this initializer with files only. To create an attachment from a directory, use [`init(compressedContentsOfDirectoryAtURL:)`](xctattachment/init(compressedcontentsofdirectoryaturl:).md).

 Use this initializer with files only. To create an attachment from a directory, use [`init(compressedContentsOfDirectoryAtURL:)`](xctattachment/init(compressedcontentsofdirectoryaturl:).md).

## Parameters

- `url`: The file URL from which data should be read to create the new attachment.

## See Also

- [convenience init(contentsOfFileAtURL: URL, uniformTypeIdentifier: String)](xctattachment/init(contentsoffileaturl:uniformtypeidentifier:).md)
  Creates an attachment from the contents of an existing file on disk, with a custom UTI.
- [convenience init(compressedContentsOfDirectoryAtURL: URL)](xctattachment/init(compressedcontentsofdirectoryaturl:).md)
  Creates an attachment containing a zipped archive of an existing directory on disk.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xctest/xctattachment/init(contentsoffileaturl:))*