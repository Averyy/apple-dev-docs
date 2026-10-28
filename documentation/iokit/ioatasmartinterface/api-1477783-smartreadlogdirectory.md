# SMARTReadLogDirectory

**Framework**: IOKit  
**Kind**: structp  
**Role**: Instance Property

Reads the 512-byte log directory.

**Availability**:
- Mac Catalyst 18.4+
- macOS 10.2+

## Declaration

```c
IOReturn (*SMARTReadLogDirectory)(void *interface, ATASMARTLogDirectory *logData);
```

## Discussion

The log directory is a directory of all possible SMART logs available from the drive.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/ioatasmartinterface/1477783-smartreadlogdirectory)*