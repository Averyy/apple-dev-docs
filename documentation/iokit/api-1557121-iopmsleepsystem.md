# IOPMSleepSystem

**Framework**: IOKit  
**Kind**: func  
**Role**: Function

Request that the system initiate sleep.

**Availability**:
- Mac Catalyst 18.4+
- macOS 10.0+

## Declaration

```c
IOReturn IOPMSleepSystem(io_connect_t fb);
```

## Return Value

Returns kIOReturnSuccess or an error condition if request failed.

## Discussion

For security purposes, caller must be root or the console user.

## Parameters

- `fb`: Port used to communicate to the kernel, from IOPMFindPowerManagement.

## See Also

### Miscellaneous
- [IOPMAssertionDictionaryKeys](./iopmlib_h/iopmassertiondictionarykeys.md)
- [IOPMAssertionTypes](./iopmlib_h/iopmassertiontypes.md)
  Use as AssertionType argument to [`IOPMAssertionCreate`](./api-1557118-iopmassertioncreate.md). The idle display will not sleep when enabled, and consequently the system will not idle sleep.
- [IOPMCopyBatteryInfo](./api-1557138-iopmcopybatteryinfo.md)
  Request raw battery data from the system.
- [IOPMFindPowerManagement](./api-1557133-iopmfindpowermanagement.md)
  Finds the Root Power Domain IOService.
- [IOPMGetAggressiveness](./api-1557117-iopmgetaggressiveness.md)
  Retrieves the current value of one of the aggressiveness factors in IOKit Power Management.
- [IOPMSetAggressiveness](./api-1557098-iopmsetaggressiveness.md)
  Sets one of the aggressiveness factors in IOKit Power Management.
- [IOPMSleepEnabled](./api-1557074-iopmsleepenabled.md)
  Tells whether the system supports full sleep, or just doze


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/1557121-iopmsleepsystem)*