# FSResolveAliasWithMountFlags

**Framework**: Core Services  
**Kind**: func  
**Role**: Function

Returns an `FSRef` to the target of an alias.

**Availability**:
- macOS 10.0+ - Deprecated in 10.8

> **Deprecated**: Use [`CFURLCreateByResolvingBookmarkData(_:_:_:_:_:_:_:)`](../CoreFoundation/cfurlcreatebyresolvingbookmarkdata%28_,_,_,_,_,_,_%29.md) instead.

## Declaration

```c
OSErr FSResolveAliasWithMountFlags(const FSRef *fromFile, AliasHandle inAlias, FSRef *target, Boolean *wasChanged, unsigned long mountFlags);
```

#### Return Value

A result code.

#### Discussion

The function `FSResolveAliasWithMountFlags` is identical to [`FSResolveAlias`](./api-1444297-fsresolvealias.md) with the exception that it provides the `mountFlags` parameter, allowing callers additional control over how the alias is resolved.

## Parameters

- `fromFile`: A pointer to the starting point for a relative search. If you pass `NULL` in this parameter, `FSResolveAliasWithMountFlags` performs an absolute search. If you pass a pointer to a valid `FSRef` in the `fromFile` parameter, `FSResolveAliasWithMountFlags` performs a relative search for the target, followed by an absolute search only if the relative search fails. If you want to perform an absolute search followed by a relative search, you should use the function [`FSMatchAliasBulk`](./api-1444389-fsmatchaliasbulk.md).
- `inAlias`: A handle to the alias record to be resolved and, if necessary, updated.
- `target`: A pointer to an `FSRef` structure. On successful return, this `FSRef` refers to the target of the alias record. This parameter must point to a valid `FSRef` structure.
- `wasChanged`: A pointer to a Boolean value indicating, on return, whether the alias record to be resolved was updated because it contained some outdated information about the target. If it updates the alias record, `FSResolveAliasWithMountFlags` sets the `wasChanged` parameter to `true`. Otherwise, it sets it to `false`. (`FSResolveAliasWithMountFlags` never updates a minimal alias, so it never sets `wasChanged` to `true` when resolving a minimal alias.
- `mountFlags`: Options controlling how the alias is resolved. See [Volume Mount Options](./api-1444436-volume_mount_options.md) for a description of the values you can use here. Set this parameter to `kResolveAliasFileNoUI` to prevent any user interaction while the alias is being resolved.

## See Also

### Resolving and Reading Alias Records
- [FSCopyAliasInfo](./api-1444271-fscopyaliasinfo.md)
  Returns information from an alias handle.
- [FSMatchAliasBulk](./api-1444389-fsmatchaliasbulk.md)
  Identifies a list of possible matches for an alias.
- [FSResolveAlias](./api-1444297-fsresolvealias.md)
  Returns an `FSRef` to the single most likely target of an alias record.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1444279-fsresolvealiaswithmountflags)*