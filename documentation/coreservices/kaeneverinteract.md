# kAENeverInteract

**Framework**: Core Services  
**Kind**: data

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
var kAENeverInteract: Int { get }
```

#### Discussion

The user interaction preference—the server application should never interact with the user in response to the Apple event. If you set the bit specified by this constant, the `AEInteractWithUser(_:_:_:)` function (when called by the server) returns the `errAENoUserInteraction` result code. When you send an Apple event to a remote application, the default is to set this bit.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/kaeneverinteract)*