# MS-DOS and Windows Text Encodings

**Framework**: Core Services  
**Kind**: enum  
**Role**: Enumeration

Specify text encodings for MS-DOS and Windows.

**Availability**:
- Mac Catalyst 17.0+
- macOS 10.0+

## Declaration

```c
enum : unsigned int {
    ...
};
```

## Topics

### Constants
- [kTextEncodingDOSLatinUS](./api-1400434-ms-dos_and_windows_text_encodings/ktextencodingdoslatinus.md)
  Code page 437.
- [kTextEncodingDOSGreek](./api-1400434-ms-dos_and_windows_text_encodings/ktextencodingdosgreek.md)
  Code page 737, formerly 437G.
- [kTextEncodingDOSBalticRim](./api-1400434-ms-dos_and_windows_text_encodings/ktextencodingdosbalticrim.md)
  Code page 775.
- [kTextEncodingDOSLatin1](./api-1400434-ms-dos_and_windows_text_encodings/ktextencodingdoslatin1.md)
  Code page 860. “multilingual.”
- [kTextEncodingDOSGreek1](./api-1400434-ms-dos_and_windows_text_encodings/ktextencodingdosgreek1.md)
  Code page 851.
- [kTextEncodingDOSLatin2](./api-1400434-ms-dos_and_windows_text_encodings/ktextencodingdoslatin2.md)
  Code page 852, Slavic.
- [kTextEncodingDOSCyrillic](./api-1400434-ms-dos_and_windows_text_encodings/ktextencodingdoscyrillic.md)
  Code page 855, IBM Cyrillic.
- [kTextEncodingDOSTurkish](./api-1400434-ms-dos_and_windows_text_encodings/ktextencodingdosturkish.md)
  Code page 857, IBM Turkish.
- [kTextEncodingDOSPortuguese](./api-1400434-ms-dos_and_windows_text_encodings/ktextencodingdosportuguese.md)
  Code page 860.
- [kTextEncodingDOSIcelandic](./api-1400434-ms-dos_and_windows_text_encodings/ktextencodingdosicelandic.md)
  Code page 861.
- [kTextEncodingDOSHebrew](./api-1400434-ms-dos_and_windows_text_encodings/ktextencodingdoshebrew.md)
  Code page 862.
- [kTextEncodingDOSCanadianFrench](./api-1400434-ms-dos_and_windows_text_encodings/ktextencodingdoscanadianfrench.md)
  Code page 863.
- [kTextEncodingDOSArabic](./api-1400434-ms-dos_and_windows_text_encodings/ktextencodingdosarabic.md)
  Code page 864.
- [kTextEncodingDOSNordic](./api-1400434-ms-dos_and_windows_text_encodings/ktextencodingdosnordic.md)
  Cde page 865.
- [kTextEncodingDOSRussian](./api-1400434-ms-dos_and_windows_text_encodings/ktextencodingdosrussian.md)
  Code page 866.
- [kTextEncodingDOSGreek2](./api-1400434-ms-dos_and_windows_text_encodings/ktextencodingdosgreek2.md)
  Code page 869, IBM Modern Green.
- [kTextEncodingDOSThai](./api-1400434-ms-dos_and_windows_text_encodings/ktextencodingdosthai.md)
  Code page 874, also for Windows.
- [kTextEncodingDOSJapanese](./api-1400434-ms-dos_and_windows_text_encodings/ktextencodingdosjapanese.md)
  Code page 932, also for Windows
- [kTextEncodingDOSChineseSimplif](./api-1400434-ms-dos_and_windows_text_encodings/ktextencodingdoschinesesimplif.md)
  Code page 936, also for Windows.
- [kTextEncodingDOSKorean](./api-1400434-ms-dos_and_windows_text_encodings/ktextencodingdoskorean.md)
  Code page 949, also for Windows; unified Hangul. 
- [kTextEncodingDOSChineseTrad](./api-1400434-ms-dos_and_windows_text_encodings/ktextencodingdoschinesetrad.md)
  Code page 950, also for Windows.
- [kTextEncodingWindowsLatin1](./api-1400434-ms-dos_and_windows_text_encodings/ktextencodingwindowslatin1.md)
  Code page 1252.
- [kTextEncodingWindowsANSI](./api-1400434-ms-dos_and_windows_text_encodings/ktextencodingwindowsansi.md)
  Code page 1252 (alternate name).
- [kTextEncodingWindowsLatin2](./api-1400434-ms-dos_and_windows_text_encodings/ktextencodingwindowslatin2.md)
  Code page 1250, Central Europe.
- [kTextEncodingWindowsCyrillic](./api-1400434-ms-dos_and_windows_text_encodings/ktextencodingwindowscyrillic.md)
  Code page 1251, Slavic Cyrillic.
- [kTextEncodingWindowsGreek](./api-1400434-ms-dos_and_windows_text_encodings/ktextencodingwindowsgreek.md)
  Code page 1253.
- [kTextEncodingWindowsLatin5](./api-1400434-ms-dos_and_windows_text_encodings/ktextencodingwindowslatin5.md)
  Code page 1254, Turkish.
- [kTextEncodingWindowsHebrew](./api-1400434-ms-dos_and_windows_text_encodings/ktextencodingwindowshebrew.md)
  Code page 1255.
