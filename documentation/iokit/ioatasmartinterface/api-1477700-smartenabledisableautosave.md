# SMARTEnableDisableAutosave

**Framework**: IOKit  
**Kind**: structp  
**Role**: Instance Property

toggle SMART Autosave.

**Availability**:
- Mac Catalyst 18.4+
- macOS 10.2+

## Declaration

```c
IOReturn (*SMARTEnableDisableAutosave)(void *interface, Boolean enable);
```

## Return Value

Returns kIOReturnSuccess if successful, kIOReturnNoDevice if there is no connection to an IOService, kIOReturnExclusiveAccess if it is already opened by another client.

## Discussion

See section 8.54.2 of ATA/ATAPI-6.

## Parameters

- `enable`: Passing true will ENABLE SMART Autosave, false will DISABLE SMART Autosave.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/ioatasmartinterface/1477700-smartenabledisableautosave)*