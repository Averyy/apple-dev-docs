# FSFollowFinderAlias

**Framework**: Core Services  
**Kind**: func  
**Role**: Function

Resolves an alias record obtained from a Finder alias file.

**Availability**:
- macOS 10.0+ - Deprecated in 10.8

> **Deprecated**: First use [`CFURLCreateBookmarkDataFromFile(_:_:_:)`](../CoreFoundation/cfurlcreatebookmarkdatafromfile%28_,_,_%29.md), then use [`CFURLCreateByResolvingBookmarkData(_:_:_:_:_:_:_:)`](../CoreFoundation/cfurlcreatebyresolvingbookmarkdata%28_,_,_,_,_,_,_%29.md).

## Declaration

```c
OSErr FSFollowFinderAlias(FSRef *fromFile, AliasHandle alias, Boolean logon, FSRef *target, Boolean *wasChanged);
```

#### Return Value

A result code.

## Parameters

- `fromFile`: A pointer to the file to use for a first attempt at a relative resolution; pass a pointer to the alias file's `FSRef` for this parameter.
- `alias`: A handle to the alias record taken from the alias file's resources.
- `logon`: If `true`, the Alias Manager attempts to mount a volume if necessary to complete the resolution of the alias.
- `target`: A pointer to an `FSRef` structure. On return, this `FSRef` refers to the target found by the resolution.
- `wasChanged`: A pointer to a Boolean value. `FSFollowFinderAlias` sets this value to `true` if it has updated the alias record.

## See Also

### Working With Finder Alias Files
- [FSIsAliasFile](./api-1444426-fsisaliasfile.md)
  Determines whether a file system object is an alias file, a data file, or a folder.
- [FSResolveAliasFile](./api-1444372-fsresolvealiasfile.md)
  Resolves an alias contained in an alias file.
- [FSResolveAliasFileWithMountFlags](./api-1444327-fsresolvealiasfilewithmountflags.md)
  Resolves an alias contained in an alias file.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1444287-fsfollowfinderalias)*