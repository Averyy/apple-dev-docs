# sendCommand

**Framework**: IOKit  
**Kind**: structp  
**Role**: Instance Property

Send a command to the UPS.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.3+

## Declaration

```c
IOReturn (*sendCommand)(void *thisPointer, CFDictionaryRef command);
```

#### Return Value

An IOReturn error code.

#### Discussion

Command keys are defined in IOPSKeys.h and begin with kIOPSCommand. An error should be returned if your device does not know how to respond to a command.

## Parameters

- `thisPointer`: The UPS Interface to use.
- `command`: CFDictionaryRef that contains the command.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/ioupsplugininterface/1560779-sendcommand)*