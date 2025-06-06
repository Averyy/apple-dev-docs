# PMSessionBeginCGDocumentNoDialog(_:_:_:)

**Framework**: Application Services  
**Kind**: func

Begins a print job that draws into a Quartz graphics context and suppresses the printing status dialog.

**Availability**:
- macOS 10.4+

## Declaration

```swift
func PMSessionBeginCGDocumentNoDialog(_ printSession: PMPrintSession, _ printSettings: PMPrintSettings, _ pageFormat: PMPageFormat) -> OSStatus
```

#### Return_value

A result code. See [`Result Codes`](core_printing#1670007.md).

#### Discussion

This function starts a print job that draws directly into a Quartz graphics context and should be called within your application’s print loop. This function is similar to the function `PMSessionBeginCGDocument` except that the printing status dialog is suppressed.

You must call `PMSessionBeginCGDocumentNoDialog` between the creation and release of a printing session. See the function [`PMCreateSession(_:)`](1463247-pmcreatesession.md). If you present a printing dialog before you call `PMSessionBeginCGDocumentNoDialog`, when calling this function you should use the same [`PMPrintSession`](pmprintsession.md) object you used to present the dialog.

Before you call `PMSessionBeginCGDocumentNoDialog`, you should call [`PMSessionValidatePrintSettings(_:_:_:)`](1458994-pmsessionvalidateprintsettings.md) and [`PMSessionValidatePageFormat(_:_:_:)`](1459090-pmsessionvalidatepageformat.md) to make sure the specified print settings and page format objects are updated and valid. After you call `PMSessionBeginCGDocumentNoDialog`, if you call a function that changes the specified print settings or page format object, the change is ignored for the current print job.

During the print job, the caller cannot obtain a Quickdraw graphics port for the printing session but can only obtain a Quartz graphics context. As a result, this function should be used in conjunction with [`PMSessionGetCGGraphicsContext(_:_:)`](1461952-pmsessiongetcggraphicscontext.md) instead of [`PMSessionGetGraphicsContext`](core_printing/1805529-pmsessiongetgraphicscontext.md).

This function must be called before its corresponding `End` function ([`PMSessionEndDocumentNoDialog(_:)`](1464527-pmsessionenddocumentnodialog.md)). If the function `PMSessionBeginCGDocumentNoDialog` returns `noErr`, you must later call the `End` function, even if errors occur within the scope of the `Begin` and `End` functions.

The printing system automatically handles printing multiple copies. Your application does not need to perform any tasks other than specifying the number of copies in the printing session.

## Parameters

- `printSession`: The printing session that provides a context for the new print job.
- `printSettings`: The print settings to use for the new print job.
- `pageFormat`: The page format to use for the new print job.

## See Also

- [func PMSessionEndDocumentNoDialog(PMPrintSession) -> OSStatus](1464527-pmsessionenddocumentnodialog.md)
  Ends a print job started by calling the function [`PMSessionBeginCGDocumentNoDialog(_:_:_:)`](1460101-pmsessionbegincgdocumentnodialog.md) or [`PMSessionBeginDocumentNoDialog`](core_printing/1805538-pmsessionbegindocumentnodialog.md).
- [func PMSessionBeginPageNoDialog(PMPrintSession, PMPageFormat?, UnsafePointer<PMRect>?) -> OSStatus](1463416-pmsessionbeginpagenodialog.md)
  Starts a new page for printing in the specified printing session and suppresses the printing status dialog.
- [func PMSessionEndPageNoDialog(PMPrintSession) -> OSStatus](1462014-pmsessionendpagenodialog.md)
  Indicates the end of drawing the current page for the specified printing session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applicationservices/1460101-pmsessionbegincgdocumentnodialog)*