# FSIsAliasFile

**Framework**: Core Services  
**Kind**: func  
**Role**: Function

Determines whether a file system object is an alias file, a data file, or a folder.

**Availability**:
- macOS 10.0+ - Deprecated in 10.8

> **Deprecated**: Use [`CFURLCopyResourcePropertyForKey(_:_:_:_:)`](../CoreFoundation/cfurlcopyresourcepropertyforkey%28_,_,_,_%29.md) with [`kCFURLIsAliasFileKey`](../CoreFoundation/kcfurlisaliasfilekey.md) instead.

## Declaration

```c
OSErr FSIsAliasFile(const FSRef *fileRef, Boolean *aliasFileFlag, Boolean *folderFlag);
```

## Return Value

A result code.

## Discussion

[Table 1](./api-1444426-fsisaliasfile.md#1966543) summarizes the information that this function provides about the object specified in the `fileRef` parameter: 

| Alias flag | Folder flag | Object kind |
| --- | --- | --- |
| T | F | Alias file |
| F | F | Data file |
| F | T | Folder |

Note that if `fileRef` is an alias file, this function does not provide any information about the object to which the alias refers. To find out whether this object is a file or a folder, you can use [`FSResolveAliasFile`](./api-1444372-fsresolvealiasfile.md).

## Parameters

- `fileRef`: A pointer to the file system object to test.
- `aliasFileFlag`: A pointer to a Boolean variable. On return, a value of `TRUE` indicates that the object specified in the `fileRef` parameter is an alias file. A value of `FALSE` indicates that the object is not an alias file. 
- `folderFlag`: A pointer to a Boolean variable. On return, a value of `TRUE` indicates that the object specified in the `fileRef` parameter is a folder. A value of `FALSE` indicates that the object is a file. 

## See Also

### Working With Finder Alias Files
- [FSFollowFinderAlias](./api-1444287-fsfollowfinderalias.md)
  Resolves an alias record obtained from a Finder alias file.
- [FSResolveAliasFile](./api-1444372-fsresolvealiasfile.md)
  Resolves an alias contained in an alias file.
- [FSResolveAliasFileWithMountFlags](./api-1444327-fsresolvealiasfilewithmountflags.md)
  Resolves an alias contained in an alias file.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1444426-fsisaliasfile)*