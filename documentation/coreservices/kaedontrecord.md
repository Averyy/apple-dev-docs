# kAEDontRecord

**Framework**: Core Services  
**Kind**: data  
**Role**: Global Variable

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
var kAEDontRecord: Int { get }
```

#### Discussion

The recording preference—your application is sending an event to itself but does not want the event recorded. When Apple event recording is on, the Apple Event Manager records a copy of every event your application sends to itself except for those events for which this flag is set.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/kaedontrecord)*