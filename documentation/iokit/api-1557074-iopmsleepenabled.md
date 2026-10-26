# IOPMSleepEnabled

**Framework**: IOKit  
**Kind**: func  
**Role**: Function

Tells whether the system supports full sleep, or just doze

**Availability**:
- Mac Catalyst 18.4+
- macOS 10.0+

## Declaration

```c
boolean_t IOPMSleepEnabled(void);
```

#### Return Value

Returns true if the system supports sleep, false if some hardware prevents full sleep.

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
- [IOPMSleepSystem](./api-1557121-iopmsleepsystem.md)
  Request that the system initiate sleep.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/1557074-iopmsleepenabled)*