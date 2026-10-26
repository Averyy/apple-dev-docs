# PMSessionConvertOldPrintRecord

**Framework**: Application Services  
**Kind**: func

Creates new page format and print settings objects from an old-style print record created for the classic Printing Manager.

> **Deprecated**: There is no replacement; during the transition from Mac OS 9 to macOS, this function facilitated the migration of print records saved in documents created in Mac OS 9, but the function no longer serves any useful purpose in macOS.

## Declaration

```c
OSStatus PMSessionConvertOldPrintRecord (
   PMPrintSession printSession,
   Handle printRecordHandle,
   PMPrintSettings *printSettings,
   PMPageFormat *pageFormat
);
```

#### Return Value

A result code. See [Result Codes](../core_printing.md#1670007).

#### Overview

You must call this function between the creation and release of a printing session. See the function [`PMCreateSession`](../api-1463247-pmcreatesession.md).

You can use `PMSessionConvertOldPrintRecord` to create page format and print settings objects from old-style print records stored in documents created by pre-Carbon versions of your application. You should validate the page format and print settings objects returned to you by calling the functions `PMSessionValidatePageFormat` and `PMSessionValidatePrintSettings`. Note that perfect translation between the old and new style objects is not achievable. 

In macOS, the function assumes the print record to be converted is a LaserWriter 8 print record.

##### Special Considerations

If you need to convert a Mac OS 9 print record into data you can use in macOS, you should extract the page size data from the print record and use the function [`PMCreatePageFormatWithPMPaper`](../api-1459274-pmcreatepageformatwithpmpaper.md) to create a `PMPageFormat` object that corresponds to that data.

## Parameters

- `printSession`: The current printing session.
- `printRecordHandle`: A handle to an old-style print record created by the classic Printing Manager. You are responsible for disposing of the handle.
- `printSettings`: On return, a print settings object that contains values converted from the print record. You are responsible for releasing the print settings object with the function [`PMRelease`](../api-1461402-pmrelease.md).
- `pageFormat`: On return, a page format object that contains values converted from the print record. You are responsible for releasing the page format object with the function [`PMRelease`](../api-1461402-pmrelease.md).

## See Also

### Converting and Saving Old Print Records
- [PMSessionMakeOldPrintRecord](./api-1805631-pmsessionmakeoldprintrecord.md)
  Creates an old-style print record from page format and print settings objects.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applicationservices/core_printing/1805626-pmsessionconvertoldprintrecord)*