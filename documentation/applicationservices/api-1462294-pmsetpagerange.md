# PMSetPageRange(_:_:_:)

**Framework**: Application Services  
**Kind**: func

Sets the valid range of pages that can be printed.

**Availability**:
- macOS 10.0+

## Declaration

```swift
func PMSetPageRange(_ printSettings: PMPrintSettings, _ minPage: UInt32, _ maxPage: UInt32) -> OSStatus
```

#### Return_value

A result code. See [`Result Codes`](core_printing#1670007.md).

#### Discussion

The function `PMSetPageRange` allows applications to set the minimum and maximum page numbers that can be printed for a document. If the user enters a value outside of this range in the Print dialog, the value is set to the closest allowed value. You can use the [`PMGetFirstPage(_:_:)`](1460271-pmgetfirstpage.md) and [`PMGetLastPage(_:_:)`](1462747-pmgetlastpage.md) functions to obtain the values entered by the user in the Print dialog.)

If you call the function `PMSetPageRange` to set the maximum page to a value other than the constant `kPMPrintAllPages`, the function `PMSetPageRange` causes the page range in the Print dialog to be properly restricted to the specified range. If you call the function `PMSetPageRange` without also calling the functions `PMSetFirstPage` or `PMSetLastPage`, then the Print dialog shows the specified page range in the From and To fields but with the All button selected. If you call the function `PMSetPageRange` and then call `PMSetFirstPage` or `PMSetLastPage` using the same page range you specified for `PMSetPageRange`, then the Print dialog shows the From button selected.

In all cases, if your application sets a range with `PMSetPageRange` and subsequently calls [`PMSetFirstPage(_:_:_:)`](1461519-pmsetfirstpage.md) or [`PMSetLastPage(_:_:_:)`](1463595-pmsetlastpage.md) with values outside of the specified range, Core Printing returns a result code of `kPMValueOutOfRange`. Conversely, if your application calls `PMSetPageRange` after calling `PMSetFirstPage` or `PMSetLastPage` (or after displaying the Print dialog), the page range specified by `PMSetPageRange` takes precedence, and the first and last page values are adjusted accordingly.

If you call this function after initiating a print job, the change is ignored for the current job.

## Parameters

- `printSettings`: The print settings object whose page range you want to set.
- `minPage`: The minimum page number allowed. This value appears as the default in the From field of the Print dialog. 
- `maxPage`: The maximum page number allowed. This value appears as the default in the To field of the Print dialog. Pass the constant   to allow the user to print the entire document. If the first page is set to 1, then passing   as the maximum page number causes the All button to be selected.

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

*[View on Apple Developer](https://developer.apple.com/documentation/applicationservices/1462294-pmsetpagerange)*