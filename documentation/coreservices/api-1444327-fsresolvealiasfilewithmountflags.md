# FSResolveAliasFileWithMountFlags

**Framework**: Core Services  
**Kind**: func  
**Role**: Function

Resolves an alias contained in an alias file.

**Availability**:
- macOS 10.0+ - Deprecated in 10.8

> **Deprecated**: First use [`CFURLCreateBookmarkDataFromFile(_:_:_:)`](../CoreFoundation/cfurlcreatebookmarkdatafromfile%28_,_,_%29.md), then use [`CFURLCreateByResolvingBookmarkData(_:_:_:_:_:_:_:)`](../CoreFoundation/cfurlcreatebyresolvingbookmarkdata%28_,_,_,_,_,_,_%29.md).

## Declaration

```c
OSErr FSResolveAliasFileWithMountFlags(FSRef *theRef, Boolean resolveAliasChains, Boolean *targetIsFolder, Boolean *wasAliased, unsigned long mountFlags);
```

## Return Value

A result code.

## Discussion

The function `FSResolveAliasFileWithMountFlags` is identical to [`FSResolveAliasFile`](./api-1444372-fsresolvealiasfile.md) with the exception that it provides the `mountFlags` parameter, allowing callers additional control over how the alias file is resolved.

## Parameters

- `theRef`: A pointer to the alias file you plan to open. If the function completes successfully, this `FSRef` describes the file or the directory referred to by the alias file.
- `resolveAliasChains`: A Boolean value. Set this parameter to `TRUE` if you want `FSResolveAliasFileWithMountFlags` to resolve all aliases in a chain (for example, an alias file that refers to an alias file and so on), stopping only when it reaches the target file. Set this parameter to `FALSE` if you want to resolve only one alias file, even if the target is another alias file. 
- `targetIsFolder`: A pointer to a Boolean value. The `FSResolveAliasFileWithMountFlags` function returns `TRUE` in this parameter if the `FSRef` in the parameter `theRef` points to a directory or a volume; otherwise, `FSResolveAliasFileWithMountFlags` returns `FALSE` in this parameter. 
- `wasAliased`: A pointer to a Boolean value. The `FSResolveAliasFileWithMountFlags` function returns `TRUE` in this parameter if the `FSRef` in the parameter `theRef` points to an alias; otherwise, `FSResolveAliasFileWithMountFlags` returns `FALSE` in this parameter. 
- `mountFlags`: Options controlling how the alias file is resolved. See [Volume Mount Options](./api-1444436-volume_mount_options.md) for a description of the values you can use here. Set this parameter to `kResolveAliasFileNoUI` to prevent any user interaction, including disk switch alerts, while the alias is being resolved.

## See Also

### Working With Finder Alias Files
- [FSFollowFinderAlias](./api-1444287-fsfollowfinderalias.md)
  Resolves an alias record obtained from a Finder alias file.
- [FSIsAliasFile](./api-1444426-fsisaliasfile.md)
  Determines whether a file system object is an alias file, a data file, or a folder.
- [FSResolveAliasFile](./api-1444372-fsresolvealiasfile.md)
  Resolves an alias contained in an alias file.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1444327-fsresolvealiasfilewithmountflags)*