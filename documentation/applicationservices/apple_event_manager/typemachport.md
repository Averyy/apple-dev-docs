# typeMachPort

**Framework**: Application Services  
**Kind**: enum

For specifying a Mach port.

#### Overview

You might use this constant as part of sending an Apple event to an arbitrary Mach port. Your code for creating the descriptor might look like the following:

```occ
mach_port_t port = lookupPortForTarget(); // User routine to get  port.
// Now create a descriptor with it:
AECreateDesc(typeMachPort, &port, sizeof(port), &desc);
```

Actually sending an Apple event to a Mach port is an advanced technique and is not documented here.

## Topics

### Constants
- [var typeMachPort: DescType](../coreservices/typemachport.md)
  Indicates a descriptor that specifies a Mach port.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applicationservices/apple_event_manager/typemachport)*