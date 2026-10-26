# kDurationImmediate

**Framework**: Core Services  
**Kind**: econst  
**Role**: Enumeration Case

The task times out immediately, whether or not the event has occurred. If the event occurred, the return status is `noErr`. If the event did not occur, the return status is `kMPTimeoutErr` (assuming no other errors occurred). 

**Availability**:
- Mac Catalyst 13.1+ - Deprecated in 13.1
- macOS 10.0+ - Deprecated in 10.7

## Declaration

```c
kDurationImmediate = 0
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1585641-timer_duration_constants/kdurationimmediate)*