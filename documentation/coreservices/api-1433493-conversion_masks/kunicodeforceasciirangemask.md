# kUnicodeForceASCIIRangeMask

**Framework**: Core Services  
**Kind**: econst  
**Role**: Enumeration Case

**Availability**:
- Mac Catalyst 17.0+
- macOS 10.0+

## Declaration

```c
kUnicodeForceASCIIRangeMask = 1L << kUnicodeForceASCIIRangeBit
```

## Discussion

A mask for setting the force ASCII range control flag. If an encoding normally treats 1-byte code points `0x00`–`0x7F` as an ISO 646 national variant that is different from ASCII, setting this flag forces `0x00`–`0x7F` to be treated as ASCII. For example, Japanese encodings such as Shift-JIS generally treat `0x00`–`0x7F` as JIS Roman, with `0x5C` as YEN SIGN instead of REVERSE SOLIDUS, but when converting a DOS file path you may want to set this flag so that `0x5C` is mapped as REVERSE SOLIDUS.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1433493-conversion_masks/kunicodeforceasciirangemask)*