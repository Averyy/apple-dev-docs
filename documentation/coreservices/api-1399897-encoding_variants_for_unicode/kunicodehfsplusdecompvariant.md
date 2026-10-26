# kUnicodeHFSPlusDecompVariant

**Framework**: Core Services  
**Kind**: econst  
**Role**: Enumeration Case

Specifies canonical decomposition according to Unicode 3.2 rules, with HFS+ exclusions ("HFS+ decomposition 3.2"). That is, it doesn't decompose in 2000-2FFF, F900-FAFF, 2F800-2FAFF. You can use ths option when converting HFS file names.

**Availability**:
- Mac Catalyst 17.0+
- macOS 10.2+

## Declaration

```c
kUnicodeHFSPlusDecompVariant = 8
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1399897-encoding_variants_for_unicode/kunicodehfsplusdecompvariant)*