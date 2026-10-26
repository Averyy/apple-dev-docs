# init(data:)

**Framework**: XCTest  
**Kind**: init  
**Role**: Initializer

Creates an attachment containing the provided data payload.

## Declaration

```swift
convenience init(data payload: Data)
```

```objc
+ (instancetype) attachmentWithData:(NSData *) payload;
```

#### Discussion

Creates an attachment with a [`uniformTypeIdentifier`](./uniformtypeidentifier.md) of `"``public.data"`.

## Parameters

- `payload`: The data to wrap as an attachment.

## See Also

### Creating Attachments from Data
- [convenience init(data: Data, uniformTypeIdentifier: String)](./init%28data,uniformtypeidentifier%29.md)
  Creates an attachment containing the provided data payload, with a custom UTI.
- [init(uniformTypeIdentifier: String?, name: String?, payload: Data?, userInfo: [AnyHashable : Any]?)](./init%28uniformtypeidentifier,name,payload,userinfo%29.md)
  Creates an attachment containing the provided data payload, optionally with a custom UTI, name, and user-provided metadata dictionary.
- [+ attachmentWithUniformTypeIdentifier:name:payload:userInfo:](./attachmentwithuniformtypeidentifier_name_payload_userinfo_.md)
  Creates an attachment containing the provided data payload, optionally with a custom UTI, name, and user-provided metadata dictionary.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xctest/xctattachment/init(data:))*