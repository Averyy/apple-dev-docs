# init(uniformTypeIdentifier:name:payload:userInfo:)

**Framework**: XCTest  
**Kind**: init

Creates an attachment containing the provided data payload, optionally with a custom UTI, name, and user-provided metadata dictionary.

## Declaration

```swift
init(uniformTypeIdentifier identifier: String?, name: String?, payload: Data?, userInfo: [AnyHashable : Any]? = nil)
```

#### Discussion

Creates an attachment with a [`uniformTypeIdentifier`](xctattachment/uniformtypeidentifier.md) of `"public.data"` if the `identifier` parameter is `nil`.

## Parameters

- `identifier`: An optional custom UTI to represent the data’s content type.
- `name`: An optional name for the attachment, to be used in Xcode’s test reports.
- `payload`: The data to wrap as an attachment.
- `userInfo`: An optional dictionary of user-provided metadata to associate with the attachment.

## See Also

- [convenience init(data: Data)](xctattachment/init(data:).md)
  Creates an attachment containing the provided data payload.
- [convenience init(data: Data, uniformTypeIdentifier: String)](xctattachment/init(data:uniformtypeidentifier:).md)
  Creates an attachment containing the provided data payload, with a custom UTI.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xctest/xctattachment/init(uniformtypeidentifier:name:payload:userinfo:))*