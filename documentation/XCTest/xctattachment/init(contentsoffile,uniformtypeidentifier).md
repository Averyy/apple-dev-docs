# init(contentsOfFile:uniformTypeIdentifier:)

**Framework**: XCTest  
**Kind**: init  
**Role**: Initializer

## Declaration

```swift
convenience init(contentsOfFile url: URL, uniformTypeIdentifier identifier: String)
```

```objc
+ (instancetype) attachmentWithContentsOfFileAtURL:(NSURL *) url uniformTypeIdentifier:(NSString *) identifier;
```

## Discussion

Creates an attachment with an existing file on disk and type.

> **Note**: Only works for files, not directories.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xctest/xctattachment/init(contentsoffile:uniformtypeidentifier:))*