# InvokePMIdleUPP

**Framework**: Application Services  
**Kind**: func

Calls an idle callback.

> **Deprecated**: There is no replacement; this function was included to facilitate porting legacy applications to macOS, but it serves no useful purpose.

## Declaration

```c
void InvokePMIdleUPP (
   PMIdleUPP userUPP
);
```

## Overview

You do not need this function in macOS. Instead, use the standard idle proc. See the [PMIdleProcPtr](./pmidleprocptr.md) callback function.

## See Also

### Creating, Calling, and Deleting Universal Procedure Pointers
- [NewPMIdleUPP](./api-1805635-newpmidleupp.md)
  Creates a new universal procedure pointer (UPP) to an idle callback.
- [DisposePMIdleUPP](./api-1805641-disposepmidleupp.md)
  Disposes of a universal procedure pointer (UPP) to an idle callback.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applicationservices/core_printing/1805637-invokepmidleupp)*