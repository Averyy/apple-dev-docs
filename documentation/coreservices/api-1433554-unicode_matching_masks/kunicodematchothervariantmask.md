# kUnicodeMatchOtherVariantMask

**Framework**: Core Services  
**Kind**: econst  
**Role**: Enumeration Case

If set, excludes mappings that do not match the text encoding variant of the `otherEncoding` field of the specified Unicode mapping structure. If not set, the function ignores the text encoding variant of that field.

**Availability**:
- Mac Catalyst 17.0+
- macOS 10.0+

## Declaration

```c
kUnicodeMatchOtherVariantMask = 1L << kUnicodeMatchOtherVariantBit
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1433554-unicode_matching_masks/kunicodematchothervariantmask)*