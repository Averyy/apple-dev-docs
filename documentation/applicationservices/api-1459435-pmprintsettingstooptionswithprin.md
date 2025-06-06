# PMPrintSettingsToOptionsWithPrinterAndPageFormat(_:_:_:_:)

**Framework**: Application Services  
**Kind**: func

Converts print settings and page format data into a CUPS options string for a specified printer.

**Availability**:
- macOS 10.5+

## Declaration

```swift
func PMPrintSettingsToOptionsWithPrinterAndPageFormat(_ settings: PMPrintSettings, _ printer: PMPrinter, _ pageFormat: PMPageFormat?, _ options: UnsafeMutablePointer<UnsafeMutablePointer<CChar>?>) -> OSStatus
```

#### Return_value

A result code. See [`Result Codes`](core_printing#1670007.md).

#### Discussion

This function creates a CUPS options string for the destination printer that captures the data in the specified print settings and page format objects. For example, you could pass this string to the function [`PMWorkflowSubmitPDFWithOptions(_:_:_:_:)`](1463747-pmworkflowsubmitpdfwithoptions.md) to submit a PDF file for workflow processing. You could also use the options string to run a CUPS filter directly.

## Parameters

- `settings`: The print settings to convert.
- `printer`: The printer to use for converting the print settings. This parameter must not be  .
- `pageFormat`: The page format to convert, or   to specify default page format data.
- `options`: A pointer to a C string. On return, a CUPS option string with the specified print settings and page format data, or   if the data could not be converted. The function allocates storage for the string. You are responsible for freeing the storage.

## See Also

- [func PMCreatePrintSettings(UnsafeMutablePointer<PMPrintSettings?>) -> OSStatus](1463239-pmcreateprintsettings.md)
  Creates a new print settings object.
- [func PMSessionDefaultPrintSettings(PMPrintSession, PMPrintSettings) -> OSStatus](1460138-pmsessiondefaultprintsettings.md)
  Assigns default parameter values to a print settings object for the specified printing session.
- [func PMSessionValidatePrintSettings(PMPrintSession, PMPrintSettings, UnsafeMutablePointer<DarwinBoolean>?) -> OSStatus](1458994-pmsessionvalidateprintsettings.md)
  Validates a print settings object within the context of the specified printing session.
- [func PMPrintSettingsCreateDataRepresentation(PMPrintSettings, UnsafeMutablePointer<Unmanaged<CFData>?>, PMDataFormat) -> OSStatus](1464570-pmprintsettingscreatedatareprese.md)
  Creates a data representation of a print settings object.
- [func PMPrintSettingsCreateWithDataRepresentation(CFData, UnsafeMutablePointer<PMPrintSettings?>) -> OSStatus](1462203-pmprintsettingscreatewithdatarep.md)
  Creates a print settings object from a data representation.
- [func PMCopyPrintSettings(PMPrintSettings, PMPrintSettings) -> OSStatus](1462491-pmcopyprintsettings.md)
  Copies the settings from one print settings object into another. 
- [func PMPrintSettingsToOptions(PMPrintSettings, UnsafeMutablePointer<UnsafeMutablePointer<CChar>?>) -> OSStatus](1459069-pmprintsettingstooptions.md)
  Converts print settings into a CUPS options string.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applicationservices/1459435-pmprintsettingstooptionswithprin)*