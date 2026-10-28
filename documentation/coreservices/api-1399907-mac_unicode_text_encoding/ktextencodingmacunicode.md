# kTextEncodingMacUnicode

**Framework**: Core Services  
**Kind**: econst  
**Role**: Enumeration Case

**Availability**:
- Mac Catalyst 17.0+
- macOS 10.0+

## Declaration

```c
kTextEncodingMacUnicode = 0x7E
```

## Discussion

Beginning with Mac OS 8.5, the set of Mac OS script codes has been extended for some Mac OS components to include Unicode. Some of these components have only 7 bits available for script code, so `kTextEncodingUnicodeDefault` cannot be used to indicate Unicode. Instead, `kTextEncodingMacUnicode` is used as a meta-value to indicate that Unicode handles the script code a special Mac OS script code. The Text Encoding Converter handles this value similar to the way it handles the constant `kTextEncodingUnicodeDefault`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1399907-mac_unicode_text_encoding/ktextencodingmacunicode)*