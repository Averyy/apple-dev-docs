# kUnicodeMapLineFeedToReturnMask

**Framework**: Core Services  
**Kind**: econst  
**Role**: Enumeration Case

**Availability**:
- Mac Catalyst 17.0+
- macOS 10.2+

## Declaration

```c
kUnicodeMapLineFeedToReturnMask = 1L << kUnicodeMapLineFeedToReturnBit
```

## Discussion

Specifies mapping o the LF (LineFeed) character used in Unix to represent new lines to the CR (CarriageReturn) used in  Mac encodings. This option has an effect only when used with the constant `kUnicodeLooseMappingsMask`. You can pass both constants  as  `iControlFlags` parameters to the functions `ConvertFromUnicodeToText`, `ConvertFromUnicodeToTextRun`, and `ConvertFromUnicodeToScriptCodeRun`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1433493-conversion_masks/kunicodemaplinefeedtoreturnmask)*