# PMPrintSettingsGetValue(_:_:_:)

**Framework**: Application Services  
**Kind**: func  
**Role**: Function

Obtains the value of a setting in a print settings object.

**Availability**:
- macOS 10.4+

## Declaration

```swift
func PMPrintSettingsGetValue(_ printSettings: PMPrintSettings, _ key: CFString, _ value: UnsafeMutablePointer<Unmanaged<CFTypeRef>?>) -> OSStatus
```

```c
OSStatus PMPrintSettingsGetValue(PMPrintSettings printSettings, CFStringRef key, CFTypeRef  _Nullable *value);
```

#### Return Value

A result code. See [Result Codes](./core_printing.md#1670007).

#### Discussion

This function, together with the function `PMPrintSettingsSetValue`, makes it possible to access print settings directly. 

## Parameters

- `printSettings`: The print settings object you want to access.
- `key`: A string constant that specifies the key for the desired setting. Some keys are currently defined in `PMTicket.h`; other keys are user-defined.
- `value`: A pointer to your Core Foundation variable. On return, the variable refers to a Core Foundation object that corresponds to the specified key. If no corresponding object exists, the variable is set to `NULL`.

## See Also

### Accessing Data in Print Settings Objects
- [func PMGetFirstPage(PMPrintSettings, UnsafeMutablePointer<UInt32>) -> OSStatus](./api-1460271-pmgetfirstpage.md)
  Obtains the number of the first page to be printed.
- [func PMSetFirstPage(PMPrintSettings, UInt32, Bool) -> OSStatus](./api-1461519-pmsetfirstpage.md)
  Sets the default page number of the first page to be printed.
- [func PMGetLastPage(PMPrintSettings, UnsafeMutablePointer<UInt32>) -> OSStatus](./api-1462747-pmgetlastpage.md)
  Obtains the number of the last page to be printed.
- [func PMSetLastPage(PMPrintSettings, UInt32, Bool) -> OSStatus](./api-1463595-pmsetlastpage.md)
  Sets the page number of the last page to be printed.
- [func PMGetPageRange(PMPrintSettings, UnsafeMutablePointer<UInt32>, UnsafeMutablePointer<UInt32>) -> OSStatus](./api-1459324-pmgetpagerange.md)
  Obtains the valid range of pages that can be printed.
- [func PMSetPageRange(PMPrintSettings, UInt32, UInt32) -> OSStatus](./api-1462294-pmsetpagerange.md)
  Sets the valid range of pages that can be printed.
- [func PMPrintSettingsGetJobName(PMPrintSettings, UnsafeMutablePointer<Unmanaged<CFString>?>) -> OSStatus](./api-1459233-pmprintsettingsgetjobname.md)
  Obtains the name of a print job.
- [func PMPrintSettingsSetJobName(PMPrintSettings, CFString) -> OSStatus](./api-1460149-pmprintsettingssetjobname.md)
  Specifies the name of a print job.
- [func PMGetCopies(PMPrintSettings, UnsafeMutablePointer<UInt32>) -> OSStatus](./api-1464480-pmgetcopies.md)
  Obtains the number of copies that the user requests to be printed.
- [func PMSetCopies(PMPrintSettings, UInt32, Bool) -> OSStatus](./api-1463804-pmsetcopies.md)
  Sets the initial value for the number of copies to be printed.
- [func PMGetCollate(PMPrintSettings, UnsafeMutablePointer<DarwinBoolean>) -> OSStatus](./api-1464492-pmgetcollate.md)
  Obtains a Boolean value that indicates whether the job collate option is selected.
- [func PMSetCollate(PMPrintSettings, Bool) -> OSStatus](./api-1463223-pmsetcollate.md)
  Specifies whether the job collate option is selected.
- [func PMGetDuplex(PMPrintSettings, UnsafeMutablePointer<PMDuplexMode>) -> OSStatus](./api-1458921-pmgetduplex.md)
  Obtains the selected duplex mode.
- [func PMSetDuplex(PMPrintSettings, PMDuplexMode) -> OSStatus](./api-1462000-pmsetduplex.md)
  Sets the duplex mode.
- [func PMPrintSettingsSetValue(PMPrintSettings, CFString, CFTypeRef?, Bool) -> OSStatus](./api-1461697-pmprintsettingssetvalue.md)
  Stores the value of a setting in a print settings object.
- [func PMPrintSettingsCopyAsDictionary(PMPrintSettings, UnsafeMutablePointer<Unmanaged<CFDictionary>?>) -> OSStatus](./api-1459088-pmprintsettingscopyasdictionary.md)
  Creates a dictionary that contains the settings in a print settings object.
- [func PMPrintSettingsCopyKeys(PMPrintSettings, UnsafeMutablePointer<Unmanaged<CFArray>?>) -> OSStatus](./api-1462730-pmprintsettingscopykeys.md)
  Obtains the keys for items in a print settings object.
- [PMGetPrintSettingsExtendedData](./core_printing/api-1805488-pmgetprintsettingsextendeddata.md)
  Obtains extended print settings data previously stored by your application.
- [PMSetPrintSettingsExtendedData](./core_printing/api-1805491-pmsetprintsettingsextendeddata.md)
  Stores your application-specific data in a print settings object.
- [PMGetJobNameCFString](./core_printing/api-1805513-pmgetjobnamecfstring.md)
  Obtains the name of the print job.
- [PMSetJobNameCFString](./core_printing/api-1805515-pmsetjobnamecfstring.md)
  Specifies the name of a print job.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applicationservices/1460602-pmprintsettingsgetvalue)*