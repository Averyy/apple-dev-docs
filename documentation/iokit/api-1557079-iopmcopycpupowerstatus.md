# IOPMCopyCPUPowerStatus

**Framework**: IOKit  
**Kind**: func  
**Role**: Function

Copy status of all current CPU power levels.

**Availability**:
- Mac Catalyst 18.4+
- macOS 10.7+

## Declaration

```c
IOReturn IOPMCopyCPUPowerStatus(CFDictionaryRef *cpuPowerStatus);
```

## Return Value

kIOReturnSuccess, or other error report. Returns kIOReturnNotFound if CPU PowerStatus has not been published.

## Discussion

The returned dictionary may define some of these keys, as defined in IOPM.h: - kIOPMCPUPowerLimitProcessorSpeedKey - kIOPMCPUPowerLimitProcessorCountKey - kIOPMCPUPowerLimitSchedulerTimeKey

## Parameters

- `cpuPowerStatus`: Upon success, a pointer to a dictionary defining CPU power; otherwise NULL. Pointer will be populated with a newly created dictionary upon successful return. Caller must release dictionary.

## See Also

### CPU Power & Thermal
- [IOPMGetThermalWarningLevel](./api-1557103-iopmgetthermalwarninglevel.md)
  Get thermal warning level of the system.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/1557079-iopmcopycpupowerstatus)*