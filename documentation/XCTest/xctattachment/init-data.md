# init(data:)

**Framework**: Xctest  
**Kind**: init

Creates an attachment containing the provided data payload.

## Declaration

```swift
convenience init(data payload: Data)
```

#### Discussion

Creates an attachment with a [`uniformTypeIdentifier`](xctattachment/uniformtypeidentifier.md) of `"``public.data"`.

## Parameters

- `payload`: The data to wrap as an attachment.

## See Also

- [convenience init(data: Data, uniformTypeIdentifier: String)](xctattachment/init(data:uniformtypeidentifier:).md)
  Creates an attachment containing the provided data payload, with a custom UTI.
- [init(uniformTypeIdentifier: String?, name: String?, payload: Data?, userInfo: [AnyHashable : Any]?)](xctattachment/init(uniformtypeidentifier:name:payload:userinfo:).md)
  Creates an attachment containing the provided data payload, optionally with a custom UTI, name, and user-provided metadata dictionary.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xctest/xctattachment/init(data:))*