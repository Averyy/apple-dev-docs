# TextEncodingFormat

**Framework**: Core Services  
**Kind**: tdef  
**Role**: Type Alias

Specify a text encoding format.

**Availability**:
- Mac Catalyst 17.0+
- macOS 10.0+

## Declaration

```c
typedef UInt32 TextEncodingFormat;
```

## Discussion

A text encoding format specifies a way of formatting or algorithmically transforming a particular base encoding. For example, the UTF-7 format is the Unicode standard formatted for transmission through channels that can handle only 7-bit values. Other text encoding formats for Unicode include UTF-8 and 16-bit or 32-bit formats. These transformations are not viewed as different base encodings. Rather, they are different formats for representing the same base encoding.

Similar to text encoding variant values, text encoding format values are specific to a particular text encoding base value or to a small set of text encoding base values. A text encoding format is defined by the `TextEncodingFormat` data type.

The function [`GetTextEncodingFormat`](./api-1400318-gettextencodingformat.md) returns the text encoding format of a text encoding specification.

## Topics

### Constants
- [kTextEncodingDefaultFormat](./api-1400077-anonymous/ktextencodingdefaultformat.md)
  The standard default format for any base encoding. 
- [kUnicode16BitFormat](./api-1400077-anonymous/kunicode16bitformat.md)
  The 16-bit character encoding format specified by the Unicode standard, equivalent to the UCS-2 format for ISO 10646. This includes support for the UTF-16 method of including non-BMP characters in a stream of 16-bit values. 
- [kUnicodeUTF7Format](./api-1400077-anonymous/kunicodeutf7format.md)
  The Unicode transformation format in which characters encodings are represented by a sequence of 7-bit values. This format cannot be handled by the Unicode Converter, only by the Text Encoding Converter. 
- [kUnicodeUTF8Format](./api-1400077-anonymous/kunicodeutf8format.md)
  The Unicode transformation format in which characters are represented by a sequence of 8-bit values. 
- [kUnicode32BitFormat](./api-1400077-anonymous/kunicode32bitformat.md)
  The UCS-4 32-bit format defined for ISO 10646. This format is not currently supported. 

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
- [National Standard Text Encodings](./api-1400246-national_standard_text_encodings.md)
  Specify text encodings for various national standards.
- [NextStep Platform Encodings](./api-1400238-nextstep_platform_encodings.md)
  Specify text encodings for the NextStep platform.
- [Special Text Encoding Values](./api-1400396-special_text_encoding_values.md)
  Specify special cases of text encodings.
- [TextEncodingNameSelector](./textencodingnameselector.md)
  Specify the part of an encoding name you want to obtain.
- [Text Encoding Variants](./api-1400145-text_encoding_variants.md)
  Specify minor variants of a base encoding or group of base encodings.
- [Unicode and ISO UCS Text Encodings](./api-1400188-unicode_and_iso_ucs_text_encodin.md)
  Specify Unicode and IOS UCS text encodings.
- [Unsupported Unicode Variants](./api-1400371-unsupported_unicode_variants.md)
  Represent Unicode variants that are not yet supported or fully defined.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/textencodingformat)*