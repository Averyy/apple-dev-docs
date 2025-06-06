# PMPrintSettingsCreateDataRepresentation(_:_:_:)

**Framework**: Application Services  
**Kind**: func

Creates a data representation of a print settings object.

**Availability**:
- macOS 10.5+

## Declaration

```swift
func PMPrintSettingsCreateDataRepresentation(_ printSettings: PMPrintSettings, _ data: UnsafeMutablePointer<Unmanaged<CFData>?>, _ format: PMDataFormat) -> OSStatus
```

#### Return_value

A result code. See [`Result Codes`](core_printing#1670007.md).

#### Discussion

This function is typically used to convert a print settings object into a data representation suitable for storage in a user document. For information about using a Core Foundation data object, see `CFData`.

Before calling this function, you should call the function [`PMSessionValidatePrintSettings(_:_:_:)`](1458994-pmsessionvalidateprintsettings.md) to make sure the print settings object contains valid values.

Apple recommends that you do not reuse the print settings information if the user prints the document again. The information supplied by the user in the Print dialog should pertain to the document only while the document prints, so there is no need to save the print settings object.

## Parameters

- `printSettings`: The print settings object to convert.
- `data`: A pointer to your   variable. On return, the variable refers to a new Core Foundation data object that contains a representation of the specified print settings object in the specified data format. You are responsible for releasing the data object.
- `format`: See   for a full description of these formats.

## See Also

- [func PMCreatePrintSettings(UnsafeMutablePointer<PMPrintSettings?>) -> OSStatus](1463239-pmcreateprintsettings.md)
  Creates a new print settings object.
- [func PMSessionDefaultPrintSettings(PMPrintSession, PMPrintSettings) -> OSStatus](1460138-pmsessiondefaultprintsettings.md)
  Assigns default parameter values to a print settings object for the specified printing session.
- [func PMSessionValidatePrintSettings(PMPrintSession, PMPrintSettings, UnsafeMutablePointer<DarwinBoolean>?) -> OSStatus](1458994-pmsessionvalidateprintsettings.md)
  Validates a print settings object within the context of the specified printing session.
- [func PMPrintSettingsCreateWithDataRepresentation(CFData, UnsafeMutablePointer<PMPrintSettings?>) -> OSStatus](1462203-pmprintsettingscreatewithdatarep.md)
  Creates a print settings object from a data representation.
- [func PMCopyPrintSettings(PMPrintSettings, PMPrintSettings) -> OSStatus](1462491-pmcopyprintsettings.md)
  Copies the settings from one print settings object into another. 
- [func PMPrintSettingsToOptions(PMPrintSettings, UnsafeMutablePointer<UnsafeMutablePointer<CChar>?>) -> OSStatus](1459069-pmprintsettingstooptions.md)
  Converts print settings into a CUPS options string.
- [func PMPrintSettingsToOptionsWithPrinterAndPageFormat(PMPrintSettings, PMPrinter, PMPageFormat?, UnsafeMutablePointer<UnsafeMutablePointer<CChar>?>) -> OSStatus](1459435-pmprintsettingstooptionswithprin.md)
  Converts print settings and page format data into a CUPS options string for a specified printer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applicationservices/1464570-pmprintsettingscreatedatareprese)*