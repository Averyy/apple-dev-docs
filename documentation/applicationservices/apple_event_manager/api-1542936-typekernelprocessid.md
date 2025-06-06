# typeKernelProcessID

**Framework**: Application Services

For specifying an application by UNIX process ID.

#### Overview

You might use this constant in a situation where you have access to the PID for a process but don’t have a Process Manager connection. Your code for creating the descriptor might look like the following:

```occ
pid_t pid = findTheAppPid(); // User supplied routine to get PID. // Now create a descriptor with it: AECreateDesc(typeKernelProcessID, &pid, sizeof(pid), &desc);
```

## Topics

### Constants
- [var typeKernelProcessID: DescType](../coreservices/typekernelprocessid.md)
  Indicates a descriptor containing a UNIX process ID. A process ID is similar to a PSN (processor serial number) but does not require a Process Manager connection. It is analogous to a 32-bit unsigned integer.
- [var typeMachPort: DescType](../coreservices/typemachport.md)
  Indicates a descriptor that specifies a Mach port.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applicationservices/apple_event_manager/1542936-typekernelprocessid)*