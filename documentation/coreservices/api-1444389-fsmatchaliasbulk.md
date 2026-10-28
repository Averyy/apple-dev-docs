# FSMatchAliasBulk

**Framework**: Core Services  
**Kind**: func  
**Role**: Function

Identifies a list of possible matches for an alias.

**Availability**:
- macOS 10.5+ - Deprecated in 10.8

> **Deprecated**: This API does not scale to volumes that contain large numbers of file system objects. To search for files that match specific properties, use Spotlight functionality instead (to learn more about Spotlight, see [Spotlight Overview](https://developer.apple.com/library/archive/documentation/Carbon/Conceptual/MetadataIntro/MetadataIntro.html#//apple_ref/doc/uid/TP40001268)).

## Declaration

```c
OSStatus FSMatchAliasBulk(const FSRef *fromFile, unsigned long rulesMask, AliasHandle inAlias, short *aliasCount, FSRef *aliasList, Boolean *needsUpdate, FSAliasFilterProcPtr aliasFilter, void *yourDataPtr);
```

## Return Value

A result code. If the Alias Manager finds the specified volume and parent directory but fails to find the target file or directory in that location, the return value is `fnfErr` and the elements in the `aliasList` parameter are not valid.

## Discussion

After it identifies a target, this function compares some key information about the target with the same information in the record. If the information does not match, this function sets the `needsUpdate` flag to `true`. This function also sets the `needsUpdate` flag to `true` if it identifies a list of possible matches rather than a single match or if `kARMsearchRelFirst` is set in the `rulesMask` parameter but the target is identified through either an absolute search or an exhaustive search. Otherwise, this function sets the `needsUpdate` flag to `false`. This function always sets the `needsUpdate` flag to `false` when resolving an alias created by `FSNewAliasMinimal`. To update the alias record to reflect the final results of the resolution, use the function [`FSUpdateAlias`](./api-1444399-fsupdatealias.md).

## Parameters

- `fromFile`: A pointer to the starting point for a relative search. You may pass `NULL` if you do not want this function to perform a relative search. By default, this function performs a relative search only if the absolute search does not find a match. If you want to perform the relative search first, you should pass `kARMSearchRelFirst` in the `rulesMask` parameter.
- `rulesMask`: A set of rules to guide the resolution. Pass the sum of all of the rules you want to invoke. For a description of the values you can use in this parameter, see [Matching Constants](./api-1444405-matching_constants.md).
- `inAlias`: A handle to the alias record to be resolved.
- `aliasCount`: On input, a pointer to the maximum number of possible matches to return. On output, the actual number of matches returned.
- `aliasList`: A pointer to an array of `FSRef` structures. On output, this array holds the results of the search, a list of possible candidates.
- `needsUpdate`: A pointer to a Boolean flag that, on output, indicates whether the alias record needs to be updated. For more information about this parameter, see the Discussion.
- `aliasFilter`: An optional application-defined filter function. The Alias Manager calls your filter function each time it identifies a possible match or after the search has continued for three seconds without a match. Your filter function returns a Boolean value that determines whether the possible match is discarded (`true`) or added to the list of possible targets (`false`). It can also terminate the search by setting the variable parameter `quitFlag`. See [`FSAliasFilterProcPtr`](./fsaliasfilterprocptr.md) for a description of the filter function.
- `yourDataPtr`: A pointer to data to be passed to the filter function, or `NULL`. The `yourDataPtr` parameter can point to any data your application might need in the filter function.

## See Also

### Resolving and Reading Alias Records
- [FSCopyAliasInfo](./api-1444271-fscopyaliasinfo.md)
  Returns information from an alias handle.
- [FSResolveAlias](./api-1444297-fsresolvealias.md)
  Returns an `FSRef` to the single most likely target of an alias record.
- [FSResolveAliasWithMountFlags](./api-1444279-fsresolvealiaswithmountflags.md)
  Returns an `FSRef` to the target of an alias.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1444389-fsmatchaliasbulk)*