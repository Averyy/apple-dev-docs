# FSCopyAliasInfo

**Framework**: Core Services  
**Kind**: func  
**Role**: Function

Returns information from an alias handle.

**Availability**:
- macOS 10.2+ - Deprecated in 10.8

> **Deprecated**: Use [`CFURLCreateResourcePropertiesForKeysFromBookmarkData(_:_:_:)`](../CoreFoundation/cfurlcreateresourcepropertiesforkeysfrombookmarkdata%28_,_,_%29.md) or [`CFURLCreateResourcePropertyForKeyFromBookmarkData(_:_:_:)`](../CoreFoundation/cfurlcreateresourcepropertyforkeyfrombookmarkdata%28_,_,_%29.md).

## Declaration

```c
OSStatus FSCopyAliasInfo(AliasHandle inAlias, HFSUniStr255 *targetName, HFSUniStr255 *volumeName, CFStringRef *pathString, FSAliasInfoBitmap *whichInfo, FSAliasInfo *info);
```

#### Return Value

A result code.

#### Discussion

This function returns the requested information from the alias handle passed in the `inAlias` parameter. The information is gathered only from the alias record, so it may not match what is on disk. No disk input/output is performed.

The `FSCopyAliasInfo` function adds support for unicode filenames and filenames longer than 32 bytes. It replaces the `GetAliasInfo` function.

## Parameters

- `inAlias`: A handle to the alias record from which to get information.
- `targetName`: A pointer to a string that, on return, contains the name of the target item. Pass `NULL` if you do not want this information returned.
- `volumeName`: A pointer to a string that, on return, contains the name of the volume the target resides on. Pass `NULL` if you do not want this information returned.
- `pathString`: A pointer a CFString that, on return, contains the POSIX path to the target. Pass `NULL` if you do not want this information returned.
- `whichInfo`: A pointer to a variable of type `FSAliasInfoBitmap`. On return, this field indicates which fields in the alias information block, specified in the `info` parameter, contain valid data. See [`FSAliasInfoBitmap`](./fsaliasinfobitmap.md) for a description of the values that may be returned here. This parameter may be `NULL`.
- `info`: A pointer to a structure of type [`FSAliasInfo`](./fsaliasinfo.md). On return, this structure contains information about the alias. Pass `NULL` if you do not want this information returned.

## See Also

### Resolving and Reading Alias Records
- [FSMatchAliasBulk](./api-1444389-fsmatchaliasbulk.md)
  Identifies a list of possible matches for an alias.
- [FSResolveAlias](./api-1444297-fsresolvealias.md)
  Returns an `FSRef` to the single most likely target of an alias record.
- [FSResolveAliasWithMountFlags](./api-1444279-fsresolvealiaswithmountflags.md)
  Returns an `FSRef` to the target of an alias.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1444271-fscopyaliasinfo)*