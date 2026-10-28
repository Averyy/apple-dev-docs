# FSResolveAliasFile

**Framework**: Core Services  
**Kind**: func  
**Role**: Function

Resolves an alias contained in an alias file.

**Availability**:
- macOS 10.0+ - Deprecated in 10.8

> **Deprecated**: First use [`CFURLCreateBookmarkDataFromFile(_:_:_:)`](../CoreFoundation/cfurlcreatebookmarkdatafromfile%28_,_,_%29.md), then use [`CFURLCreateByResolvingBookmarkData(_:_:_:_:_:_:_:)`](../CoreFoundation/cfurlcreatebyresolvingbookmarkdata%28_,_,_,_,_,_,_%29.md).

## Declaration

```c
OSErr FSResolveAliasFile(FSRef *theRef, Boolean resolveAliasChains, Boolean *targetIsFolder, Boolean *wasAliased);
```

## Return Value

A result code. When it finds the specified volume and parent directory but fails to find the target file or directory in that location, `FSResolveAliasFile` returns `fnfErr`.

## Discussion

If your application bypasses the Finder when manipulating documents, it should check for and resolve aliases itself by using the `FSResolveAliasFile` function.

The `FSResolveAliasFile` function first checks the catalog file for the file or directory specified in the parameter `theRef` to determine whether it is an alias and whether it is a file or a directory. If the object is not an alias, `FSResolveAliasFile` leaves `theRef` unchanged, sets the `targetIsFolder` parameter to `TRUE` for a directory or volume and `FALSE` for a file, sets `wasAliased` to `FALSE`, and returns `noErr`. If the object is an alias, `FSResolveAliasFile` resolves it, places the target in the parameter `theRef`, and sets the `wasAliased` flag to `TRUE`.

If `FSResolveAliasFile` receives an error code while resolving an alias, it leaves the input parameters as they are and exits, returning an error code. `FSResolveAliasFile` can return any Resource Manager or File Manager errors.

## Parameters

- `theRef`: A pointer to the alias file you plan to open. If the function completes successfully, this `FSRef` describes to the file or the directory referred to by the alias file.
- `resolveAliasChains`: A Boolean value. Set this parameter to `TRUE` if you want `FSResolveAliasFile` to resolve all aliases in a chain (for example, an alias file that refers to an alias file and so on), stopping only when it reaches the target file. Set this parameter to `FALSE` if you want to resolve only one alias file, even if the target is another alias file. 
- `targetIsFolder`: A pointer to a Boolean value. The `FSResolveAliasFile` function returns `TRUE` in this parameter if the `FSRef` in the parameter `theRef` points to a directory or a volume; otherwise, `FSResolveAliasFile` returns `FALSE` in this parameter. 
- `wasAliased`: A pointer to a Boolean value. The `FSResolveAliasFile` function returns `TRUE` in this parameter if the `FSRef` in the parameter `theRef` points to an alias; otherwise, `FSResolveAliasFile` returns `FALSE` in this parameter. 

## See Also

### Working With Finder Alias Files
- [FSFollowFinderAlias](./api-1444287-fsfollowfinderalias.md)
  Resolves an alias record obtained from a Finder alias file.
- [FSIsAliasFile](./api-1444426-fsisaliasfile.md)
  Determines whether a file system object is an alias file, a data file, or a folder.
- [FSResolveAliasFileWithMountFlags](./api-1444327-fsresolvealiasfilewithmountflags.md)
  Resolves an alias contained in an alias file.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1444372-fsresolvealiasfile)*