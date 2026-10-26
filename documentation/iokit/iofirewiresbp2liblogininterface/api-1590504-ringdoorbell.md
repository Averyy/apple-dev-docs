# ringDoorbell

**Framework**: IOKit  
**Kind**: structp  
**Role**: Instance Property

Rings the doorbell on the LUN.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```c
IOReturn (*ringDoorbell)(void *self);
```

#### Return Value

Returns kIOReturnSuccess if the ring started successfully.

#### Discussion

Non-immediate appends to the ORB chain may require the fetch agent state machine to be notified of the new ORB's presence. This is accomplished by writing to the so called doorbell register. This method begins one of those writes.

## Parameters

- `self`: Pointer to IOFireWireSBP2LibLoginInterface object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/iofirewiresbp2liblogininterface/1590504-ringdoorbell)*