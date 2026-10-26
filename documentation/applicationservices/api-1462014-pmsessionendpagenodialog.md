# PMSessionEndPageNoDialog(_:)

**Framework**: Application Services  
**Kind**: func  
**Role**: Function

Indicates the end of drawing the current page for the specified printing session.

**Availability**:
- macOS 10.2+

## Declaration

```swift
func PMSessionEndPageNoDialog(_ printSession: PMPrintSession) -> OSStatus
```

```c
OSStatus PMSessionEndPageNoDialog(PMPrintSession printSession);
```

#### Return Value

A result code. See [Result Codes](./core_printing.md#1670007).

#### Discussion

This function is similar to the function `PMSessionEndPage` except that the printing status dialog is suppressed.

You must call this function between the creation and release of a printing session. See the function [`PMCreateSession(_:)`](./api-1463247-pmcreatesession.md). You must call the functions `PMSessionBeginPageNoDialog` and `PMSessionEndPageNoDialog` within the scope of calls to the `Begin` print job function ([`PMSessionBeginCGDocumentNoDialog(_:_:_:)`](./api-1460101-pmsessionbegincgdocumentnodialog.md)) and the `End` print job function ([`PMSessionEndDocumentNoDialog(_:)`](./api-1464527-pmsessionenddocumentnodialog.md)).

If the function `PMSessionBeginPageNoDialog` returns `noErr`, you must later call the function `PMSessionEndPageNoDialog`, even if errors occur within the scope of `PMSessionBeginPageNoDialog` and `PMSessionEndPageNoDialog`. You should not call `PMSessionEndPageNoDialog` if `PMSessionBeginPageNoDialog` returns an error.

## Parameters

- `printSession`: The printing session that provides a context for the print job.

## See Also

### Print Loop Functions
- [func PMSessionBeginCGDocumentNoDialog(PMPrintSession, PMPrintSettings, PMPageFormat) -> OSStatus](./api-1460101-pmsessionbegincgdocumentnodialog.md)
  Begins a print job that draws into a Quartz graphics context and suppresses the printing status dialog.
- [func PMSessionEndDocumentNoDialog(PMPrintSession) -> OSStatus](./api-1464527-pmsessionenddocumentnodialog.md)
  Ends a print job started by calling the function [`PMSessionBeginCGDocumentNoDialog(_:_:_:)`](./api-1460101-pmsessionbegincgdocumentnodialog.md) or [PMSessionBeginDocumentNoDialog](./core_printing/api-1805538-pmsessionbegindocumentnodialog.md).
- [func PMSessionBeginPageNoDialog(PMPrintSession, PMPageFormat?, UnsafePointer<PMRect>?) -> OSStatus](./api-1463416-pmsessionbeginpagenodialog.md)
  Starts a new page for printing in the specified printing session and suppresses the printing status dialog.
- [PMSessionBeginDocumentNoDialog](./core_printing/api-1805538-pmsessionbegindocumentnodialog.md)
  Begins a print job that, by default, draws into a QuickDraw graphics port, and suppresses the printing status dialog.
- [PMSessionSetIdleProc](./core_printing/api-1805540-pmsessionsetidleproc.md)
  Installs an idle callback function in your print loop.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applicationservices/1462014-pmsessionendpagenodialog)*