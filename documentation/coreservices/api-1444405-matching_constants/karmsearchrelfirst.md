# kARMSearchRelFirst

**Framework**: Core Services  
**Kind**: econst  
**Role**: Enumeration Case

**Availability**:
- Mac Catalyst 13.1+ - Deprecated in 13.1
- macOS 10.0+ - Deprecated in 10.8

## Declaration

```c
kARMSearchRelFirst = 0x00000400
```

## Discussion

If `kARMSearch` is also set, perform a relative search before the absolute search. (If `kARMSearch` is also set and the target is found through the absolute search, `MatchAlias` sets the `needsUpdate` flag to `true`.) If neither `kARMSearch` nor `kARMSearchMore` is set, perform only a relative search. If `kARMSearch` is not set but `kARMSearchMore` is set, perform a relative search followed by an exhaustive search.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1444405-matching_constants/karmsearchrelfirst)*