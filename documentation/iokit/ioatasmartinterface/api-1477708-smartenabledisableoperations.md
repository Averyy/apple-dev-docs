# SMARTEnableDisableOperations

**Framework**: IOKit  
**Kind**: structp  
**Role**: Instance Property

toggle SMART Operations.

**Availability**:
- Mac Catalyst 18.4+
- macOS 10.2+

## Declaration

```c
IOReturn (*SMARTEnableDisableOperations)(void *interface, Boolean enable);
```

#### Return Value

Returns kIOReturnSuccess if successful, kIOReturnNoDevice if there is no connection to an IOService, kIOReturnExclusiveAccess if it is already opened by another client.

#### Discussion

See section 8.54.1 and 8.54.3 of ATA/ATAPI-6.

## Parameters

- `enable`: Passing true will ENABLE SMART operations, false will DISABLE SMART operations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/ioatasmartinterface/1477708-smartenabledisableoperations)*