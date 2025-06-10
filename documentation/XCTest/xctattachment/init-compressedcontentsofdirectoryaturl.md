# init(compressedContentsOfDirectoryAtURL:)

**Framework**: XCTest  
**Kind**: init

Creates an attachment containing a zipped archive of an existing directory on disk.

## Declaration

```swift
convenience init(compressedContentsOfDirectory url: URL)
```

#### Discussion

Zips the contents of the provided directory and wraps the compressed output in an attachment with a [`uniformTypeIdentifier`](xctattachment/uniformtypeidentifier.md) of `"public.zip-archive"`. The attachment’s [`name`](xctattachment/name.md) property is set to the name of the zipped directory followed by an extension of `".zip"`.

Available on macOS only.

## Parameters

- `url`: A file URL for a directory whose contents should be compressed.

## See Also

- [convenience init(contentsOfFileAtURL: URL)](xctattachment/init(contentsoffileaturl:).md)
  Creates an attachment from the contents of an existing file on disk.
- [convenience init(contentsOfFileAtURL: URL, uniformTypeIdentifier: String)](xctattachment/init(contentsoffileaturl:uniformtypeidentifier:).md)
  Creates an attachment from the contents of an existing file on disk, with a custom UTI.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xctest/xctattachment/init(compressedcontentsofdirectoryaturl:))*