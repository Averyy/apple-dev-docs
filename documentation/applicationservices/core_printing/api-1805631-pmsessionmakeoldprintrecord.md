# PMSessionMakeOldPrintRecord

**Framework**: Application Services  
**Kind**: func

Creates an old-style print record from page format and print settings objects.

> **Deprecated**: There is no replacement; old-style print records are obsolete and serve no useful purpose in macOS.

## Declaration

```c
OSStatus PMSessionMakeOldPrintRecord (
   PMPrintSession printSession,
   PMPrintSettings printSettings,
   PMPageFormat pageFormat,
   Handle *printRecordHandle
);
```

#### Return Value

A result code. See [Result Codes](../core_printing.md#1670007).

#### Overview

You must call this function between the creation and release of a printing session. See the function [`PMCreateSession`](../api-1463247-pmcreatesession.md).

You can use `PMSessionMakeOldPrintRecord` to create an old-style print record to store with your documents for compatibility with pre-Carbon versions of your application. Note that because the page format and print settings objects contain more information than the old print record, some settings may be lost in the conversion. That is, perfect translation between the old and new style objects is not achievable.

In macOS, the function always creates a LaserWriter 8 compatible print record.

##### Special Considerations

The proper way to keep page format information for use in macOS is with a flattened `PMPageFormat` object. Typically applications don't keep print settings with a document but if that is appropriate for a given application, the proper way to do so is to use a flattened `PMPrintSettings` object.

## Parameters

- `printSession`: The current printing session.
- `printSettings`: A print settings object. To create a print settings object you can call the function [`PMCreatePrintSettings`](../api-1463239-pmcreateprintsettings.md) and then call the function [`PMSessionDefaultPrintSettings`](../api-1460138-pmsessiondefaultprintsettings.md) to initialize the print settings object to default values. 
- `pageFormat`: A page format object. To create a page format object you can call the function [`PMCreatePageFormat`](../api-1459485-pmcreatepageformat.md) and then call the function [`PMSessionDefaultPageFormat`](../api-1462217-pmsessiondefaultpageformat.md) to initialize the page format object to default values. 
- `printRecordHandle`: On return, a handle to an old-style print record. You are responsible for disposing of the handle.

## See Also

### Converting and Saving Old Print Records
- [PMSessionConvertOldPrintRecord](./api-1805626-pmsessionconvertoldprintrecord.md)
  Creates new page format and print settings objects from an old-style print record created for the classic Printing Manager.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applicationservices/core_printing/1805631-pmsessionmakeoldprintrecord)*