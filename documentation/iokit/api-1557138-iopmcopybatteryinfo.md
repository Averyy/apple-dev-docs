# IOPMCopyBatteryInfo

**Framework**: IOKit  
**Kind**: func  
**Role**: Function

Request raw battery data from the system.

**Availability**:
- Mac Catalyst 18.4+
- macOS 10.0+

## Declaration

```c
IOReturn IOPMCopyBatteryInfo(mach_port_t masterPort, CFArrayRef *info);
```

#### Return Value

Returns kIOReturnSuccess or an error condition if request failed.

#### Discussion

WARNING! IOPMCoyBatteryInfo is unsupported on ALL Intel CPU based systems. For PPC CPU based systems, it remains not recommended. For almost all purposes, developers should use the richer IOPowerSources API (with change notifications) instead of using IOPMCopyBatteryInfo. Keys to decipher IOPMCopyBatteryInfo's return CFArray exist in IOPM.h.

## Parameters

- `masterPort`: The primary port obtained from [`IOMasterPort`](./api-1514652-iomasterport.md). Pass `MACH_PORT_NULL`.
- `info`: A CFArray of CFDictionaries containing raw battery data.

## See Also

### Miscellaneous
- [IOPMAssertionDictionaryKeys](./iopmlib_h/iopmassertiondictionarykeys.md)
- [IOPMAssertionTypes](./iopmlib_h/iopmassertiontypes.md)
  Use as AssertionType argument to [`IOPMAssertionCreate`](./api-1557118-iopmassertioncreate.md). The idle display will not sleep when enabled, and consequently the system will not idle sleep.
- [IOPMFindPowerManagement](./api-1557133-iopmfindpowermanagement.md)
  Finds the Root Power Domain IOService.
- [IOPMGetAggressiveness](./api-1557117-iopmgetaggressiveness.md)
  Retrieves the current value of one of the aggressiveness factors in IOKit Power Management.
- [IOPMSetAggressiveness](./api-1557098-iopmsetaggressiveness.md)
  Sets one of the aggressiveness factors in IOKit Power Management.
- [IOPMSleepEnabled](./api-1557074-iopmsleepenabled.md)
  Tells whether the system supports full sleep, or just doze
- [IOPMSleepSystem](./api-1557121-iopmsleepsystem.md)
  Request that the system initiate sleep.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/1557138-iopmcopybatteryinfo)*