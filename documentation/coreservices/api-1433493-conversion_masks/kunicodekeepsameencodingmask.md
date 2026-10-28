# kUnicodeKeepSameEncodingMask

**Framework**: Core Services  
**Kind**: econst  
**Role**: Enumeration Case

**Availability**:
- Mac Catalyst 17.0+
- macOS 10.0+

## Declaration

```c
kUnicodeKeepSameEncodingMask = 1L << kUnicodeKeepSameEncodingBit
```

## Discussion

A mask for setting the keep-same-encoding control flag. Determines how the Unicode Converter treats the conversion of Unicode text following a text element that could not be converted to the first destination encoding when multiple destination encodings exist. This control flag applies only if the `kUnicodeTextRunMask` control flag is set. 

If you set this flag, the function [`ConvertFromUnicodeToTextRun`](../api-1433511-convertfromunicodetotextrun.md) attempts to minimize encoding changes in the conversion of the source text string; that is, once it is forced to make an encoding change, it attempts to use that encoding as the conversion destination for as long as possible. 

If you clear this flag, `ConvertFromUnicodeToTextRun` attempts to keep most of the converted string in one encoding, switching to other encodings only when necessary. 


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1433493-conversion_masks/kunicodekeepsameencodingmask)*