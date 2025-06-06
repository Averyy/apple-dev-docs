# PMPrintSettingsCopyKeys(_:_:)

**Framework**: Application Services  
**Kind**: func

Obtains the keys for items in a print settings object.

**Availability**:
- macOS 10.5+

## Declaration

```swift
func PMPrintSettingsCopyKeys(_ printSettings: PMPrintSettings, _ settingsKeys: UnsafeMutablePointer<Unmanaged<CFArray>?>) -> OSStatus
```

#### Return_value

A result code. See [`Result Codes`](core_printing#1670007.md).

#### Discussion

This function provides an array of the keys in a print settings object. You could get the values for the keys in the array with [`PMPrintSettingsGetValue(_:_:_:)`](1460602-pmprintsettingsgetvalue.md), or use the keys to look up the values in the dictionary returned by [`PMPrintSettingsCopyAsDictionary(_:_:)`](1459088-pmprintsettingscopyasdictionary.md).

## Parameters

- `printSettings`: The print settings object with the desired keys.
- `settingsKeys`: A pointer to your   variable. On return, the variable refers to a Core Foundation array that contains the keys for items in the specified print settings object. Each of these keys may be passed to the function   to obtain a value. You are responsible for releasing the array. If an error occurs, the variable is set to  .

## See Also

- [func PMGetFirstPage(PMPrintSettings, UnsafeMutablePointer<UInt32>) -> OSStatus](1460271-pmgetfirstpage.md)
  Obtains the number of the first page to be printed.
- [func PMSetFirstPage(PMPrintSettings, UInt32, Bool) -> OSStatus](1461519-pmsetfirstpage.md)
  Sets the default page number of the first page to be printed.
- [func PMGetLastPage(PMPrintSettings, UnsafeMutablePointer<UInt32>) -> OSStatus](1462747-pmgetlastpage.md)
  Obtains the number of the last page to be printed.
- [func PMSetLastPage(PMPrintSettings, UInt32, Bool) -> OSStatus](1463595-pmsetlastpage.md)
  Sets the page number of the last page to be printed.
- [func PMGetPageRange(PMPrintSettings, UnsafeMutablePointer<UInt32>, UnsafeMutablePointer<UInt32>) -> OSStatus](1459324-pmgetpagerange.md)
  Obtains the valid range of pages that can be printed.
- [func PMSetPageRange(PMPrintSettings, UInt32, UInt32) -> OSStatus](1462294-pmsetpagerange.md)
  Sets the valid range of pages that can be printed.
- [func PMPrintSettingsGetJobName(PMPrintSettings, UnsafeMutablePointer<Unmanaged<CFString>?>) -> OSStatus](1459233-pmprintsettingsgetjobname.md)
  Obtains the name of a print job.
- [func PMPrintSettingsSetJobName(PMPrintSettings, CFString) -> OSStatus](1460149-pmprintsettingssetjobname.md)
  Specifies the name of a print job.
- [func PMGetCopies(PMPrintSettings, UnsafeMutablePointer<UInt32>) -> OSStatus](1464480-pmgetcopies.md)
  Obtains the number of copies that the user requests to be printed.
- [func PMSetCopies(PMPrintSettings, UInt32, Bool) -> OSStatus](1463804-pmsetcopies.md)
  Sets the initial value for the number of copies to be printed.
- [func PMGetCollate(PMPrintSettings, UnsafeMutablePointer<DarwinBoolean>) -> OSStatus](1464492-pmgetcollate.md)
  Obtains a Boolean value that indicates whether the job collate option is selected.
- [func PMSetCollate(PMPrintSettings, Bool) -> OSStatus](1463223-pmsetcollate.md)
  Specifies whether the job collate option is selected.
- [func PMGetDuplex(PMPrintSettings, UnsafeMutablePointer<PMDuplexMode>) -> OSStatus](1458921-pmgetduplex.md)
  Obtains the selected duplex mode.
- [func PMSetDuplex(PMPrintSettings, PMDuplexMode) -> OSStatus](1462000-pmsetduplex.md)
  Sets the duplex mode.
- [func PMPrintSettingsGetValue(PMPrintSettings, CFString, UnsafeMutablePointer<Unmanaged<CFTypeRef>?>) -> OSStatus](1460602-pmprintsettingsgetvalue.md)
  Obtains the value of a setting in a print settings object.
- [func PMPrintSettingsSetValue(PMPrintSettings, CFString, CFTypeRef?, Bool) -> OSStatus](1461697-pmprintsettingssetvalue.md)
  Stores the value of a setting in a print settings object.
- [func PMPrintSettingsCopyAsDictionary(PMPrintSettings, UnsafeMutablePointer<Unmanaged<CFDictionary>?>) -> OSStatus](1459088-pmprintsettingscopyasdictionary.md)
  Creates a dictionary that contains the settings in a print settings object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applicationservices/1462730-pmprintsettingscopykeys)*