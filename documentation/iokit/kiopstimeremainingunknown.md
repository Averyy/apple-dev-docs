# kIOPSTimeRemainingUnknown

**Framework**: IOKit  
**Kind**: macro  
**Role**: Macro

Possible return value from [`IOPSGetTimeRemainingEstimate`](./api-1523835-iopsgettimeremainingestimate.md)

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.7+

## Declaration

```c
#define kIOPSTimeRemainingUnknown
```

#### Discussion

Indicates the system is connected to a limited power source, but the system is still calculating a time remaining estimate. Check for a valid estimate again when the notification kIOPSPowerSourcesNotificationKey fires.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/kiopstimeremainingunknown)*