# SMARTWriteLogAtAddress

**Framework**: IOKit  
**Kind**: structp  
**Role**: Instance Property

Writes to the 512-byte log at the specified logOffset in the log.

**Availability**:
- Mac Catalyst 18.4+
- macOS 10.2+

## Declaration

```c
IOReturn (*SMARTWriteLogAtAddress)(void *interface, UInt32 logOffset, const void *buffer, UInt32 size);
```

## Discussion

Writes to the 512-byte log at the specified logOffset in the log. See section 8.54.8.4 of ATA/ATAPI-6.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/ioatasmartinterface/1477753-smartwritelogataddress)*