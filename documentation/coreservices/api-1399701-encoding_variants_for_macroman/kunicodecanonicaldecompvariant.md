# kUnicodeCanonicalDecompVariant

**Framework**: Core Services  
**Kind**: econst  
**Role**: Enumeration Case

**Availability**:
- Mac Catalyst 17.0+
- macOS 10.0+

## Declaration

```c
kUnicodeCanonicalDecompVariant = 2
```

#### Discussion

A variant of Unicode using maximal decomposition with characters in canonical order. This variant does not include most characters which have a canonical decomposition, such as single characters for accented Latin letters or single characters for Korean Hangul syllables (however, this restriction is relaxed for symbol characters in the range U+2000 to U+2FFF). In TEC Manager 1.3, the Unicode Converter supports this variant for converting to and from Mac OS encodings.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1399701-encoding_variants_for_macroman/kunicodecanonicaldecompvariant)*