- [kTextEncodingWindowsArabic](./api-1400434-ms-dos_and_windows_text_encodings/ktextencodingwindowsarabic.md)
  Code page 1256.
- [kTextEncodingWindowsBalticRim](./api-1400434-ms-dos_and_windows_text_encodings/ktextencodingwindowsbalticrim.md)
  Code page 1257.
- [kTextEncodingWindowsVietnamese](./api-1400434-ms-dos_and_windows_text_encodings/ktextencodingwindowsvietnamese.md)
  Code page 1258.
- [kTextEncodingWindowsKoreanJohab](./api-1400434-ms-dos_and_windows_text_encodings/ktextencodingwindowskoreanjohab.md)
  Code page 1361, for Window NT.

## See Also

### Encodings and Variants
- [TextEncodingBase](./textencodingbase.md)
  Specify base text encodings.
- [Compatibility TextEncodings](./api-1399939-compatibility_textencodings.md)
  Specify text encodings that are provided for backward compatibility.
- [EBCDIC and IBM Host Text Encodings](./api-1400244-ebcdic_and_ibm_host_text_encodin.md)
  Specify text encodings used by IBM computers.
- [Encoding Variants for Big-5](./api-1399673-encoding_variants_for_big-5.md)
  Specify variants of Big-5 encoding.
- [Encoding Variants for Mac OS Encodings](./api-1399862-encoding_variants_for_mac_os_enc.md)
  Specify variant Mac OS encodings that use script codes other than 0
- [Encoding Variants for MacArabic](./api-1399984-encoding_variants_for_macarabic.md)
  Specify variants of MacArabic.
- [Encoding Variants for MacCroatian](./api-1400365-encoding_variants_for_maccroatia.md)
  Specify variants of MacCroation.
- [Encoding Variants for MacCyrillic](./api-1400107-encoding_variants_for_maccyrilli.md)
  Specify variants of MacCyrillic.
- [Encoding Variants for MacFarsi](./api-1399681-encoding_variants_for_macfarsi.md)
  Specify variants of MacFarsi.
- [Encoding Variants for MacHebrew](./api-1400410-encoding_variants_for_machebrew.md)
  Specify variants of MacHebrew.
- [Encoding Variants for MacIcelandic](./api-1400089-encoding_variants_for_maciceland.md)
  Specify variants of MacIcelandic.
- [Encoding Variants for MacJapanese](./api-1399915-encoding_variants_for_macjapanes.md)
  Specify variants of MacJapanese.
- [Encoding Variants for MacRoman](./api-1399701-encoding_variants_for_macroman.md)
  Specify variants of MacRoman.
- [Encoding Variants for MacRoman Related to Currency](./api-1399860-encoding_variants_for_macroman_r.md)
  Specify variants of MacRoman that are related to currency.
- [Encoding Variants for MacRomanian](./api-1399955-encoding_variants_for_macromania.md)
  Specify variants of MacRomanian.
- [Encoding Variants for MacRomanLatin1](./api-1400256-encoding_variants_for_macromanla.md)
  Specify variants of MacRomanLatin1.
- [Encoding Variants for MacVT100](./api-1400045-encoding_variants_for_macvt100.md)
  Specify variants of MacVT100.
- [Encoding Variants for Unicode](./api-1399897-encoding_variants_for_unicode.md)
  Specify variants of Unicode.
- [EUC Text Encodings](./api-1399707-euc_text_encodings.md)
  Specify Extendec Unix Code text encodings.
- [HFS Text Encoding](./api-1400242-hfs_text_encoding.md)
  Specifies a Mac OS HFS text encoding.
- [ISO 2022 Text Encodings](./api-1400073-iso_2022_text_encodings.md)
  Specify text encodings for ISO 2002.
- [ISO 8-bit and 7-bit Text Encodings](./api-1399699-iso_8-bit_and_7-bit_text_encodings.md)
  Specify text encodings for ISO 8-bit and 7-bit.
- [Mac Unicode Text Encoding](./api-1399907-mac_unicode_text_encoding.md)
  Specifies a script code that should be handled as a special Mac OS script code.
- [Miscellaneous Text Encoding Standards](./api-1399782-miscellaneous_text_encoding_stan.md)
  Specify miscellaneous text encodings.
- [National Standard Text Encodings](./api-1400246-national_standard_text_encodings.md)
  Specify text encodings for various national standards.
- [NextStep Platform Encodings](./api-1400238-nextstep_platform_encodings.md)
  Specify text encodings for the NextStep platform.
- [Special Text Encoding Values](./api-1400396-special_text_encoding_values.md)
  Specify special cases of text encodings.
- [TextEncodingFormat](./textencodingformat.md)
  Specify a text encoding format.
- [TextEncodingNameSelector](./textencodingnameselector.md)
  Specify the part of an encoding name you want to obtain.
- [Text Encoding Variants](./api-1400145-text_encoding_variants.md)
  Specify minor variants of a base encoding or group of base encodings.
- [Unicode and ISO UCS Text Encodings](./api-1400188-unicode_and_iso_ucs_text_encodin.md)
  Specify Unicode and IOS UCS text encodings.
- [Unsupported Unicode Variants](./api-1400371-unsupported_unicode_variants.md)
  Represent Unicode variants that are not yet supported or fully defined.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1400434-ms-dos_and_windows_text_encodings)*