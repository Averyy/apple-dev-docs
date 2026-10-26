# kTECFallbackTextLengthFixBit

**Framework**: Core Services  
**Kind**: econst  
**Role**: Enumeration Case

**Availability**:
- Mac Catalyst 17.0+
- macOS 10.0+

## Declaration

```c
kTECFallbackTextLengthFixBit = 1
```

#### Discussion

This is set if the Unicode Converter has a bug fix to use the source length (`srcConvLen) `and destination length (`destConvLen)` returned by a caller-supplied fall-back handler for any status it returns except `kTECUnmappableElementErr`. Previously it honored only these values if `noErr` was returned.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1400304-unicode_converter_flags/ktecfallbacktextlengthfixbit)*