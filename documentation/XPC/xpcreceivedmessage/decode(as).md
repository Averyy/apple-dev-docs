# decode(as:)

**Framework**: XPC  
**Kind**: method  
**Role**: Instance Method

Decodes a message as the given type.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS
- watchOS 10.0+

## Declaration

```swift
func decode<T>(as type: T.Type = T.self) throws -> T where T : Decodable
```

#### Return Value

A value of the specified type if the message data decodes successfully.

#### Discussion

If the message data doesn’t decode to the type, this method throws the appropriate [`DecodingError`](../../Swift/decodingerror.md).

## Parameters

- `type`: The type of the value in the message.

## See Also

### Accessing message content
- [var isSync: Bool](./issync.md)
  A Boolean value that indicates if this message is from a synchronous request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xpc/xpcreceivedmessage/decode(as:))*