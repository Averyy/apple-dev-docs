# SMARTValidateReadData

**Framework**: IOKit  
**Kind**: structp  
**Role**: Instance Property

Test the integrity of the device SMART data structure.

**Availability**:
- Mac Catalyst 18.4+
- macOS 10.2+

## Declaration

```c
IOReturn (*SMARTValidateReadData)(void *interface, const ATASMARTData *data);
```

## Discussion

The data structure checksum is the two's complement of the sum of the first 511 bytes in the data structure. The sum of all 512 bytes will be zero when the checksum is correct. See section 8.54.5.8.7 of ATA/ATAPI-6. Will return an error if checksum fails.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/ioatasmartinterface/1477745-smartvalidatereaddata)*