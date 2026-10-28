# FSNewAliasMinimal

**Framework**: Core Services  
**Kind**: func  
**Role**: Function

Creates a new minimal alias record, given a target file or directory.

**Availability**:
- macOS 10.0+ - Deprecated in 10.8

> **Deprecated**: Use [`CFURLCreateBookmarkData(_:_:_:_:_:_:)`](../CoreFoundation/cfurlcreatebookmarkdata%28_,_,_,_,_,_%29.md) instead.

## Declaration

```c
OSErr FSNewAliasMinimal(const FSRef *target, AliasHandle *inAlias);
```

## Return Value

A result code. If the specified target is valid, this function creates an alias record for the target and returns `noErr`. Any other return value indicates that this function did not create an alias record.

## Discussion

The `FSNewAliasMinimal` function creates an alias record that contains only the minimum information necessary to describe the target. The `FSNewAliasMinimal` function uses the standard alias record data structure, but it fills in only parts of the record.

The [`FSResolveAlias`](./api-1444297-fsresolvealias.md) function never updates a minimal alias record.

## Parameters

- `target`: A pointer to the target of the alias record.
- `inAlias`: A pointer to an alias handle. On return, this handle refers to the newly created alias record. If the function fails to create an alias record, it sets `inAlias` to `NULL`.

## See Also

### Creating and Updating Alias Records
- [FSNewAlias](./api-1444363-fsnewalias.md)
  Creates a new alias record, given a target file or directory.
- [FSNewAliasUnicode](./api-1444376-fsnewaliasunicode.md)
  Creates a new alias record, given the Unicode name and parent directory of the target.
- [FSNewAliasFromPath](./api-1444431-fsnewaliasfrompath.md)
  Creates a new alias record, given the pathname of the target file or directory.
- [FSNewAliasMinimalUnicode](./api-1444409-fsnewaliasminimalunicode.md)
  Creates a minimal alias, given the Unicode name and parent directory of the target.
- [FSUpdateAlias](./api-1444399-fsupdatealias.md)
  Updates an alias record for a specified target.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1444337-fsnewaliasminimal)*