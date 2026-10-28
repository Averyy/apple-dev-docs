# SMARTReadDataThresholds

**Framework**: IOKit  
**Kind**: structp  
**Role**: Instance Property

Retrieves 512 byte device SMART data thresholds structure.

**Availability**:
- Mac Catalyst 18.4+
- macOS 10.2+

## Declaration

```c
IOReturn (*SMARTReadDataThresholds)(void *interface, ATASMARTDataThresholds *dataThresholds);
```

## Discussion

Retrieves 512 byte device SMART data thresholds structure. This command is not defined as part of ATA/ATAPI-6, but is implemented by a large variety of manufacturers. Will return an appropiate error if command can not be completed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/ioatasmartinterface/1477797-smartreaddatathresholds)*