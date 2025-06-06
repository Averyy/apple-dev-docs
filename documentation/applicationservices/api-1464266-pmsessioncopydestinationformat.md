# PMSessionCopyDestinationFormat(_:_:_:)

**Framework**: Application Services  
**Kind**: func

Obtains the destination format for a print job.

**Availability**:
- macOS 10.1+

## Declaration

```swift
func PMSessionCopyDestinationFormat(_ printSession: PMPrintSession, _ printSettings: PMPrintSettings, _ destFormatP: UnsafeMutablePointer<Unmanaged<CFString>?>) -> OSStatus
```

#### Return_value

A result code. See [`Result Codes`](core_printing#1670007.md).

#### Discussion

You must call this function between the creation and release of a printing session. See the function [`PMCreateSession(_:)`](1463247-pmcreatesession.md).

## Parameters

- `printSession`: The printing session that provides a context for the print job.
- `printSettings`: The print settings object for the print job whose destination format you want to obtain.
- `destFormatP`: If an error occurs, the variable is set to  . If the function executes without error  and the variable is set to  , the print job is set to use the default destination format.

## See Also

- [func PMSessionSetDestination(PMPrintSession, PMPrintSettings, PMDestinationType, CFString?, CFURL?) -> OSStatus](1459855-pmsessionsetdestination.md)
  Sets the destination location, format, and type for a print job.
- [func PMSessionGetDestinationType(PMPrintSession, PMPrintSettings, UnsafeMutablePointer<PMDestinationType>) -> OSStatus](1461071-pmsessiongetdestinationtype.md)
  Obtains the output destination for a print job.
- [func PMSessionCopyDestinationLocation(PMPrintSession, PMPrintSettings, UnsafeMutablePointer<Unmanaged<CFURL>?>) -> OSStatus](1462967-pmsessioncopydestinationlocation.md)
  Obtains a destination location for a print job.
- [func PMSessionCopyOutputFormatList(PMPrintSession, PMDestinationType, UnsafeMutablePointer<Unmanaged<CFArray>?>) -> OSStatus](1461332-pmsessioncopyoutputformatlist.md)
  Obtains an array of destination formats supported by the current print destination. 


---

*[View on Apple Developer](https://developer.apple.com/documentation/applicationservices/1464266-pmsessioncopydestinationformat)*