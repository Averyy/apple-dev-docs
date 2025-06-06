# kAEDontReconnect

**Framework**: Core Services  
**Kind**: data

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
var kAEDontReconnect: Int { get }
```

#### Discussion

Deprecated and unsupported in macOS. The reconnection preference—the Apple Event Manager must not automatically try to reconnect if it receives a `sessClosedErr` result code from the PPC Toolbox. If you don’t set this flag, the Apple Event Manager automatically attempts to reconnect and reestablish the session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/kaedontreconnect)*