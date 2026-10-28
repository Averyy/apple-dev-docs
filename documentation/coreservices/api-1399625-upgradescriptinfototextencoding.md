# UpgradeScriptInfoToTextEncoding

**Framework**: Core Services  
**Kind**: func  
**Role**: Function

Converts any combination of a Mac OS script code, a languagecode, a region code, and a font name to a text encoding.

**Availability**:
- macOS 10.0+

## Declaration

```c
OSStatus UpgradeScriptInfoToTextEncoding(ScriptCode iTextScriptID, LangCode iTextLanguageID, RegionCode iRegionID, ConstStr255Param iTextFontname, TextEncoding *oEncoding);
```

## Return Value

A resultcode. See [Result Codes](./carbon_core/text_encoding_conversion_manager.md#1664324). This function returns `paramErr` iftwo or more of the input parameter values conflict in some way—forexample, the Mac OS language code does not belong to the script whosescript code you specified, or if the input parameter values are invalid.The function returns a `kTECTableFormatErr` resultcode if the internal mapping tables used for translation are invalid.

## Discussion

The `UpgradeScriptInfoToTextEncoding` functionallows you to derive a text encoding specification from script codes,language codes, region codes, and font names. A one-to-one correspondenceexists between many of the Script Manager’s script codes and aparticular Mac OS text encoding base value. However, because textencodings are a superset of script codes, some combinations of scriptcode, language code, region code, and font name might result ina different text encoding base value than would be the case if thetranslation were based on the script code alone. 

When you call the `UpgradeScriptInfoToTextEncoding` function,you can specify any combination of its parameters, but you mustspecify at least one. 

If you don’t specify an explicit value for a script, language,or region code parameter, you must pass the do-not-care constantappropriate to that parameter. If you do not specify an explicitvalue for `iTextFontName`,you must pass `NULL`. `UpgradeScriptInfoToTextEncoding` usesas much information as you supply to determine the equivalent textencoding or the closest approximation. If you provide more thanone parameter, all parameters are checked against one another toensure that they are valid in combination. 

A font name, such as `'Symbol'` or `'ZapfDingbats,'` can indicate a particular textencoding base. Other font names can indicate particular variantsassociated with a particular text encoding base. Otherwise, thefont name is used to obtain a script code, and this script code willbe checked against any script code you supply (in this case, thefont must be installed; if it is not, the function returns a `paramErr` resultcode). If you do not supply either a language code or a region codeand the script code you supply or the one that is derived matchesthe system script, then the system’s localization is used to determinethe appropriate region and language code. This is used for derivingtext encoding base values that depend on region and language, suchas `kTextEncodingMacTurkish`. 

For more information see the  [`RevertTextEncodingToScriptInfo`](./api-1400023-reverttextencodingtoscriptinfo.md)  functionand  [`TextEncodingBase`](./textencodingbase.md). 

## Parameters

- `iTextScriptID`: A valid Script Manager script code. The Mac OS Script Manager defines constants for script codes using this format: `sm`Xxx. To designate the system script, specify the meta-value of `smSystemScript`. To designate the current script based on the font specified in the graphics port (`grafPort`), specify the metavalue of `smCurrentScript`. To indicate that you do not want to provide a script code for this parameter, specify the constant `kTextScriptDontCare`. 
- `iTextLanguageID`: A valid Script Manager language code. The Mac OS Script Manager defines constants for language codes using this format: `lang`Xxx. To indicate that you do not want to provide a language code for this parameter, specify the constant `kTextLanguageDontCare`. 
- `iRegionID`: A valid Script Manager region code. The Mac OS Script Manager defines constants for region codes using this format: `ver`Xxx. To indicate that you do not want to provide a region code for this parameter, specify the constant `kTextRegionDontCare`. 
- `iTextFontname`: The name of a font associated with a particular text encoding specification, such as Symbol or Zapf Dingbats, or the name of any font that is currently installed on the system. To indicate that you do not want to provide a font name, specify a value of `NULL`. 
- `oEncoding`: A pointer to a value of type `TextEncoding`. On return, this value holds the text encoding specification that the function created from the other values you provided. 

## See Also

### Converting Between Script Manager Values and Text Encodings
- [RevertTextEncodingToScriptInfo](./api-1400023-reverttextencodingtoscriptinfo.md)
  Converts the given Mac OS text encoding specificationto the corresponding script code and, if possible, language codeand font name.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1399625-upgradescriptinfototextencoding)*