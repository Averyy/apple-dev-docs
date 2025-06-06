# AEEventID

**Framework**: Core Services  
**Kind**: tdef

Specifies the event ID of an Apple event.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
typealias AEEventID = FourCharCode
```

#### Discussion

Apple events are identified by their event class and event ID attributes. The event ID is the attribute that identifies a particular Apple event within its event class. In conjunction with the event class, the event ID uniquely identifies the Apple event and communicates what action the Apple event should perform.

For more information on Apple event IDs, see [`Event ID Constants`](apple_events/1527223-event_id_constants.md). 


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/aeeventid)*