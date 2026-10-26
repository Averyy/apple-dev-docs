# SMARTExecuteOffLineImmediate

**Framework**: IOKit  
**Kind**: structp  
**Role**: Instance Property

immediately initiate collection of SMART data.

**Availability**:
- Mac Catalyst 18.4+
- macOS 10.2+

## Declaration

```c
IOReturn (*SMARTExecuteOffLineImmediate)(void *interface, Boolean extendedTest);
```

#### Return Value

Returns kIOReturnSuccess if successful, kIOReturnNoDevice if there is no connection to an IOService, kIOReturnExclusiveAccess if it is already opened by another client.

#### Discussion

See section 8.54.4 of ATA/ATAPI-6.

## Parameters

- `extendedTest`: passing true will collect "off-line" extended test, false short test.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/ioatasmartinterface/1477737-smartexecuteofflineimmediate)*