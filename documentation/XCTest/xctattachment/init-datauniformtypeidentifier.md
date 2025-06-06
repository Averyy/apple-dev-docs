# init(data:uniformTypeIdentifier:)

**Framework**: Xctest  
**Kind**: init

Creates an attachment containing the provided data payload, with a custom UTI.

## Declaration

```swift
convenience init(data payload: Data, uniformTypeIdentifier identifier: String)
```

#### Discussion

Creates an attachment with a [`uniformTypeIdentifier`](xctattachment/uniformtypeidentifier.md) of `"``public.data"`.

## Parameters

- `payload`: The data to wrap as an attachment.
- `identifier`: A custom UTI to represent the data’s content type.

## See Also

- [convenience init(data: Data)](xctattachment/init(data:).md)
  Creates an attachment containing the provided data payload.
- [init(uniformTypeIdentifier: String?, name: String?, payload: Data?, userInfo: [AnyHashable : Any]?)](xctattachment/init(uniformtypeidentifier:name:payload:userinfo:).md)
  Creates an attachment containing the provided data payload, optionally with a custom UTI, name, and user-provided metadata dictionary.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xctest/xctattachment/init(data:uniformtypeidentifier:))*