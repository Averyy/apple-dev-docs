# PMSessionEndDocumentNoDialog(_:)

**Framework**: Application Services  
**Kind**: func

Ends a print job started by calling the function [`PMSessionBeginCGDocumentNoDialog(_:_:_:)`](1460101-pmsessionbegincgdocumentnodialog.md) or [`PMSessionBeginDocumentNoDialog`](core_printing/1805538-pmsessionbegindocumentnodialog.md).

**Availability**:
- macOS 10.2+

## Declaration

```swift
func PMSessionEndDocumentNoDialog(_ printSession: PMPrintSession) -> OSStatus
```

#### Return_value

A result code. See [`Result Codes`](core_printing#1670007.md).

#### Discussion

This function is similar to the function `PMSessionEndDocument` except that the printing status dialog is suppressed.

This function is used to end a print job, and it should be called within your application’s print loop after the call to the function `PMSessionEndPageNoDialog` and before releasing the printing session. The same printing session that is created by the function `PMCreateSession` for the Print dialog should be used for the print loop.

The function `PMSessionEndDocumentNoDialog` must be called after its corresponding `Begin` function ([`PMSessionBeginCGDocumentNoDialog(_:_:_:)`](1460101-pmsessionbegincgdocumentnodialog.md) or [`PMSessionBeginDocumentNoDialog`](core_printing/1805538-pmsessionbegindocumentnodialog.md)). If the `Begin` function returns `noErr`, the function `PMSessionEndDocument` must be called, even if errors occur within the scope of the `Begin` and `End` functions. You should not call `PMSessionEndDocumentNoDialog` if the `Begin` function returns an error.

## Parameters

- `printSession`: The current printing session. On return, the printing session is no longer valid; however, you must still call the function   to release the object. 

## See Also

- [func PMSessionBeginCGDocumentNoDialog(PMPrintSession, PMPrintSettings, PMPageFormat) -> OSStatus](1460101-pmsessionbegincgdocumentnodialog.md)
  Begins a print job that draws into a Quartz graphics context and suppresses the printing status dialog.
- [func PMSessionBeginPageNoDialog(PMPrintSession, PMPageFormat?, UnsafePointer<PMRect>?) -> OSStatus](1463416-pmsessionbeginpagenodialog.md)
  Starts a new page for printing in the specified printing session and suppresses the printing status dialog.
- [func PMSessionEndPageNoDialog(PMPrintSession) -> OSStatus](1462014-pmsessionendpagenodialog.md)
  Indicates the end of drawing the current page for the specified printing session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applicationservices/1464527-pmsessionenddocumentnodialog)*