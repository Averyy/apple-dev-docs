# PMSessionGetDataFromSession(_:_:_:)

**Framework**: Application Services  
**Kind**: func  
**Role**: Function

Obtains application-specific data previously stored in a printing session object.

**Availability**:
- macOS 10.0+

## Declaration

```swift
func PMSessionGetDataFromSession(_ printSession: PMPrintSession, _ key: CFString, _ data: UnsafeMutablePointer<Unmanaged<CFTypeRef>?>) -> OSStatus
```

```c
OSStatus PMSessionGetDataFromSession(PMPrintSession printSession, CFStringRef key, CFTypeRef  _Nullable *data);
```

#### Return Value

A result code. See [Result Codes](./core_printing.md#1670007).

#### Discussion

You must call this function between the creation and release of a printing session. See the function [`PMCreateSession(_:)`](./api-1463247-pmcreatesession.md).

## Parameters

- `printSession`: The printing session whose data you want to obtain.
- `key`: The key that uniquely identifies the data to be retrieved. You specify this key when you store the data using the function [`PMSessionSetDataInSession(_:_:_:)`](./api-1461902-pmsessionsetdatainsession.md). 
- `data`: A pointer to your [`CFTypeRef`](../CoreFoundation/cftyperef.md) variable. On return, the variable refers to the data retrieved from the printing session.

## See Also

### Accessing Data in Printing Session Objects
- [func PMSessionSetDataInSession(PMPrintSession, CFString, CFTypeRef) -> OSStatus](./api-1461902-pmsessionsetdatainsession.md)
  Stores your application-specific data in a printing session object.
- [func PMSessionGetCurrentPrinter(PMPrintSession, UnsafeMutablePointer<PMPrinter?>) -> OSStatus](./api-1458998-pmsessiongetcurrentprinter.md)
  Obtains the current printer associated with a printing session.
- [func PMSessionSetCurrentPMPrinter(PMPrintSession, PMPrinter) -> OSStatus](./api-1461096-pmsessionsetcurrentpmprinter.md)
  Changes the current printer for a printing session.
- [func PMSessionGetCGGraphicsContext(PMPrintSession, UnsafeMutablePointer<Unmanaged<CGContext>?>) -> OSStatus](./api-1461952-pmsessiongetcggraphicscontext.md)
  Obtains the Quartz graphics context for the current page in a printing session.
- [func PMSessionError(PMPrintSession) -> OSStatus](./api-1460003-pmsessionerror.md)
  Obtains the result code for any error returned by the printing session. 
- [func PMSessionSetError(PMPrintSession, OSStatus) -> OSStatus](./api-1460216-pmsessionseterror.md)
  Sets the value of the current result code for the specified printing session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applicationservices/1462964-pmsessiongetdatafromsession)*