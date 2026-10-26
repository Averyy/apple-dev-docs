# kUnicodeMatchOtherBaseMask

**Framework**: Core Services  
**Kind**: econst  
**Role**: Enumeration Case

If set, excludes mappings that do not match the text encoding base of the `otherEncoding` field of the structure [`UnicodeMapping`](../unicodemapping.md). If not set, the function ignores the text encoding base of that field. 

**Availability**:
- Mac Catalyst 17.0+
- macOS 10.0+

## Declaration

```c
kUnicodeMatchOtherBaseMask = 1L << kUnicodeMatchOtherBaseBit
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1433554-unicode_matching_masks/kunicodematchotherbasemask)*