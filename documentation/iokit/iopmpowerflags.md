# IOPMPowerFlags

**Framework**: IOKit  
**Kind**: tdef  
**Role**: Type Alias

Bits are used in defining capabilityFlags, inputPowerRequirements, and outputPowerCharacter in the IOPMPowerState structure.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```c
typedef unsigned long IOPMPowerFlags;
```

## Discussion

These bits may be bitwise-OR'd together in the IOPMPowerState capabilityFlags field, the outputPowerCharacter field, and/or the inputPowerRequirement field.

The comments clearly mark whether each flag should be used in the capabilityFlags field, outputPowerCharacter field, and inputPowerRequirement field, or all three.

The value of capabilityFlags, inputPowerRequirement or outputPowerCharacter may be 0. Most drivers implement their 'OFF' state, used when asleep, by defininf each of the 3 fields as 0.

The bits listed below are only the most common bits used to define a device's power states. Your device's IO family may require that your device specify other input or output power flags to interact properly. Consult family-specific documentation to determine if your IOPower plane parents or children require other power flags; they probably don't.

## Topics

### Constants
- [kIOPMPowerOn](./api-1499606-anonymous/kiopmpoweron.md)
- [kIOPMDeviceUsable](./api-1499606-anonymous/kiopmdeviceusable.md)
- [kIOPMLowPower](./api-1499606-anonymous/kiopmlowpower.md)
- [kIOPMPreventIdleSleep](./api-1499606-anonymous/kiopmpreventidlesleep.md)
- [kIOPMSleepCapability](./api-1499606-anonymous/kiopmsleepcapability.md)
- [kIOPMRestartCapability](./api-1499606-anonymous/kiopmrestartcapability.md)
- [kIOPMSleep](./api-1499606-anonymous/kiopmsleep.md)
- [kIOPMRestart](./api-1499606-anonymous/kiopmrestart.md)
- [kIOPMInitialDeviceState](./api-1499606-anonymous/kiopminitialdevicestate.md)
- [kIOPMRootDomainState](./api-1499606-anonymous/kiopmrootdomainstate.md)

## See Also

### Related Documentation
- [IOPMPowerFlags](../kernel/iopmpowerflags.md)
  Bits are used in defining capabilityFlags, inputPowerRequirements, and outputPowerCharacter in the IOPMPowerState structure.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/iopmpowerflags)*