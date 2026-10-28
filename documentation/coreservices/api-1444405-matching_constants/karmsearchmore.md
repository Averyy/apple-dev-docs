# kARMSearchMore

**Framework**: Core Services  
**Kind**: econst  
**Role**: Enumeration Case

**Availability**:
- Mac Catalyst 13.1+ - Deprecated in 13.1
- macOS 10.0+ - Deprecated in 10.8

## Declaration

```c
kARMSearchMore = 0x00000200
```

## Discussion

Perform an exhaustive search for the alias target. On HFS volumes, the exhaustive search uses the File Manager function `PBCatSearch` to identify candidates with matching creation date, type, and creator. The `PBCatSearch` function is available only on HFS volumes and only on systems running version 7.0 or later. On MFS volumes or HFS volumes that do not support `PBCatSearch`, the exhaustive search makes a series of indexed calls to File Manager functions, using the same search criteria. If you set `kARMSearchMore` and either or both of `kARMSearch` and `kARMSearchRelFirst`, `MatchAlias` performs the fast search first.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1444405-matching_constants/karmsearchmore)*