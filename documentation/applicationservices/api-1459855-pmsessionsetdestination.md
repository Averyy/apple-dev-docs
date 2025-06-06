# PMSessionSetDestination(_:_:_:_:_:)

**Framework**: Application Services  
**Kind**: func

Sets the destination location, format, and type for a print job.

**Availability**:
- macOS 10.1+

## Declaration

```swift
func PMSessionSetDestination(_ printSession: PMPrintSession, _ printSettings: PMPrintSettings, _ destType: PMDestinationType, _ destFormat: CFString?, _ destLocation: CFURL?) -> OSStatus
```

#### Return_value

A result code. See [`Result Codes`](core_printing#1670007.md).

#### Discussion

You can use the function `PMSessionSetDestination` when you want to send print output to a file without requiring user interaction. You must call this function between the creation and release of a printing session. See the function [`PMCreateSession(_:)`](1463247-pmcreatesession.md).

## Parameters

- `printSession`: The printing session that provides a context for the print job.
- `printSettings`: The print settings for the print job whose destination you want to set.
- `destType`: See   for a complete description of destination types you can specify.
- `destFormat`: The MIME type to be generated for the specified destination type. Pass   if you want to use the default format for the specified destination type. To obtain a list of valid formats for a given destination type, use the function  .
- `destLocation`: A reference to a Core Foundation URL that specifies a destination location. You can provide this if the destination type supports a destination location. Otherwise, pass  . For example, if the destination type is a file ( ) you can supply a file system URL to specify where the file resides.

## See Also

- [func PMSessionGetDestinationType(PMPrintSession, PMPrintSettings, UnsafeMutablePointer<PMDestinationType>) -> OSStatus](1461071-pmsessiongetdestinationtype.md)
  Obtains the output destination for a print job.
- [func PMSessionCopyDestinationFormat(PMPrintSession, PMPrintSettings, UnsafeMutablePointer<Unmanaged<CFString>?>) -> OSStatus](1464266-pmsessioncopydestinationformat.md)
  Obtains the destination format for a print job.
- [func PMSessionCopyDestinationLocation(PMPrintSession, PMPrintSettings, UnsafeMutablePointer<Unmanaged<CFURL>?>) -> OSStatus](1462967-pmsessioncopydestinationlocation.md)
  Obtains a destination location for a print job.
- [func PMSessionCopyOutputFormatList(PMPrintSession, PMDestinationType, UnsafeMutablePointer<Unmanaged<CFArray>?>) -> OSStatus](1461332-pmsessioncopyoutputformatlist.md)
  Obtains an array of destination formats supported by the current print destination. 


---

*[View on Apple Developer](https://developer.apple.com/documentation/applicationservices/1459855-pmsessionsetdestination)*