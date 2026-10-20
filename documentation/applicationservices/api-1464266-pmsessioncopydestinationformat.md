# PMSessionCopyDestinationFormat(_:_:_:)

**Framework**: Application Services  
**Kind**: func  
**Role**: Function

Obtains the destination format for a print job.

**Availability**:
- macOS 10.1+

## Declaration

```swift
func PMSessionCopyDestinationFormat(_ printSession: PMPrintSession, _ printSettings: PMPrintSettings, _ destFormatP: UnsafeMutablePointer<Unmanaged<CFString>?>) -> OSStatus
```

```c
OSStatus PMSessionCopyDestinationFormat(PMPrintSession printSession, PMPrintSettings printSettings, CFStringRef  _Nullable *destFormatP);
```

#### Return Value

A result code. See [Result Codes](./core_printing.md#1670007).

#### Discussion

You must call this function between the creation and release of a printing session. See the function [`PMCreateSession(_:)`](./api-1463247-pmcreatesession.md).

## Parameters

- `printSession`: The printing session that provides a context for the print job.
- `printSettings`: The print settings object for the print job whose destination format you want to obtain.
- `destFormatP`: A pointer to your [`CFString`](../CoreFoundation/cfstring.md) variable. On return, the variable refers to a Core Foundation string that contains the destination format for the print job. You are responsible for releasing the string. Currently, there are two possible values: `kPMDocumentFormatPDF` or `kPMDocumentFormatPostScript`.

  If an error occurs, the variable is set to `NULL`. If the function executes without error  and the variable is set to `NULL`, the print job is set to use the default destination format.

## See Also

### Accessing the Print Job Destination
- [func PMSessionSetDestination(PMPrintSession, PMPrintSettings, PMDestinationType, CFString?, CFURL?) -> OSStatus](./api-1459855-pmsessionsetdestination.md)
  Sets the destination location, format, and type for a print job.
- [func PMSessionGetDestinationType(PMPrintSession, PMPrintSettings, UnsafeMutablePointer<PMDestinationType>) -> OSStatus](./api-1461071-pmsessiongetdestinationtype.md)
  Obtains the output destination for a print job.
- [func PMSessionCopyDestinationLocation(PMPrintSession, PMPrintSettings, UnsafeMutablePointer<Unmanaged<CFURL>?>) -> OSStatus](./api-1462967-pmsessioncopydestinationlocation.md)
  Obtains a destination location for a print job.
- [func PMSessionCopyOutputFormatList(PMPrintSession, PMDestinationType, UnsafeMutablePointer<Unmanaged<CFArray>?>) -> OSStatus](./api-1461332-pmsessioncopyoutputformatlist.md)
  Obtains an array of destination formats supported by the current print destination. 


---

*[View on Apple Developer](https://developer.apple.com/documentation/applicationservices/1464266-pmsessioncopydestinationformat)*