# DisposePMIdleUPP

**Framework**: Application Services  
**Kind**: func

Disposes of a universal procedure pointer (UPP) to an idle callback.

> **Deprecated**: There is no replacement; this function was included to facilitate porting legacy applications to macOS, but it serves no useful purpose.

## Declaration

```c
void DisposePMIdleUPP (
   PMIdleUPP userUPP
);
```

#### Overview

You do not need this function in macOS. Instead, use the standard idle proc. See the [PMIdleProcPtr](./pmidleprocptr.md) callback function.

## See Also

### Creating, Calling, and Deleting Universal Procedure Pointers
- [NewPMIdleUPP](./api-1805635-newpmidleupp.md)
  Creates a new universal procedure pointer (UPP) to an idle callback.
- [InvokePMIdleUPP](./api-1805637-invokepmidleupp.md)
  Calls an idle callback.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applicationservices/core_printing/1805641-disposepmidleupp)*