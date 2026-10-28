# IOPMGetThermalWarningLevel

**Framework**: IOKit  
**Kind**: func  
**Role**: Function

Get thermal warning level of the system.

**Availability**:
- Mac Catalyst 18.4+
- macOS 10.7+

## Declaration

```c
IOReturn IOPMGetThermalWarningLevel(uint32_t *thermalLevel);
```

## Return Value

kIOReturnSuccess, or other error report. Returns kIOReturnNotFound if thermal warning level has not been published.

## See Also

### CPU Power & Thermal
- [IOPMCopyCPUPowerStatus](./api-1557079-iopmcopycpupowerstatus.md)
  Copy status of all current CPU power levels.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/1557103-iopmgetthermalwarninglevel)*