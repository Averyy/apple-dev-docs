# TextEncodingBase

**Framework**: Core Services  
**Kind**: tdef  
**Role**: Type Alias

Specify base text encodings.

**Availability**:
- Mac Catalyst 17.0+
- macOS 10.0+

## Declaration

```c
typedef UInt32 TextEncodingBase;
```

## Discussion

You use a base text encoding data type to specify which text encoding or text encoding scheme you have used to express a given text. The text encoding base value is the primary specification of the source or target encoding. Values 0 through 32 correspond directly to Mac OS script codes. Values 33 through 254 are for other Mac OS encodings that do not have their own script codes, such as the Symbol encoding implemented by the Symbol font. You can also specify a meta-value as a base text encoding, such as `kTextEncodingMacHFS` and `kTextEncodingUnicodeDefault`. A meta-value is mapped to a real value. 

The function [`GetTextEncodingBase`](./api-1399792-gettextencodingbase.md) returns the text encoding base of a text encoding specification.

A base text encoding is defined by the `TextEncodingBase` data type.  

## Topics

### Constants
- [kTextEncodingMacRoman](./api-1399980-afp_text_encodings/ktextencodingmacroman.md)
  The encoding for Mac OS Roman.
- [kTextEncodingMacJapanese](./api-1399980-afp_text_encodings/ktextencodingmacjapanese.md)
  The encoding for Mac OS Japanese.
- [kTextEncodingMacChineseTrad](./api-1399980-afp_text_encodings/ktextencodingmacchinesetrad.md)
  The encoding for Mac OS traditional Chinese.
- [kTextEncodingMacKorean](./api-1399980-afp_text_encodings/ktextencodingmackorean.md)
  The encoding for Mac OS Korean.
- [kTextEncodingMacArabic](./api-1399980-afp_text_encodings/ktextencodingmacarabic.md)
  The encoding for Mac OS Arabic.
- [kTextEncodingMacHebrew](./api-1399980-afp_text_encodings/ktextencodingmachebrew.md)
  The encoding for Mac OS Hebrew.
- [kTextEncodingMacGreek](./api-1399980-afp_text_encodings/ktextencodingmacgreek.md)
  The encoding for Mac OS Greek.
- [kTextEncodingMacCyrillic](./api-1399980-afp_text_encodings/ktextencodingmaccyrillic.md)
  The encoding for Mac OS Cyrillic.
- [kTextEncodingMacDevanagari](./api-1399980-afp_text_encodings/ktextencodingmacdevanagari.md)
  The encoding for Mac OS Devanagari.
- [kTextEncodingMacGurmukhi](./api-1399980-afp_text_encodings/ktextencodingmacgurmukhi.md)
  The encoding for Mac OS Gurmukhi.
- [kTextEncodingMacGujarati](./api-1399980-afp_text_encodings/ktextencodingmacgujarati.md)
  The encoding for Mac OS Gujurati.
- [kTextEncodingMacOriya](./api-1399980-afp_text_encodings/ktextencodingmacoriya.md)
  The encoding for Mac OS Oriya.
- [kTextEncodingMacBengali](./api-1399980-afp_text_encodings/ktextencodingmacbengali.md)
  The encoding for Mac OS Bengali.
- [kTextEncodingMacTamil](./api-1399980-afp_text_encodings/ktextencodingmactamil.md)
  The encoding for Mac OS Tamil.
- [kTextEncodingMacTelugu](./api-1399980-afp_text_encodings/ktextencodingmactelugu.md)
  The encoding for Mac OS Telugu.
- [kTextEncodingMacKannada](./api-1399980-afp_text_encodings/ktextencodingmackannada.md)
  The encoding for Mac OS Kannada.
- [kTextEncodingMacMalayalam](./api-1399980-afp_text_encodings/ktextencodingmacmalayalam.md)
  The encoding for Mac OS Malayalam.
