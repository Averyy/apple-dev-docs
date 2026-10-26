# kUCCollatePunctuationSignificantMask

**Framework**: Core Services  
**Kind**: econst  
**Role**: Enumeration Case

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```c
kUCCollatePunctuationSignificantMask = 1L << 15
```

#### Discussion

If the corresponding bit is set, then punctuation and symbols are treated as significant instead of ignorable. This will produce results closer to the behavior of the older non-Unicode Mac OS collation functions. This option is available with Mac OS 9 and later.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1390427-anonymous/kuccollatepunctuationsignificantmask)*