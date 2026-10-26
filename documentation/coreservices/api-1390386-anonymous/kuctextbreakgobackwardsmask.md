# kUCTextBreakGoBackwardsMask

**Framework**: Core Services  
**Kind**: econst  
**Role**: Enumeration Case

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```c
kUCTextBreakGoBackwardsMask = 1L << 1
```

#### Discussion

If the corresponding bit is set, then `UCFindTextBreak` searches backward from the value provided in its `startOffset` parameter to find the next text break. If the corresponding bit is clear, then `UCFindTextBreak` searches forward from the `startOffset` value to find the next text break.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1390386-anonymous/kuctextbreakgobackwardsmask)*