# init(string:)

**Framework**: XCTest  
**Kind**: init  
**Role**: Initializer

Creates an attachment containing the provided string.

## Declaration

```swift
convenience init(string: String)
```

```objc
+ (instancetype) attachmentWithString:(NSString *) string;
```

## Discussion

Creates an attachment with a [`uniformTypeIdentifier`](./uniformtypeidentifier.md) of `"``public.plain-text"`.

## Parameters

- `string`: The string to wrap as an attachment.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xctest/xctattachment/init(string:))*