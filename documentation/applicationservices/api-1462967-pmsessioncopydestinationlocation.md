# PMSessionCopyDestinationLocation(_:_:_:)

**Framework**: Application Services  
**Kind**: func

Obtains a destination location for a print job.

**Availability**:
- macOS 10.1+

## Declaration

```swift
func PMSessionCopyDestinationLocation(_ printSession: PMPrintSession, _ printSettings: PMPrintSettings, _ destLocationP: UnsafeMutablePointer<Unmanaged<CFURL>?>) -> OSStatus
```

#### Return_value

A result code. See [`Result Codes`](core_printing#1670007.md).

#### Discussion

You must call this function between the creation and release of a printing session. See the function [`PMCreateSession(_:)`](1463247-pmcreatesession.md).

Some destination types define a specific kind of destination location for a print job. For example, the destination type `kPMDestinationFile` uses a file system URL to specify where a new file should be created for the print job’s output.

## Parameters

- `printSession`: The printing session that provides a context for the print job.
- `printSettings`: The print settings for the print job whose destination location you want to obtain.
- `destLocationP`: A pointer to your   variable. On return, the variable refers to a Core Foundation URL that specifies the destination location of the print job. You are responsible for releasing the URL. If   is returned and the function executes without error (result code is  ), the print job uses the default destination location for the current destination type. If an error occurs, the variable is set to  . 

## See Also

- [func PMSessionSetDestination(PMPrintSession, PMPrintSettings, PMDestinationType, CFString?, CFURL?) -> OSStatus](1459855-pmsessionsetdestination.md)
  Sets the destination location, format, and type for a print job.
- [func PMSessionGetDestinationType(PMPrintSession, PMPrintSettings, UnsafeMutablePointer<PMDestinationType>) -> OSStatus](1461071-pmsessiongetdestinationtype.md)
  Obtains the output destination for a print job.
- [func PMSessionCopyDestinationFormat(PMPrintSession, PMPrintSettings, UnsafeMutablePointer<Unmanaged<CFString>?>) -> OSStatus](1464266-pmsessioncopydestinationformat.md)
  Obtains the destination format for a print job.
- [func PMSessionCopyOutputFormatList(PMPrintSession, PMDestinationType, UnsafeMutablePointer<Unmanaged<CFArray>?>) -> OSStatus](1461332-pmsessioncopyoutputformatlist.md)
  Obtains an array of destination formats supported by the current print destination. 


---

*[View on Apple Developer](https://developer.apple.com/documentation/applicationservices/1462967-pmsessioncopydestinationlocation)*