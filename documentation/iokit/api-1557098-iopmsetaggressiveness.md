# IOPMSetAggressiveness

**Framework**: IOKit  
**Kind**: func  
**Role**: Function

Sets one of the aggressiveness factors in IOKit Power Management.

**Availability**:
- Mac Catalyst 18.4+
- macOS 10.0+

## Declaration

```c
IOReturn IOPMSetAggressiveness(io_connect_t fb, unsigned long type, unsigned long aggressiveness);
```

#### Return Value

Returns kIOReturnSuccess or an error condition if request failed.

## Parameters

- `fb`: Representation of the Root Power Domain from IOPMFindPowerManagement.
- `type`: Specifies which aggressiveness factor is being set.
- `aggressiveness`: New value of the aggressiveness factor.

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
- [IOPMSleepEnabled](./api-1557074-iopmsleepenabled.md)
  Tells whether the system supports full sleep, or just doze
- [IOPMSleepSystem](./api-1557121-iopmsleepsystem.md)
  Request that the system initiate sleep.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/1557098-iopmsetaggressiveness)*