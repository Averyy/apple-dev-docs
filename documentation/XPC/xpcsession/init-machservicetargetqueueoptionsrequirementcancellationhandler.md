# init(machService:targetQueue:options:requirement:cancellationHandler:)

**Framework**: XPC  
**Kind**: init

**Availability**:
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)

## Declaration

```swift
@preconcurrency
convenience init(machService: String, targetQueue: DispatchQueue? = nil, options: XPCSession.InitializationOptions = .none, requirement: XPCPeerRequirement, cancellationHandler: ((XPCRichError) -> Void)? = nil) throws
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/xpc/xpcsession/init(machservice:targetqueue:options:requirement:cancellationhandler:))*