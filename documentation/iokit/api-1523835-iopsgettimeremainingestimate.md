# IOPSGetTimeRemainingEstimate

**Framework**: IOKit  
**Kind**: func  
**Role**: Function

Returns the estimated minutes remaining until all power sources (battery and/or UPS's) are empty, or returns [`kIOPSTimeRemainingUnlimited`](./kiopstimeremainingunlimited.md) if attached to an unlimited power source.

**Availability**:
- Mac Catalyst 18.4+
- macOS 10.7+

## Declaration

```c
CFTimeInterval IOPSGetTimeRemainingEstimate(void);
```

#### Return Value

Returns [`kIOPSTimeRemainingUnknown`](./kiopstimeremainingunknown.md) if the OS cannot determine the time remaining.

Returns [`kIOPSTimeRemainingUnlimited`](./kiopstimeremainingunlimited.md) if the system has an unlimited power source.

Otherwise returns a positive number of type CFTimeInterval, indicating the time remaining in seconds until all power sources are depleted.

#### Discussion

If attached to an "Unlimited" power source, like AC power or any external source, the return value is [`kIOPSTimeRemainingUnlimited`](./kiopstimeremainingunlimited.md)

If the system is on "Limited" power, like a battery or UPS, but is still calculating the time remaining, which may take several seconds after each system power event (e.g. waking from sleep, or unplugging AC Power), the return value is [`kIOPSTimeRemainingUnknown`](./kiopstimeremainingunknown.md)

Otherwise, if the system is on "Limited" power and the system has an accurate time remaining estimate, the system returns a CFTimeInterval estimate of the time remaining until the system is out of battery power.

If you require more detailed battery information, use [`IOPSCopyPowerSourcesInfo`](./api-1523839-iopscopypowersourcesinfo.md)> and [`IOPSGetPowerSourceDescription`](./api-1523867-iopsgetpowersourcedescription.md)>.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/1523835-iopsgettimeremainingestimate)*