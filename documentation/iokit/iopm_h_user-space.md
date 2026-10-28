# IOPM.h User-Space

**Framework**: IOKit  
**Role**: API Collection

Defines power management constants and keys used by both in-kernel and user space power management.

## Overview

IOPM.h defines a range of power management constants used in several in-kernel and user space APIs. Most significantly, the IOPMPowerFlags used to specify the fields of an IOPMPowerState struct are defined here.

Most of the constants defined in IOPM.h are deprecated or for Apple internal use only, and are not elaborated on in headerdoc.

### Included Headers

- <IOKit/IOTypes.h>
- <IOKit/IOMessage.h>
- <IOKit/IOReturn.h>

## Topics

### Data Types
- [IOPMSystemCapabilityChangeParameters](../kernel/iopmsystemcapabilitychangeparameters.md)
  A structure describing a system capability change.
### Constants
- [Defines](./iopm_h_user-space/defines.md)
- [Global Variables](./iopm_h_user-space/global_variables.md)
- [IOPMPowerFlags](../kernel/iopmpowerflags.md)
  Bits are used in defining capabilityFlags, inputPowerRequirements, and outputPowerCharacter in the IOPMPowerState structure.
- [IOPMSystemCapabilityChangeFlags](./api-1499721-iopmsystemcapabilitychangeflags.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/iopm_h_user-space)*