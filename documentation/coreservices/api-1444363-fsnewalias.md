# FSNewAlias

**Framework**: Core Services  
**Kind**: func  
**Role**: Function

Creates a new alias record, given a target file or directory.

**Availability**:
- macOS 10.0+ - Deprecated in 10.8

> **Deprecated**: Use [`CFURLCreateBookmarkData(_:_:_:_:_:_:)`](../CoreFoundation/cfurlcreatebookmarkdata%28_,_,_,_,_,_%29.md) instead.

## Declaration

```c
OSErr FSNewAlias(const FSRef *fromFile, const FSRef *target, AliasHandle *inAlias);
```

#### Return Value

A result code. If the specified target is valid, this function creates an alias record for the target and returns `noErr`. Any other return value indicates that this function did not create an alias record.

#### Discussion

The `FSNewAlias` function creates an alias record that describes the specified target. It allocates the storage, fills in the record, and puts a record handle to that storage in the `inAlias` parameter. `FSNewAlias` records the full pathname of the target and a collection of other information relevant to locating the target, verifying the target, and mounting the target’s volume, if necessary. You can have `FSNewAlias` store relative search information as well by supplying a starting point for a relative search.

## Parameters

- `fromFile`: A pointer to the starting point for a relative search. You may pass `NULL` if you do not need relative search information in the alias record. The files or directories specified in the `fromFile` and `target` parameters must reside on the same volume.
- `target`: A pointer to the target file or directory of the alias.
- `inAlias`: A pointer to an alias handle. On return, this handle refers to the newly created alias record. If the function fails to create an alias record, it sets `inAlias` to `NULL`.

## See Also

### Creating and Updating Alias Records
- [FSNewAliasUnicode](./api-1444376-fsnewaliasunicode.md)
  Creates a new alias record, given the Unicode name and parent directory of the target.
- [FSNewAliasFromPath](./api-1444431-fsnewaliasfrompath.md)
  Creates a new alias record, given the pathname of the target file or directory.
- [FSNewAliasMinimal](./api-1444337-fsnewaliasminimal.md)
  Creates a new minimal alias record, given a target file or directory.
- [FSNewAliasMinimalUnicode](./api-1444409-fsnewaliasminimalunicode.md)
  Creates a minimal alias, given the Unicode name and parent directory of the target.
- [FSUpdateAlias](./api-1444399-fsupdatealias.md)
  Updates an alias record for a specified target.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1444363-fsnewalias)*