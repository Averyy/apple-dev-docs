# submitORB

**Framework**: IOKit  
**Kind**: structp  
**Role**: Instance Property

Submits the given orb

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```c
IOReturn (*submitORB)(void *self, IOFireWireSBP2LibORBInterface **orb);
```

#### Return Value

Returns kIOReturnSuccess if the ORB has been started successfully.

#### Discussion

Starts execution of the given ORB. If the ORB is an immediate ORB it's addresss is written to the fetch agent. If it is a non immediate orb its address is appended to the last orb of the currently processing chain. The doorbell is not rung automatically it must be run manually with the ringDoorbell command described below.

## Parameters

- `self`: Pointer to IOFireWireSBP2LibLoginInterface object.
- `orb`: The orb to be executed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/iofirewiresbp2liblogininterface/1590476-submitorb)*