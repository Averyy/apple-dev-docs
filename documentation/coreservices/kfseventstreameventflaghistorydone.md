# kFSEventStreamEventFlagHistoryDone

**Framework**: Core Services  
**Kind**: data

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.5+

## Declaration

```swift
var kFSEventStreamEventFlagHistoryDone: Int { get }
```

#### Discussion

Denotes a sentinel event sent to mark the end of the "historical" events sent as a result of specifying a sinceWhen value in the FSEventStreamCreate...() call that created this event stream. (It will not be sent if kFSEventStreamEventIdSinceNow was passed for sinceWhen.) After invoking the client's callback with all the "historical" events that occurred before now, the client's callback will be invoked with an event where the kFSEventStreamEventFlagHistoryDone flag is set. The client should ignore the path supplied in this callback.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/kfseventstreameventflaghistorydone)*