- [kTextEncodingMacSinhalese](./api-1399980-afp_text_encodings/ktextencodingmacsinhalese.md)
  The encoding for Mac OS Sinhalese.
- [kTextEncodingMacBurmese](./api-1399980-afp_text_encodings/ktextencodingmacburmese.md)
  The encoding for Mac OS Burmese.
- [kTextEncodingMacKhmer](./api-1399980-afp_text_encodings/ktextencodingmackhmer.md)
  The encoding for Mac OS Khmer.
- [kTextEncodingMacThai](./api-1399980-afp_text_encodings/ktextencodingmacthai.md)
  The encoding for Mac OS Thai.
- [kTextEncodingMacLaotian](./api-1399980-afp_text_encodings/ktextencodingmaclaotian.md)
  The encoding for Mac OS Laotian.
- [kTextEncodingMacGeorgian](./api-1399980-afp_text_encodings/ktextencodingmacgeorgian.md)
  The encoding for Mac OS Georgian.
- [kTextEncodingMacArmenian](./api-1399980-afp_text_encodings/ktextencodingmacarmenian.md)
  The encoding for Mac OS Armenian.
- [kTextEncodingMacChineseSimp](./api-1399980-afp_text_encodings/ktextencodingmacchinesesimp.md)
  The encoding for Mac OS simple Chinese.
- [kTextEncodingMacTibetan](./api-1399980-afp_text_encodings/ktextencodingmactibetan.md)
  The encoding for Mac OS Tibetan.
- [kTextEncodingMacMongolian](./api-1399980-afp_text_encodings/ktextencodingmacmongolian.md)
  The encoding for Mac OS Mongolian.
- [kTextEncodingMacEthiopic](./api-1399980-afp_text_encodings/ktextencodingmacethiopic.md)
  The encoding for Mac OS Ethiopic.
- [kTextEncodingMacCentralEurRoman](./api-1399980-afp_text_encodings/ktextencodingmaccentraleurroman.md)
  The encoding for Mac OS Central European Roman.
- [kTextEncodingMacVietnamese](./api-1399980-afp_text_encodings/ktextencodingmacvietnamese.md)
  The encoding for Mac OS Vietnamese.
- [kTextEncodingMacExtArabic](./api-1399980-afp_text_encodings/ktextencodingmacextarabic.md)
  The encoding for Mac OS ExtArabic.
- [kTextEncodingMacSymbol](./api-1399980-afp_text_encodings/ktextencodingmacsymbol.md)
  This Mac OS encoding uses script code 0, `smRoman`.
- [kTextEncodingMacDingbats](./api-1399980-afp_text_encodings/ktextencodingmacdingbats.md)
  This Mac OS encoding uses script code 0, `smRoman`.
- [kTextEncodingMacTurkish](./api-1399980-afp_text_encodings/ktextencodingmacturkish.md)
  This Mac OS encoding uses script code 0, `smRoman`.
- [kTextEncodingMacCroatian](./api-1399980-afp_text_encodings/ktextencodingmaccroatian.md)
  This Mac OS encoding uses script code 0, `smRoman`.
- [kTextEncodingMacIcelandic](./api-1399980-afp_text_encodings/ktextencodingmacicelandic.md)
  This Mac OS encoding uses script code 0, `smRoman`.
- [kTextEncodingMacRomanian](./api-1399980-afp_text_encodings/ktextencodingmacromanian.md)
  This Mac OS encoding uses script code 0, `smRoman`.
- [kTextEncodingMacCeltic](./api-1399980-afp_text_encodings/ktextencodingmacceltic.md)
  This Mac OS encoding uses script code 0, `smRoman`.
- [kTextEncodingMacGaelic](./api-1399980-afp_text_encodings/ktextencodingmacgaelic.md)
  This Mac OS encoding uses script code 0, `smRoman`.
- [kTextEncodingMacKeyboardGlyphs](./api-1399980-afp_text_encodings/ktextencodingmackeyboardglyphs.md)

## See Also

### Encodings and Variants
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

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/textencodingbase)*