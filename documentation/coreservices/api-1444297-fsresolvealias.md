# FSResolveAlias

**Framework**: Core Services  
**Kind**: func  
**Role**: Function

Returns an `FSRef` to the single most likely target of an alias record.

**Availability**:
- macOS 10.0+ - Deprecated in 10.8

> **Deprecated**: Use [`CFURLCreateByResolvingBookmarkData(_:_:_:_:_:_:_:)`](../CoreFoundation/cfurlcreatebyresolvingbookmarkdata%28_,_,_,_,_,_,_%29.md) instead.

## Declaration

```c
OSErr FSResolveAlias(const FSRef *fromFile, AliasHandle alias, FSRef *target, Boolean *wasChanged);
```

#### Return Value

A result code. When it finds the specified volume and parent directory but fails to find the target file or directory in that location, `FSResolveAlias` returns `fnfErr`. Note that the `FSRef` in the `alias` parameter is not valid in this case.

#### Discussion

The `FSResolveAlias` function performs a fast search for the target of the alias. If the resolution is successful, `FSResolveAlias` returns (in the `target` parameter) the `FSRef` for the target file system object, updates the alias record if necessary, and reports (through the `wasChanged` parameter) whether the record was updated. If the target is on an unmounted AppleShare volume, `FSResolveAlias` automatically mounts the volume. If the target is on an unmounted ejectable volume, `FSResolveAlias` asks the user to insert the volume. The `FSResolveAlias` function exits after it finds one acceptable target.

After it identifies a target, `FSResolveAlias` compares some key information about the target with the information in the alias record. If the information differs, `FSResolveAlias` updates the record to match the target.

The `FSResolveAlias` function displays the standard dialogs when it needs input from the user, such as a name and password for mounting a remote volume. The user can cancel the resolution through these dialogs. 

## Parameters

- `fromFile`: A pointer to the starting point for a relative search. If you pass `NULL` in this parameter, `FSResolveAlias` performs only an absolute search. If you pass a pointer to a valid `FSRef` in the `fromFile` parameter, `FSResolveAlias` performs a relative search for the target, followed by an absolute search only if the relative search fails. If you want to perform an absolute search followed by a relative search, you should use the function [`FSMatchAliasBulk`](./api-1444389-fsmatchaliasbulk.md).
- `alias`: A handle to the alias record to be resolved and, if necessary, updated.
- `target`: A pointer to an `FSRef`. On successful return, this `FSRef` describes the target of the alias record. This parameter must point to a valid `FSRef` structure.
- `wasChanged`: A pointer to a Boolean value indicating, on return, whether the alias record in the `alias` parameter was updated because it contained some outdated information about the target. If it updates the alias record, `FSResolveAlias` sets the `wasChanged` parameter to `true`. Otherwise, it sets it to `false`. (`FSResolveAlias` never updates a minimal alias, so it never sets `wasChanged` to `true` when resolving a minimal alias.

## See Also

### Resolving and Reading Alias Records
- [FSCopyAliasInfo](./api-1444271-fscopyaliasinfo.md)
  Returns information from an alias handle.
- [FSMatchAliasBulk](./api-1444389-fsmatchaliasbulk.md)
  Identifies a list of possible matches for an alias.
- [FSResolveAliasWithMountFlags](./api-1444279-fsresolvealiaswithmountflags.md)
  Returns an `FSRef` to the target of an alias.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1444297-fsresolvealias)*