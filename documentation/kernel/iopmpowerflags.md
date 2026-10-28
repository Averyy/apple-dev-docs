# IOPMPowerFlags

**Framework**: Kernel  
**Kind**: tdef  
**Role**: Type Alias

Bits are used in defining capabilityFlags, inputPowerRequirements, and outputPowerCharacter in the IOPMPowerState structure.

**Availability**:
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
- [kIOPMPowerOn](./api-1645009-anonymous/kiopmpoweron.md)
- [kIOPMDeviceUsable](./api-1645009-anonymous/kiopmdeviceusable.md)
- [kIOPMLowPower](./api-1645009-anonymous/kiopmlowpower.md)
- [kIOPMPreventIdleSleep](./api-1645009-anonymous/kiopmpreventidlesleep.md)
- [kIOPMSleepCapability](./api-1645009-anonymous/kiopmsleepcapability.md)
- [kIOPMRestartCapability](./api-1645009-anonymous/kiopmrestartcapability.md)
- [kIOPMSleep](./api-1645009-anonymous/kiopmsleep.md)
- [kIOPMRestart](./api-1645009-anonymous/kiopmrestart.md)
- [kIOPMInitialDeviceState](./api-1645009-anonymous/kiopminitialdevicestate.md)

## See Also

### Related Documentation
- [IOPMPowerFlags](./iopmpowerflags.md)
  Bits are used in defining capabilityFlags, inputPowerRequirements, and outputPowerCharacter in the IOPMPowerState structure.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iopmpowerflags)*