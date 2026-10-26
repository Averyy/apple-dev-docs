# Event Source Constants

**Framework**: Core Services  
**Kind**: enum  
**Role**: Enumeration

Identify how an Apple event was delivered.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```c
enum : unsigned int {
    ...
};
```

## Topics

### Constants
- [kAEUnknownSource](./api-1527201-event_source_constants/kaeunknownsource.md)
  The source of the Apple event is unknown.
- [kAEDirectCall](./api-1527201-event_source_constants/kaedirectcall.md)
  The source of the Apple event is a direct call that bypassed the PPC Toolbox.
- [kAESameProcess](./api-1527201-event_source_constants/kaesameprocess.md)
  The source of the Apple event is the same application that received the event (the target application and the source application are the same).
- [kAELocalProcess](./api-1527201-event_source_constants/kaelocalprocess.md)
  The source application is another process on the same computer as the target application.
- [kAERemoteProcess](./api-1527201-event_source_constants/kaeremoteprocess.md)
  The source application is a process on a remote computer on the network.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1527201-event_source_constants)*