# init(contentsOfFile:)

**Framework**: XCTest  
**Kind**: init

## Declaration

```swift
convenience init(contentsOfFile url: URL)
```

#### Discussion

Creates an attachment with an existing file on disk. Attachment’s uniform type identifier is inferred from the file extension. If no type can be inferred from the extension, fallback is “public.data”.

> **Note**: Only works for files, not directories.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xctest/xctattachment/init(contentsoffile:))*