# SMARTReadLogAtAddress

**Framework**: IOKit  
**Kind**: structp  
**Role**: Instance Property

Reads the 512-byte log at the specified logOffset in the log.

**Availability**:
- Mac Catalyst 18.4+
- macOS 10.2+

## Declaration

```c
IOReturn (*SMARTReadLogAtAddress)(void *interface, UInt32 logOffset, void *buffer, UInt32 size);
```

#### Discussion

Reads the 512-byte log at the specified logOffset in the log. See section 8.54.6.4 of ATA/ATAPI-6.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/ioatasmartinterface/1477739-smartreadlogataddress)*