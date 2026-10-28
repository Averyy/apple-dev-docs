# FSUpdateAlias

**Framework**: Core Services  
**Kind**: func  
**Role**: Function

Updates an alias record for a specified target.

**Availability**:
- macOS 10.0+ - Deprecated in 10.8

> **Deprecated**: First use [`CFURLCreateBookmarkData(_:_:_:_:_:_:)`](../CoreFoundation/cfurlcreatebookmarkdata%28_,_,_,_,_,_%29.md), then use [`CFURLWriteBookmarkDataToFile(_:_:_:_:)`](../CoreFoundation/cfurlwritebookmarkdatatofile%28_,_,_,_%29.md).

## Declaration

```c
OSErr FSUpdateAlias(const FSRef *fromFile, const FSRef *target, AliasHandle alias, Boolean *wasChanged);
```

## Return Value

A result code.

## Discussion

This function rebuilds the entire alias record and fills it in as the `FSNewAlias` function would. The `FSUpdateAlias` function always creates a complete alias record. When you use `FSUpdateAlias` to update a minimal alias record, you convert the minimal record to a complete record.

## Parameters

- `fromFile`: A pointer to the starting point for a relative search. You may pass `NULL` if you do not need relative search information in the alias record. The two files or directories specified in the `fromFile` and `target` parameters must reside on the same volume.
- `target`: A pointer to the target of the alias record.
- `alias`: A handle to the alias record to be updated.
- `wasChanged`: A pointer to a Boolean value that, on output, indicates whether the newly constructed alias record is different from the old one. If the new record is exactly the same as the old one, the value is `false`. Otherwise, the value is `true`. Check this parameter to determine whether you need to save an updated record.

## See Also

### Creating and Updating Alias Records
- [FSNewAlias](./api-1444363-fsnewalias.md)
  Creates a new alias record, given a target file or directory.
- [FSNewAliasUnicode](./api-1444376-fsnewaliasunicode.md)
  Creates a new alias record, given the Unicode name and parent directory of the target.
- [FSNewAliasFromPath](./api-1444431-fsnewaliasfrompath.md)
  Creates a new alias record, given the pathname of the target file or directory.
- [FSNewAliasMinimal](./api-1444337-fsnewaliasminimal.md)
  Creates a new minimal alias record, given a target file or directory.
- [FSNewAliasMinimalUnicode](./api-1444409-fsnewaliasminimalunicode.md)
  Creates a minimal alias, given the Unicode name and parent directory of the target.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1444399-fsupdatealias)*