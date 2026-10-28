# SMARTReturnStatus

**Framework**: IOKit  
**Kind**: structp  
**Role**: Instance Property

see if device has detected a threshold exceeded condition.

**Availability**:
- Mac Catalyst 18.4+
- macOS 10.2+

## Declaration

```c
IOReturn (*SMARTReturnStatus)(void *interface, Boolean *exceededCondition);
```

## Return Value

Returns kIOReturnSuccess if successful, kIOReturnNoDevice if there is no connection to an IOService, kIOReturnExclusiveAccess if it is already opened by another client.

## Discussion

The caller will poll this function and if exceededCondition is non-zero and we returned kIOReturnSuccess the device threshold exceeded condition. This would prompt the caller to call ATASMARTReadData to get more information. See section 8.54.7 of ATA/ATAPI-6.

## Parameters

- `exceededCondition`: if exceededCondition is non-zero the device threshold exceeded condition.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/ioatasmartinterface/1477727-smartreturnstatus)*