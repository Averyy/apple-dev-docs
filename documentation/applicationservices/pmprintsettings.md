# PMPrintSettings

**Framework**: Application Services  
**Kind**: tdef

An opaque type that stores the settings in the Print dialog.

**Availability**:
- macOS 10.0+

## Declaration

```swift
typealias PMPrintSettings = OpaquePointer
```

#### Discussion

Your application uses print settings objects to store information such as the number of copies and the range of pages to print in a printing session. To create a print settings object, you use the function [`PMCreatePrintSettings(_:)`](1463239-pmcreateprintsettings.md). A new print settings object is empty and unusable until you call [`PMSessionDefaultPrintSettings(_:_:)`](1460138-pmsessiondefaultprintsettings.md) or [`PMCopyPrintSettings(_:_:)`](1462491-pmcopyprintsettings.md) to initialize the settings. You can also use the functions [`PMSetPrintSettingsExtendedData`](core_printing/1805491-pmsetprintsettingsextendeddata.md) and [`PMGetPrintSettingsExtendedData`](core_printing/1805488-pmgetprintsettingsextendeddata.md) to store and retrieve application-specific data in a print settings object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applicationservices/pmprintsettings)*