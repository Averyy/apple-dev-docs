# Matching Constants

**Framework**: Core Services  
**Kind**: enum  
**Role**: Enumeration

Specify the matching criteria for the alias matching functions.

**Availability**:
- Mac Catalyst 13.1+ - Deprecated in 13.1
- macOS 10.0+ - Deprecated in 10.8

## Declaration

```c
enum : unsigned int {
    ...
};
```

## Topics

### Constants
- [kARMMountVol](./api-1444405-matching_constants/karmmountvol.md)
  Automatically try to mount the target’s volume if it is not mounted.
- [kARMNoUI](./api-1444405-matching_constants/karmnoui.md)
  Stop if a search requires user interaction, such as a password dialog box when mounting a remote volume. If user interaction is needed and `kARMNoUI` is in effect, the search fails.
- [kARMMultVols](./api-1444405-matching_constants/karmmultvols.md)
- [kARMSearch](./api-1444405-matching_constants/karmsearch.md)
  Perform a fast search for the alias target. If `kARMSearchRelFirst` is not set, perform an absolute search first, followed by a relative search only if the value of the `fromFile` parameter is not `NULL` and the list of matches is not full.
- [kARMSearchMore](./api-1444405-matching_constants/karmsearchmore.md)
- [kARMSearchRelFirst](./api-1444405-matching_constants/karmsearchrelfirst.md)
- [kARMTryFileIDFirst](./api-1444405-matching_constants/karmtryfileidfirst.md)
  Perform a search using the file ID of the target before searching using the path.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1444405-matching_constants)*