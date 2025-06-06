# kAEAlwaysInteract

**Framework**: Core Services  
**Kind**: data

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
var kAEAlwaysInteract: Int { get }
```

#### Discussion

The user interaction preference—the server application should always interact with the user in response to the Apple event. By convention, you set the bit specified by this constant whenever the server application normally asks a user to confirm a decision or interact in any other way, even if no additional information is needed from the user. If you set the bit specified by this constant, the `AEInteractWithUser(_:_:_:)` function either brings the server application to the foreground or posts a notification request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/kaealwaysinteract)*