# init(compressedContentsOfDirectory:)

**Framework**: XCTest  
**Kind**: init  
**Role**: Initializer

## Declaration

```swift
convenience init(compressedContentsOfDirectory url: URL)
```

```objc
+ (instancetype) attachmentWithCompressedContentsOfDirectoryAtURL:(NSURL *) url;
```

## Discussion

Creates an attachment with an existing directory on disk. Automatically zips the directory, the content type is “public.zip-archive”.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xctest/xctattachment/init(compressedcontentsofdirectory:))*