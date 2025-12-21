# init(machService:targetQueue:options:requirement:incomingMessageHandler:cancellationHandler:)

**Framework**: XPC  
**Kind**: init

**Availability**:
- Mac Catalyst 26.0+
- macOS 26.0+

## Declaration

```swift
@preconcurrency
convenience init<Message>(machService: String, targetQueue: DispatchQueue? = nil, options: XPCSession.InitializationOptions = .none, requirement: XPCPeerRequirement, incomingMessageHandler: ((Message) -> (any Encodable)?)? = nil, cancellationHandler: ((XPCRichError) -> Void)? = nil) throws where Message : Decodable
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/xpc/xpcsession/init(machservice:targetqueue:options:requirement:incomingmessagehandler:cancellationhandler:)-7o5oq)*