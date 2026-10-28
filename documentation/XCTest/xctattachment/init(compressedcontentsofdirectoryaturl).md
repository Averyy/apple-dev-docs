# init(compressedContentsOfDirectoryAtURL:)

**Framework**: XCTest  
**Kind**: init  
**Role**: Initializer

Creates an attachment containing a zipped archive of an existing directory on disk.

## Declaration

```swift
convenience init(compressedContentsOfDirectoryAtURL url: URL)
```

## Discussion

Zips the contents of the provided directory and wraps the compressed output in an attachment with a [`uniformTypeIdentifier`](./uniformtypeidentifier.md) of `"public.zip-archive"`. The attachment’s [`name`](./name.md) property is set to the name of the zipped directory followed by an extension of `".zip"`.

Available on macOS only.

## Parameters

- `url`: A file URL for a directory whose contents should be compressed.

## See Also

### Creating Attachments from Files and Folders
- [convenience init(contentsOfFileAtURL: URL)](./init%28contentsoffileaturl%29.md)
  Creates an attachment from the contents of an existing file on disk.
- [convenience init(contentsOfFileAtURL: URL, uniformTypeIdentifier: String)](./init%28contentsoffileaturl,uniformtypeidentifier%29.md)
  Creates an attachment from the contents of an existing file on disk, with a custom UTI.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xctest/xctattachment/init(compressedcontentsofdirectoryaturl:))*