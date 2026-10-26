# IOPMSchedulePowerEvent

**Framework**: IOKit  
**Kind**: func  
**Role**: Function

Schedule the machine to wake from sleep, power on, go to sleep, or shutdown.

**Availability**:
- Mac Catalyst 18.4+
- macOS 10.3+

## Declaration

```c
IOReturn IOPMSchedulePowerEvent(CFDateRef time_to_wake, CFStringRef my_id, CFStringRef type);
```

#### Return Value

kIOReturnSuccess on success, otherwise on failure

#### Discussion

This event will be added to the system's queue of power events and stored persistently on disk. The sleep and shutdown events present a graphical warning and allow a console user to cancel the event. Must be called as root.

## Parameters

- `time_to_wake`: Date and time that the system will power on/off.
- `my_id`: A CFStringRef identifying the calling app by CFBundleIdentifier. May be NULL.
- `type`: The type of power on you desire, either wake from sleep or power on. Choose from: CFSTR(kIOPMAutoWake) == wake machine, CFSTR(kIOPMAutoPowerOn) == power on machine, CFSTR(kIOPMAutoWakeOrPowerOn) == wake or power on, CFSTR(kIOPMAutoSleep) == sleep machine, CFSTR(kIOPMAutoShutdown) == power off machine, CFSTR(kIOPMAutoRestart) == restart the machine.

## See Also

### ScheduledEvents
- [IOPMCancelScheduledPowerEvent](./api-1557116-iopmcancelscheduledpowerevent.md)
  Cancel a previously scheduled power event.
- [IOPMCopyScheduledPowerEvents](./api-1557109-iopmcopyscheduledpowerevents.md)
  List all scheduled system power events


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/1557076-iopmschedulepowerevent)*