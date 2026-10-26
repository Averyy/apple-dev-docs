# National Standard Text Encodings

**Framework**: Core Services  
**Kind**: enum  
**Role**: Enumeration

Specify text encodings for various national standards.

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
- [kTextEncodingUS_ASCII](./api-1400246-national_standard_text_encodings/ktextencodingus_ascii.md)
- [kTextEncodingJIS_X0201_76](./api-1400246-national_standard_text_encodings/ktextencodingjis_x0201_76.md)
  JIS Roman and 1-byte katakana (halfwidth). 
- [kTextEncodingJIS_X0208_83](./api-1400246-national_standard_text_encodings/ktextencodingjis_x0208_83.md)
- [kTextEncodingJIS_X0208_90](./api-1400246-national_standard_text_encodings/ktextencodingjis_x0208_90.md)
- [kTextEncodingJIS_X0212_90](./api-1400246-national_standard_text_encodings/ktextencodingjis_x0212_90.md)
- [kTextEncodingJIS_C6226_78](./api-1400246-national_standard_text_encodings/ktextencodingjis_c6226_78.md)
- [kTextEncodingShiftJIS_X0213_00](./api-1399701-encoding_variants_for_macroman/ktextencodingshiftjis_x0213_00.md)
  Shift-JIS format encoding of JIS X0213 planes 1 and 2
- [kTextEncodingGB_2312_80](./api-1400246-national_standard_text_encodings/ktextencodinggb_2312_80.md)
- [kTextEncodingGBK_95](./api-1400246-national_standard_text_encodings/ktextencodinggbk_95.md)
  Annex to GB13000-93, for Windows 95; EUC-CN extended.
- [kTextEncodingGB_18030_2000](./api-1400246-national_standard_text_encodings/ktextencodinggb_18030_2000.md)
- [kTextEncodingKSC_5601_87](./api-1400246-national_standard_text_encodings/ktextencodingksc_5601_87.md)
  This is the same as KSC 5601-92 without Johab annex. 
- [kTextEncodingKSC_5601_92_Johab](./api-1400246-national_standard_text_encodings/ktextencodingksc_5601_92_johab.md)
  KSC 5601-92 Johab annex. 
- [kTextEncodingCNS_11643_92_P1](./api-1400246-national_standard_text_encodings/ktextencodingcns_11643_92_p1.md)
  CNS 11643-1992 plane 1. 
- [kTextEncodingCNS_11643_92_P2](./api-1400246-national_standard_text_encodings/ktextencodingcns_11643_92_p2.md)
  CNS 11643-1992 plane 2. 
- [kTextEncodingCNS_11643_92_P3](./api-1400246-national_standard_text_encodings/ktextencodingcns_11643_92_p3.md)
  CNS 11643-1992 plane 3 (11643-1986 plane 14). 
- [kTextEncodingANSEL](./api-1400246-national_standard_text_encodings/ktextencodingansel.md)
- [kTextEncodingGB_18030_2005](./api-1400246-national_standard_text_encodings/ktextencodinggb_18030_2005.md)
- [kTextEncodingJIS_X0213_MenKuTen](./api-1400246-national_standard_text_encodings/ktextencodingjis_x0213_menkuten.md)
- [kTextEncodingShiftJIS_X0213](./api-1400246-national_standard_text_encodings/ktextencodingshiftjis_x0213.md)

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
- [MS-DOS and Windows Text Encodings](./api-1400434-ms-dos_and_windows_text_encodings.md)
  Specify text encodings for MS-DOS and Windows.
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

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1400246-national_standard_text_encodings)*