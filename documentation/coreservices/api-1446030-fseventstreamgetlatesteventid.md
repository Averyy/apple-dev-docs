# FSEventStreamGetLatestEventId(_:)

**Framework**: Core Services  
**Kind**: func  
**Role**: Function

**Availability**:
- Mac Catalyst 13.1+
- macOS 10.5+

## Declaration

```swift
func FSEventStreamGetLatestEventId(_ streamRef: ConstFSEventStreamRef) -> FSEventStreamEventId
```

```c
FSEventStreamEventId FSEventStreamGetLatestEventId(ConstFSEventStreamRef streamRef);
```

#### Return Value

The sinceWhen attribute of the stream.

#### Discussion

Fetches the sinceWhen property of the stream. Upon receiving an event (and just before invoking the client's callback) this attribute is updated to the highest-numbered event ID mentioned in the event.

## Parameters

- `streamRef`: A valid stream.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1446030-fseventstreamgetlatesteventid)*