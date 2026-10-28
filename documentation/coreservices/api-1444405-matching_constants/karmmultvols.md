# kARMMultVols

**Framework**: Core Services  
**Kind**: econst  
**Role**: Enumeration Case

**Availability**:
- Mac Catalyst 13.1+ - Deprecated in 13.1
- macOS 10.0+ - Deprecated in 10.8

## Declaration

```c
kARMMultVols = 0x00000008
```

## Discussion

Search all mounted volumes. The search begins with the volume on which the target resided when the record was created. When you specify a fast search of all mounted volumes, `MatchAlias` performs a formal fast search only on the volume described in the alias record. On all other volumes it looks for the target by ID or by name in the directory with the specified parent directory ID. When you specify an exhaustive search of multiple volumes, `MatchAlias` performs the same search on all volumes. When resolving an alias record created by `NewAliasMinimalFromFullPath`, `MatchAlias` ignores this flag.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1444405-matching_constants/karmmultvols)*