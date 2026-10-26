# PMSessionSetIdleProc

**Framework**: Application Services  
**Kind**: func

Installs an idle callback function in your print loop.

> **Deprecated**: There is no replacement; this function was included to facilitate porting legacy applications to macOS, but it serves no useful purpose.

## Declaration

```c
OSStatus PMSessionSetIdleProc (
   PMPrintSession printSession,
   PMIdleUPP idleProc
);
```

#### Return Value

A result code. See [Result Codes](../core_printing.md#1670007).

#### Overview

You do not need this function in macOS. Instead, use the standard idle proc. 

## Parameters

- `printSession`: The printing session that provides a context for the print job.
- `idleProc`: A universal procedure pointer to your idle function. Your idle function is defined by the callback [PMIdleProcPtr](./pmidleprocptr.md).

## See Also

### Print Loop Functions
- [PMSessionBeginCGDocumentNoDialog](../api-1460101-pmsessionbegincgdocumentnodialog.md)
  Begins a print job that draws into a Quartz graphics context and suppresses the printing status dialog.
- [PMSessionBeginDocumentNoDialog](./api-1805538-pmsessionbegindocumentnodialog.md)
  Begins a print job that, by default, draws into a QuickDraw graphics port, and suppresses the printing status dialog.
- [PMSessionEndDocumentNoDialog](../api-1464527-pmsessionenddocumentnodialog.md)
  Ends a print job started by calling the function [`PMSessionBeginCGDocumentNoDialog`](../api-1460101-pmsessionbegincgdocumentnodialog.md) or [PMSessionBeginDocumentNoDialog](./api-1805538-pmsessionbegindocumentnodialog.md).
- [PMSessionBeginPageNoDialog](../api-1463416-pmsessionbeginpagenodialog.md)
  Starts a new page for printing in the specified printing session and suppresses the printing status dialog.
- [PMSessionEndPageNoDialog](../api-1462014-pmsessionendpagenodialog.md)
  Indicates the end of drawing the current page for the specified printing session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applicationservices/core_printing/1805540-pmsessionsetidleproc)*