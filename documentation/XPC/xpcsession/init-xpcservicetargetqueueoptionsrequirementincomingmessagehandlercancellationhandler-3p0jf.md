# init(xpcService:targetQueue:options:requirement:incomingMessageHandler:cancellationHandler:)

**Framework**: XPC  
**Kind**: init

**Availability**:
- Mac Catalyst 26.0+
- macOS 26.0+

## Declaration

```swift
@preconcurrency
convenience init(xpcService: String, targetQueue: DispatchQueue? = nil, options: XPCSession.InitializationOptions = .none, requirement: XPCPeerRequirement, incomingMessageHandler: ((XPCDictionary) -> XPCDictionary?)? = nil, cancellationHandler: ((XPCRichError) -> Void)? = nil) throws
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/xpc/xpcsession/init(xpcservice:targetqueue:options:requirement:incomingmessagehandler:cancellationhandler:)-3p0jf)*