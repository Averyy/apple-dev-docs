# PMSessionBeginPageNoDialog(_:_:_:)

**Framework**: Application Services  
**Kind**: func

Starts a new page for printing in the specified printing session and suppresses the printing status dialog.

**Availability**:
- macOS 10.2+

## Declaration

```swift
func PMSessionBeginPageNoDialog(_ printSession: PMPrintSession, _ pageFormat: PMPageFormat?, _ pageFrame: UnsafePointer<PMRect>?) -> OSStatus
```

#### Return_value

A result code. If the user cancels the print job, this function returns `kPMCancel`.

#### Discussion

This function is similar to the function `PMSessionBeginPage` except that the function `PMSessionBeginPageNoDialog` suppresses the printing status dialog. You must call this function between the creation and release of a printing session. See the function [`PMCreateSession(_:)`](1463247-pmcreatesession.md). You must call the functions `PMSessionBeginPageNoDialog` and [`PMSessionEndPageNoDialog(_:)`](1462014-pmsessionendpagenodialog.md) within the scope of calls to the `Begin` print job function ([`PMSessionBeginCGDocumentNoDialog(_:_:_:)`](1460101-pmsessionbegincgdocumentnodialog.md)) and the `End` print job function ([`PMSessionEndDocumentNoDialog(_:)`](1464527-pmsessionenddocumentnodialog.md)).

You should call the function [`PMSessionError(_:)`](1460003-pmsessionerror.md) immediately before you call `PMSessionBeginPageNoDialog`. If `PMSessionError` returns an error, then you should not call the function `PMSessionBeginPageNoDialog`. Because `PMSessionBeginPage` also initializes the printing graphics context, your application should not make assumptions about the state of the context (for example, the current font) between successive pages. After each call to `PMSessionBeginPageNoDialog`, your application should call [`PMSessionGetCGGraphicsContext(_:_:)`](1461952-pmsessiongetcggraphicscontext.md) to obtain the current printing context.

If the function `PMSessionBeginPageNoDialog` returns `noErr`, you must later call the function `PMSessionEndPageNoDialog`, even if errors occur within the scope of `PMSessionBeginPageNoDialog` and `PMSessionEndPageNoDialog`.

The printing system automatically handles printing multiple copies. Your application does not need to perform any tasks other than specifying the number of copies in the printing session.

##### 1771101

Prior to OS X v10.5, the `pageFormat` parameter is ignored. In macOS 10.5 and later, the printing system supports multiple orientations within a print job. When you call this function and supply a page format, the orientation specified in the page format is used for the current page. Other settings in the page format, such as paper size or scaling, are ignored.

## Parameters

- `printSession`: The printing session that provides a context for the print job.
- `pageFormat`: The page format for the new page. If you pass  , the printing system uses the page format you passed to  .
- `pageFrame`: You should pass  , as this parameter is currently unsupported.

## See Also

- [func PMSessionBeginCGDocumentNoDialog(PMPrintSession, PMPrintSettings, PMPageFormat) -> OSStatus](1460101-pmsessionbegincgdocumentnodialog.md)
  Begins a print job that draws into a Quartz graphics context and suppresses the printing status dialog.
- [func PMSessionEndDocumentNoDialog(PMPrintSession) -> OSStatus](1464527-pmsessionenddocumentnodialog.md)
  Ends a print job started by calling the function [`PMSessionBeginCGDocumentNoDialog(_:_:_:)`](1460101-pmsessionbegincgdocumentnodialog.md) or [`PMSessionBeginDocumentNoDialog`](core_printing/1805538-pmsessionbegindocumentnodialog.md).
- [func PMSessionEndPageNoDialog(PMPrintSession) -> OSStatus](1462014-pmsessionendpagenodialog.md)
  Indicates the end of drawing the current page for the specified printing session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applicationservices/1463416-pmsessionbeginpagenodialog)*