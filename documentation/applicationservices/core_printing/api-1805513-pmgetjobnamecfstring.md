# PMGetJobNameCFString

**Framework**: Application Services  
**Kind**: func

Obtains the name of the print job.

> **Deprecated**: Use [`PMPrintSettingsGetJobName`](../api-1459233-pmprintsettingsgetjobname.md) instead.

## Declaration

```c
OSStatus PMGetJobNameCFString (
   PMPrintSettings printSettings,
   CFStringRef *name
);
```

## Return Value

A result code. See [Result Codes](../core_printing.md#1670007).

## Parameters

- `printSettings`: The print settings object whose job name you want to obtain.
- `name`: A pointer to your [`CFStringRef`](../../CoreFoundation/cfstring.md) variable. On return, the variable refers to a string that contains the name of the print job. Despite what its name implies, the function `PMGetJobNameCFString` has Create/Copy semantics which means your application must release the string returned to it.

## See Also

### Accessing Data in Print Settings Objects
- [PMGetPrintSettingsExtendedData](./api-1805488-pmgetprintsettingsextendeddata.md)
  Obtains extended print settings data previously stored by your application.
- [PMSetPrintSettingsExtendedData](./api-1805491-pmsetprintsettingsextendeddata.md)
  Stores your application-specific data in a print settings object.
- [PMGetFirstPage](../api-1460271-pmgetfirstpage.md)
  Obtains the number of the first page to be printed.
- [PMSetFirstPage](../api-1461519-pmsetfirstpage.md)
  Sets the default page number of the first page to be printed.
- [PMGetLastPage](../api-1462747-pmgetlastpage.md)
  Obtains the number of the last page to be printed.
- [PMSetLastPage](../api-1463595-pmsetlastpage.md)
  Sets the page number of the last page to be printed.
- [PMGetPageRange](../api-1459324-pmgetpagerange.md)
  Obtains the valid range of pages that can be printed.
- [PMSetPageRange](../api-1462294-pmsetpagerange.md)
  Sets the valid range of pages that can be printed.
- [PMPrintSettingsGetJobName](../api-1459233-pmprintsettingsgetjobname.md)
  Obtains the name of a print job.
- [PMPrintSettingsSetJobName](../api-1460149-pmprintsettingssetjobname.md)
  Specifies the name of a print job.
- [PMGetCopies](../api-1464480-pmgetcopies.md)
  Obtains the number of copies that the user requests to be printed.
- [PMSetCopies](../api-1463804-pmsetcopies.md)
  Sets the initial value for the number of copies to be printed.
- [PMGetCollate](../api-1464492-pmgetcollate.md)
  Obtains a Boolean value that indicates whether the job collate option is selected.
- [PMSetCollate](../api-1463223-pmsetcollate.md)
  Specifies whether the job collate option is selected.
- [PMGetDuplex](../api-1458921-pmgetduplex.md)
  Obtains the selected duplex mode.
- [PMSetDuplex](../api-1462000-pmsetduplex.md)
  Sets the duplex mode.
- [PMPrintSettingsGetValue](../api-1460602-pmprintsettingsgetvalue.md)
  Obtains the value of a setting in a print settings object.
- [PMPrintSettingsSetValue](../api-1461697-pmprintsettingssetvalue.md)
  Stores the value of a setting in a print settings object.
- [PMPrintSettingsCopyAsDictionary](../api-1459088-pmprintsettingscopyasdictionary.md)
  Creates a dictionary that contains the settings in a print settings object.
- [PMPrintSettingsCopyKeys](../api-1462730-pmprintsettingscopykeys.md)
  Obtains the keys for items in a print settings object.
- [PMSetJobNameCFString](./api-1805515-pmsetjobnamecfstring.md)
  Specifies the name of a print job.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applicationservices/core_printing/1805513-pmgetjobnamecfstring)*