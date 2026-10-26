# kUnicodeUseFallbacksMask

**Framework**: Core Services  
**Kind**: econst  
**Role**: Enumeration Case

**Availability**:
- Mac Catalyst 17.0+
- macOS 10.0+

## Declaration

```c
kUnicodeUseFallbacksMask = 1L << kUnicodeUseFallbacksBit
```

#### Discussion

A mask for setting the Unicode-use-fallbacks conversion flag. The Unicode Converter uses fallback mappings when it encounters a source text element for which there is no equivalent destination encoding. Fallback mappings are mappings that do not preserve the meaning or identity of the source character but represent a useful approximation of it. See the function [`SetFallbackUnicodeToText`](../api-1433614-setfallbackunicodetotext.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1433493-conversion_masks/kunicodeusefallbacksmask)*