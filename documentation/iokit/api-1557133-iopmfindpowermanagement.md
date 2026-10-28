# IOPMFindPowerManagement

**Framework**: IOKit  
**Kind**: func  
**Role**: Function

Finds the Root Power Domain IOService.

**Availability**:
- Mac Catalyst 18.4+
- macOS 10.0+

## Declaration

```c
io_connect_t IOPMFindPowerManagement(mach_port_t master_device_port);
```

## Return Value

Returns a [`io_connect_t`](./io_connect_t.md) handle on the root domain. Must be released with IOServiceClose() when done.

## Parameters

- `master_device_port`: Pass in `MACH_PORT_NULL` for the primary device port.

## See Also

### Miscellaneous
- [IOPMAssertionDictionaryKeys](./iopmlib_h/iopmassertiondictionarykeys.md)
- [IOPMAssertionTypes](./iopmlib_h/iopmassertiontypes.md)
  Use as AssertionType argument to [`IOPMAssertionCreate`](./api-1557118-iopmassertioncreate.md). The idle display will not sleep when enabled, and consequently the system will not idle sleep.
- [IOPMCopyBatteryInfo](./api-1557138-iopmcopybatteryinfo.md)
  Request raw battery data from the system.
- [IOPMGetAggressiveness](./api-1557117-iopmgetaggressiveness.md)
  Retrieves the current value of one of the aggressiveness factors in IOKit Power Management.
- [IOPMSetAggressiveness](./api-1557098-iopmsetaggressiveness.md)
  Sets one of the aggressiveness factors in IOKit Power Management.
- [IOPMSleepEnabled](./api-1557074-iopmsleepenabled.md)
  Tells whether the system supports full sleep, or just doze
- [IOPMSleepSystem](./api-1557121-iopmsleepsystem.md)
  Request that the system initiate sleep.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/1557133-iopmfindpowermanagement)*