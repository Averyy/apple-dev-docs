# SMARTReadData

**Framework**: IOKit  
**Kind**: structp  
**Role**: Instance Property

Retrieves 512 byte device SMART data structure.

**Availability**:
- Mac Catalyst 18.4+
- macOS 10.2+

## Declaration

```c
IOReturn (*SMARTReadData)(void *interface, ATASMARTData *data);
```

## Discussion

See section 8.54.5 of ATA/ATAPI-6. Will return an appropiate error if command can not be completed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/ioatasmartinterface/1477805-smartreaddata)*