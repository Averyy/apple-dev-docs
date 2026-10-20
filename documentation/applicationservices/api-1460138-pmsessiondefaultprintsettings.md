# PMSessionDefaultPrintSettings(_:_:)

**Framework**: Application Services  
**Kind**: func  
**Role**: Function

Assigns default parameter values to a print settings object for the specified printing session.

**Availability**:
- macOS 10.0+

## Declaration

```swift
func PMSessionDefaultPrintSettings(_ printSession: PMPrintSession, _ printSettings: PMPrintSettings) -> OSStatus
```

```c
OSStatus PMSessionDefaultPrintSettings(PMPrintSession printSession, PMPrintSettings printSettings);
```

#### Return Value

A result code. See [Result Codes](./core_printing.md#1670007).

#### Discussion

You must call the function `PMSessionDefaultPrintSettings` between the creation and release of a printing session. See the function [`PMCreateSession(_:)`](./api-1463247-pmcreatesession.md). 

## Parameters

- `printSession`: The printing session for the specified print settings object.
- `printSettings`: The print settings object to which you want to assign default values.

## See Also

### Creating and Using Print Settings Objects
- [func PMCreatePrintSettings(UnsafeMutablePointer<PMPrintSettings?>) -> OSStatus](./api-1463239-pmcreateprintsettings.md)
  Creates a new print settings object.
- [func PMSessionValidatePrintSettings(PMPrintSession, PMPrintSettings, UnsafeMutablePointer<DarwinBoolean>?) -> OSStatus](./api-1458994-pmsessionvalidateprintsettings.md)
  Validates a print settings object within the context of the specified printing session.
- [func PMPrintSettingsCreateDataRepresentation(PMPrintSettings, UnsafeMutablePointer<Unmanaged<CFData>?>, PMDataFormat) -> OSStatus](./api-1464570-pmprintsettingscreatedatareprese.md)
  Creates a data representation of a print settings object.
- [func PMPrintSettingsCreateWithDataRepresentation(CFData, UnsafeMutablePointer<PMPrintSettings?>) -> OSStatus](./api-1462203-pmprintsettingscreatewithdatarep.md)
  Creates a print settings object from a data representation.
- [func PMCopyPrintSettings(PMPrintSettings, PMPrintSettings) -> OSStatus](./api-1462491-pmcopyprintsettings.md)
  Copies the settings from one print settings object into another. 
- [func PMPrintSettingsToOptions(PMPrintSettings, UnsafeMutablePointer<UnsafeMutablePointer<CChar>?>) -> OSStatus](./api-1459069-pmprintsettingstooptions.md)
  Converts print settings into a CUPS options string.
- [func PMPrintSettingsToOptionsWithPrinterAndPageFormat(PMPrintSettings, PMPrinter, PMPageFormat?, UnsafeMutablePointer<UnsafeMutablePointer<CChar>?>) -> OSStatus](./api-1459435-pmprintsettingstooptionswithprin.md)
  Converts print settings and page format data into a CUPS options string for a specified printer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applicationservices/1460138-pmsessiondefaultprintsettings)*