# handleCancellation(error:)

**Framework**: Xpc  
**Kind**: method  
**Required**: Yes

A closure the system invokes when it cancels a session with a client.

**Availability**:
- Mac Catalyst 17.0+
- macOS 14.0+

## Declaration

```swift
func handleCancellation(error: XPCRichError)
```

## Parameters

- `error`: A description of the reason for the session’s cancellation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xpc/xpcpeerhandler/handlecancellation(error:))*