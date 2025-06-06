# FSEventStreamEventId

**Framework**: Core Services  
**Kind**: tdef

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.5+

## Declaration

```swift
typealias FSEventStreamEventId = UInt64
```

#### Discussion

Event IDs that can be passed to the FSEventStreamCreate...() functions and FSEventStreamCallback(). They are monotonically increasing per system, even across reboots and drives coming and going. They bear no relation to any particular clock or timebase.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/fseventstreameventid)*