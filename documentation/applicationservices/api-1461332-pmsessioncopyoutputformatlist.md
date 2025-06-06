# PMSessionCopyOutputFormatList(_:_:_:)

**Framework**: Application Services  
**Kind**: func

Obtains an array of destination formats supported by the current print destination. 

**Availability**:
- macOS 10.1+

## Declaration

```swift
func PMSessionCopyOutputFormatList(_ printSession: PMPrintSession, _ destType: PMDestinationType, _ documentFormatP: UnsafeMutablePointer<Unmanaged<CFArray>?>) -> OSStatus
```

#### Return_value

A result code. See [`Result Codes`](core_printing#1670007.md).

#### Discussion

You must call this function between the creation and release of a printing session. See the function [`PMCreateSession(_:)`](1463247-pmcreatesession.md).

## Parameters

- `printSession`: The printing session that provides a context for the print job. The printer associated with this session is queried for the MIME types it supports.
- `destType`: A destination type that specifies the destination for which you want to obtain valid destination formats. See   for a list of the possible destination types a print job can have.
- `documentFormatP`: A pointer to your   variable. On return, the variable refers to a Core Foundation array that contains a list of destination formats that can be generated for the current print destination. See   for a list of some of the output formats that can be returned.

## See Also

- [func PMSessionSetDestination(PMPrintSession, PMPrintSettings, PMDestinationType, CFString?, CFURL?) -> OSStatus](1459855-pmsessionsetdestination.md)
  Sets the destination location, format, and type for a print job.
- [func PMSessionGetDestinationType(PMPrintSession, PMPrintSettings, UnsafeMutablePointer<PMDestinationType>) -> OSStatus](1461071-pmsessiongetdestinationtype.md)
  Obtains the output destination for a print job.
- [func PMSessionCopyDestinationFormat(PMPrintSession, PMPrintSettings, UnsafeMutablePointer<Unmanaged<CFString>?>) -> OSStatus](1464266-pmsessioncopydestinationformat.md)
  Obtains the destination format for a print job.
- [func PMSessionCopyDestinationLocation(PMPrintSession, PMPrintSettings, UnsafeMutablePointer<Unmanaged<CFURL>?>) -> OSStatus](1462967-pmsessioncopydestinationlocation.md)
  Obtains a destination location for a print job.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applicationservices/1461332-pmsessioncopyoutputformatlist)*