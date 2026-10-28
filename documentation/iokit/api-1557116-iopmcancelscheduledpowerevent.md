# IOPMCancelScheduledPowerEvent

**Framework**: IOKit  
**Kind**: func  
**Role**: Function

Cancel a previously scheduled power event.

**Availability**:
- Mac Catalyst 18.4+
- macOS 10.3+

## Declaration

```c
IOReturn IOPMCancelScheduledPowerEvent(CFDateRef time_to_wake, CFStringRef my_id, CFStringRef type);
```

## Return Value

kIOReturnSuccess on success, otherwise on failure

## Discussion

Arguments mirror those to IOPMSchedulePowerEvent. All arguments must match the original arguments from when the power on was scheduled. Must be called as root.

## Parameters

- `time_to_wake`: Cancel entry with this date and time.
- `my_id`: Cancel entry with this name.
- `type`: Type to cancel

## See Also

### ScheduledEvents
- [IOPMCopyScheduledPowerEvents](./api-1557109-iopmcopyscheduledpowerevents.md)
  List all scheduled system power events
- [IOPMSchedulePowerEvent](./api-1557076-iopmschedulepowerevent.md)
  Schedule the machine to wake from sleep, power on, go to sleep, or shutdown.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/1557116-iopmcancelscheduledpowerevent)*