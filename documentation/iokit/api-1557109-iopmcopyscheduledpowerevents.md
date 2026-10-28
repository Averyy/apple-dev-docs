# IOPMCopyScheduledPowerEvents

**Framework**: IOKit  
**Kind**: func  
**Role**: Function

List all scheduled system power events

**Availability**:
- Mac Catalyst 18.4+
- macOS 10.3+

## Declaration

```c
CFArrayRef IOPMCopyScheduledPowerEvents(void);
```

## Return Value

A CFArray of CFDictionaries of power events. The CFArray must be released by the caller. NULL if there are no scheduled events.

## Discussion

Returns a CFArray of CFDictionaries of power events. Each CFDictionary contains keys for CFSTR(kIOPMPowerEventTimeKey), CFSTR(kIOPMPowerEventAppNameKey), and CFSTR(kIOPMPowerEventTypeKey).

## See Also

### ScheduledEvents
- [IOPMCancelScheduledPowerEvent](./api-1557116-iopmcancelscheduledpowerevent.md)
  Cancel a previously scheduled power event.
- [IOPMSchedulePowerEvent](./api-1557076-iopmschedulepowerevent.md)
  Schedule the machine to wake from sleep, power on, go to sleep, or shutdown.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/1557109-iopmcopyscheduledpowerevents)*