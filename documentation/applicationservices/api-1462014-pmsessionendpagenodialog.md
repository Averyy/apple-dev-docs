# PMSessionEndPageNoDialog(_:)

**Framework**: Application Services  
**Kind**: func

Indicates the end of drawing the current page for the specified printing session.

**Availability**:
- macOS 10.2+

## Declaration

```swift
func PMSessionEndPageNoDialog(_ printSession: PMPrintSession) -> OSStatus
```

#### Return_value

A result code. See [`Result Codes`](core_printing#1670007.md).

#### Discussion

This function is similar to the function `PMSessionEndPage` except that the printing status dialog is suppressed.

You must call this function between the creation and release of a printing session. See the function [`PMCreateSession(_:)`](1463247-pmcreatesession.md). You must call the functions `PMSessionBeginPageNoDialog` and `PMSessionEndPageNoDialog` within the scope of calls to the `Begin` print job function ([`PMSessionBeginCGDocumentNoDialog(_:_:_:)`](1460101-pmsessionbegincgdocumentnodialog.md)) and the `End` print job function ([`PMSessionEndDocumentNoDialog(_:)`](1464527-pmsessionenddocumentnodialog.md)).

If the function `PMSessionBeginPageNoDialog` returns `noErr`, you must later call the function `PMSessionEndPageNoDialog`, even if errors occur within the scope of `PMSessionBeginPageNoDialog` and `PMSessionEndPageNoDialog`. You should not call `PMSessionEndPageNoDialog` if `PMSessionBeginPageNoDialog` returns an error.

## Parameters

- `printSession`: The printing session that provides a context for the print job.

## See Also

- [func PMSessionBeginCGDocumentNoDialog(PMPrintSession, PMPrintSettings, PMPageFormat) -> OSStatus](1460101-pmsessionbegincgdocumentnodialog.md)
  Begins a print job that draws into a Quartz graphics context and suppresses the printing status dialog.
- [func PMSessionEndDocumentNoDialog(PMPrintSession) -> OSStatus](1464527-pmsessionenddocumentnodialog.md)
  Ends a print job started by calling the function [`PMSessionBeginCGDocumentNoDialog(_:_:_:)`](1460101-pmsessionbegincgdocumentnodialog.md) or [`PMSessionBeginDocumentNoDialog`](core_printing/1805538-pmsessionbegindocumentnodialog.md).
- [func PMSessionBeginPageNoDialog(PMPrintSession, PMPageFormat?, UnsafePointer<PMRect>?) -> OSStatus](1463416-pmsessionbeginpagenodialog.md)
  Starts a new page for printing in the specified printing session and suppresses the printing status dialog.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applicationservices/1462014-pmsessionendpagenodialog)*