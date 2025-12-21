# init(machService:targetQueue:options:requirement:incomingMessageHandler:cancellationHandler:)

**Framework**: XPC  
**Kind**: init

**Availability**:
- Mac Catalyst 26.0+
- macOS 26.0+

## Declaration

```swift
@preconcurrency
convenience init(machService: String, targetQueue: DispatchQueue? = nil, options: XPCSession.InitializationOptions = .none, requirement: XPCPeerRequirement, incomingMessageHandler: ((XPCDictionary) -> XPCDictionary?)? = nil, cancellationHandler: ((XPCRichError) -> Void)? = nil) throws
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/xpc/xpcsession/init(machservice:targetqueue:options:requirement:incomingmessagehandler:cancellationhandler:)-5pk9g)*