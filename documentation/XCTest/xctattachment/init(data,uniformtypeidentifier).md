# init(data:uniformTypeIdentifier:)

**Framework**: XCTest  
**Kind**: init  
**Role**: Initializer

Creates an attachment containing the provided data payload, with a custom UTI.

## Declaration

```swift
convenience init(data payload: Data, uniformTypeIdentifier identifier: String)
```

```objc
+ (instancetype) attachmentWithData:(NSData *) payload uniformTypeIdentifier:(NSString *) identifier;
```

#### Discussion

Creates an attachment with a [`uniformTypeIdentifier`](./uniformtypeidentifier.md) of `"``public.data"`.

## Parameters

- `payload`: The data to wrap as an attachment.
- `identifier`: A custom UTI to represent the data’s content type.

## See Also

### Creating Attachments from Data
- [convenience init(data: Data)](./init%28data%29.md)
  Creates an attachment containing the provided data payload.
- [init(uniformTypeIdentifier: String?, name: String?, payload: Data?, userInfo: [AnyHashable : Any]?)](./init%28uniformtypeidentifier,name,payload,userinfo%29.md)
  Creates an attachment containing the provided data payload, optionally with a custom UTI, name, and user-provided metadata dictionary.
- [+ attachmentWithUniformTypeIdentifier:name:payload:userInfo:](./attachmentwithuniformtypeidentifier_name_payload_userinfo_.md)
  Creates an attachment containing the provided data payload, optionally with a custom UTI, name, and user-provided metadata dictionary.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xctest/xctattachment/init(data:uniformtypeidentifier:))*