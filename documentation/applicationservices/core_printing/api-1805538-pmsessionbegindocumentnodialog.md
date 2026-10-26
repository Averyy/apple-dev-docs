# PMSessionBeginDocumentNoDialog

**Framework**: Application Services  
**Kind**: func

Begins a print job that, by default, draws into a QuickDraw graphics port, and suppresses the printing status dialog.

> **Deprecated**: Use [`PMSessionBeginCGDocumentNoDialog`](../api-1460101-pmsessionbegincgdocumentnodialog.md) instead.

## Declaration

```c
OSStatus PMSessionBeginDocumentNoDialog (
   PMPrintSession printSession,
   PMPrintSettings printSettings,
   PMPageFormat pageFormat
);
```

#### Return Value

A result code. See [Result Codes](../core_printing.md#1670007).

#### Overview

The function `PMSessionBeginDocumentNoDialog` starts a print job and should be called within your application’s print loop. This function is similar to the function PMSessionBeginDocument except that the printing status dialog is suppressed.

You must call this function between the creation and release of a printing session. See the function [`PMCreateSession`](../api-1463247-pmcreatesession.md). If you present a printing dialog before you call `PMSessionBeginDocumentNoDialog`, when calling this function you should use the same [`PMPrintSession`](../pmprintsession.md) object you used to present the dialog.

Before you call `PMSessionBeginDocumentNoDialog`, you should call [`PMSessionValidatePrintSettings`](../api-1458994-pmsessionvalidateprintsettings.md) and [`PMSessionValidatePageFormat`](../api-1459090-pmsessionvalidatepageformat.md) to make sure the specified print settings and page format objects are updated and valid. After you call `PMSessionBeginDocumentNoDialog`, if you call a function that changes the specified print settings or page format object, the change is ignored for the current print job.

This function must be called before its corresponding `End` function ([`PMSessionEndDocumentNoDialog`](../api-1464527-pmsessionenddocumentnodialog.md)). If the function `PMSessionBeginDocumentNoDialog` returns `noErr`, you must call the `End` function, even if errors occur within the scope of the `Begin` and `End` functions.

The printing system automatically handles printing multiple copies. Your application does not need to perform any tasks other than specifying the number of copies in the printing session.

##### Special Considerations

In macOS 10.4 and later, Apple recommends using the function [`PMSessionBeginCGDocumentNoDialog`](../api-1460101-pmsessionbegincgdocumentnodialog.md) instead of this function. QuickDraw is deprecated and your application should be using Quartz 2D for its rendering.

## Parameters

- `printSession`: The printing session that provides a context for the new print job.
- `printSettings`: The print settings to use for the new print job.
- `pageFormat`: The page format to use for the new print job.

## See Also

### Print Loop Functions
- [PMSessionBeginCGDocumentNoDialog](../api-1460101-pmsessionbegincgdocumentnodialog.md)
  Begins a print job that draws into a Quartz graphics context and suppresses the printing status dialog.
- [PMSessionEndDocumentNoDialog](../api-1464527-pmsessionenddocumentnodialog.md)
  Ends a print job started by calling the function [`PMSessionBeginCGDocumentNoDialog`](../api-1460101-pmsessionbegincgdocumentnodialog.md) or [PMSessionBeginDocumentNoDialog](./api-1805538-pmsessionbegindocumentnodialog.md).
- [PMSessionBeginPageNoDialog](../api-1463416-pmsessionbeginpagenodialog.md)
  Starts a new page for printing in the specified printing session and suppresses the printing status dialog.
- [PMSessionEndPageNoDialog](../api-1462014-pmsessionendpagenodialog.md)
  Indicates the end of drawing the current page for the specified printing session.
- [PMSessionSetIdleProc](./api-1805540-pmsessionsetidleproc.md)
  Installs an idle callback function in your print loop.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applicationservices/core_printing/1805538-pmsessionbegindocumentnodialog)*