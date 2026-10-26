# Timer Duration Constants

**Framework**: Core Services  
**Kind**: enum  
**Role**: Enumeration

Specify the maximum time a task should wait for an event to occur. 

**Availability**:
- Mac Catalyst 13.1+ - Deprecated in 13.1
- macOS 10.0+ - Deprecated in 10.7

## Declaration

```c
enum : int {
    ...
};
```

## Topics

### Constants
- [kDurationImmediate](./api-1585641-timer_duration_constants/kdurationimmediate.md)
  The task times out immediately, whether or not the event has occurred. If the event occurred, the return status is `noErr`. If the event did not occur, the return status is `kMPTimeoutErr` (assuming no other errors occurred). 
- [kDurationForever](./api-1585641-timer_duration_constants/kdurationforever.md)
  The task waits forever. The blocking call waits until either the event occurs, or until the object being waited upon (such as a message queue) is deleted.
- [kDurationMillisecond](./api-1585641-timer_duration_constants/kdurationmillisecond.md)
  The task waits one millisecond before timing out. 
- [kDurationMicrosecond](./api-1585641-timer_duration_constants/kdurationmicrosecond.md)
  The task waits one microsecond before timing out. 


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1585641-timer_duration_constants)*