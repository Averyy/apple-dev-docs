# NewPMIdleUPP

**Framework**: Application Services  
**Kind**: func

Creates a new universal procedure pointer (UPP) to an idle callback.

> **Deprecated**: There is no replacement; this function was included to facilitate porting legacy applications to macOS, but it serves no useful purpose.

## Declaration

```c
PMIdleUPP NewPMIdleUPP (
   PMIdleProcPtr userRoutine
);
```

## Overview

You do not need this function in macOS. Instead, use the standard idle proc. See the [PMIdleProcPtr](./pmidleprocptr.md) callback function.

## See Also

### Creating, Calling, and Deleting Universal Procedure Pointers
- [InvokePMIdleUPP](./api-1805637-invokepmidleupp.md)
  Calls an idle callback.
- [DisposePMIdleUPP](./api-1805641-disposepmidleupp.md)
  Disposes of a universal procedure pointer (UPP) to an idle callback.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applicationservices/core_printing/1805635-newpmidleupp)*