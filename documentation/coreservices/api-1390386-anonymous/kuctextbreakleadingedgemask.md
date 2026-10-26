# kUCTextBreakLeadingEdgeMask

**Framework**: Core Services  
**Kind**: econst  
**Role**: Enumeration Case

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```c
kUCTextBreakLeadingEdgeMask = 1L << 0
```

#### Discussion

If the corresponding bit is set, then the starting offset for the `UCFindTextBreak` function is assumed to be in the word containing the character following the offset; this is the normal case when searching forward. If the corresponding bit is clear, then the starting offset for `UCFindTextBreak` is assumed to be in the word containing the character preceding the offset; this is the normal case when searching backward.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1390386-anonymous/kuctextbreakleadingedgemask)*