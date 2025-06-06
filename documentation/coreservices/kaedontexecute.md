# kAEDontExecute

**Framework**: Core Services  
**Kind**: data

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
var kAEDontExecute: Int { get }
```

#### Discussion

The execution preference—your application is sending an Apple event to itself for recording purposes only—that is, you want the Apple Event Manager to send a copy of the event to the recording process but you do not want your application actually to receive the event.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/kaedontexecute)*