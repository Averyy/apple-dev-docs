# PMSetLastPage(_:_:_:)

**Framework**: Application Services  
**Kind**: func

Sets the page number of the last page to be printed.

**Availability**:
- macOS 10.0+

## Declaration

```swift
func PMSetLastPage(_ printSettings: PMPrintSettings, _ last: UInt32, _ lock: Bool) -> OSStatus
```

#### Return_value

A result code. See [`Result Codes`](core_printing#1670007.md). 

#### Discussion

Typically, you call this function after the Print dialog is displayed to indicate the number of the last page number to be printed. In macOS, setting the last page provides information used by the progress dialog that is shown during printing.

If you call the function [`PMSetPageRange(_:_:_:)`](1462294-pmsetpagerange.md) and then call `PMSetFirstPage` or `PMSetLastPage` using the same page range you specified for `PMSetPageRange`, then the Print dialog shows the From button selected. If you use the constant `kPMPrintAllPages` to set the page range with the function `PMSetPageRange`, then the Print dialog opens with the All button selected regardless of whether you also call `PMSetFirstPage` or `PMSetLastPage`. 

If you call this function after initiating a print job, the change is ignored for the current job.

## Parameters

- `printSettings`: The print settings object whose last page number you want to set.
- `last`: The page number of the last page to print. This value appears in the To field of the Print dialog. Pass the constant   to print the entire document. 
- `lock`: The lock state of the setting. Locking is not supported at this time. 

## See Also

- [func PMGetFirstPage(PMPrintSettings, UnsafeMutablePointer<UInt32>) -> OSStatus](1460271-pmgetfirstpage.md)
  Obtains the number of the first page to be printed.
- [func PMSetFirstPage(PMPrintSettings, UInt32, Bool) -> OSStatus](1461519-pmsetfirstpage.md)
  Sets the default page number of the first page to be printed.
- [func PMGetLastPage(PMPrintSettings, UnsafeMutablePointer<UInt32>) -> OSStatus](1462747-pmgetlastpage.md)
  Obtains the number of the last page to be printed.
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
- [func PMPrintSettingsCopyKeys(PMPrintSettings, UnsafeMutablePointer<Unmanaged<CFArray>?>) -> OSStatus](1462730-pmprintsettingscopykeys.md)
  Obtains the keys for items in a print settings object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applicationservices/1463595-pmsetlastpage)*