# PMIdleProcPtr

**Framework**: Application Services  
**Kind**: tdef

Defines a pointer to an idle function. 

> **Deprecated**: There is no replacement; this callback function was included to facilitate porting legacy applications to macOS, but it serves no useful purpose.

## Declaration

```c
typedef void (*PMIdleProcPtr) (void);
```

## Overview

You would declare your idle function like this if you were to name it `MyPrintIdleCallback`:

### Discussion

If you install an idle function using the function `PMSessionSetIdleProc`, the printing system calls your idle function periodically during your print loop. Your idle function can display application status while printing, but it should not duplicate information displayed by the printing system or the printer driver. If you don’t install an idle function, you get the standard dialog for the current driver in Mac OS 8 and 9.

Your idle function must check whether the user has pressed Command-period, in which case your application should stop its printing operation. If your status dialog contains a button to cancel the printing operation, your idle function should also check for clicks in the button and respond accordingly.

To provide a pointer to your idle function, you create a universal procedure pointer (UPP) of type `PMIdleUPP`, using the function `NewPMIdleUPP`. You can do so with code similar to the following: 

```occ
PMIdleUPP MyPrintIdleUPP;
MyPrintIdleUPP = NewPMIdleUPP (&MyPrintIdleCallback);
```

When your print job is completed, you should use the function `DisposePMIdleUPP` to dispose of the universal procedure pointer associated with your idle function. However, if you will use the same idle function in subsequent print jobs, you can reuse the same UPP, rather than dispose of it and later create a new UPP.

### Special Considerations

Your idle function is not called in macOS. It’s only called in Mac OS 8 and 9.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applicationservices/core_printing/pmidleprocptr)*