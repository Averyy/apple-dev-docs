# PMSessionGetDestinationType(_:_:_:)

**Framework**: Application Services  
**Kind**: func

Obtains the output destination for a print job.

**Availability**:
- macOS 10.1+

## Declaration

```swift
func PMSessionGetDestinationType(_ printSession: PMPrintSession, _ printSettings: PMPrintSettings, _ destTypeP: UnsafeMutablePointer<PMDestinationType>) -> OSStatus
```

#### Return_value

A result code. See [`Result Codes`](core_printing#1670007.md). 

#### Discussion

You must call this function between the creation and release of a printing session. See the function [`PMCreateSession(_:)`](1463247-pmcreatesession.md).

All of the destination types are stored in the print settings object except for `kPMDestinationPreview`, which is stored in the printing session object. If the destination type is set as preview, the preview setting overrides the destination set in the print settings object.

## Parameters

- `printSession`: The printing session that provides a context for the print job. This must be the same printing session used for the Print dialog. The printing session contains the preview setting, which can override the destination type in the print settings.
- `printSettings`: The print settings for the print job whose destination you want to obtain.
- `destTypeP`: See   for a complete description of the destination type constants.

## See Also

- [func PMSessionSetDestination(PMPrintSession, PMPrintSettings, PMDestinationType, CFString?, CFURL?) -> OSStatus](1459855-pmsessionsetdestination.md)
  Sets the destination location, format, and type for a print job.
- [func PMSessionCopyDestinationFormat(PMPrintSession, PMPrintSettings, UnsafeMutablePointer<Unmanaged<CFString>?>) -> OSStatus](1464266-pmsessioncopydestinationformat.md)
  Obtains the destination format for a print job.
- [func PMSessionCopyDestinationLocation(PMPrintSession, PMPrintSettings, UnsafeMutablePointer<Unmanaged<CFURL>?>) -> OSStatus](1462967-pmsessioncopydestinationlocation.md)
  Obtains a destination location for a print job.
- [func PMSessionCopyOutputFormatList(PMPrintSession, PMDestinationType, UnsafeMutablePointer<Unmanaged<CFArray>?>) -> OSStatus](1461332-pmsessioncopyoutputformatlist.md)
  Obtains an array of destination formats supported by the current print destination. 


---

*[View on Apple Developer](https://developer.apple.com/documentation/applicationservices/1461071-pmsessiongetdestinationtype)*