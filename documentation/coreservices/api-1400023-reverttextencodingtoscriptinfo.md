# RevertTextEncodingToScriptInfo

**Framework**: Core Services  
**Kind**: func  
**Role**: Function

Converts the given Mac OS text encoding specificationto the corresponding script code and, if possible, language codeand font name.

**Availability**:
- macOS 10.0+

## Declaration

```c
OSStatus RevertTextEncodingToScriptInfo(TextEncoding iEncoding, ScriptCode *oTextScriptID, LangCode *oTextLanguageID, Str255 oTextFontname);
```

#### Return Value

A result code. See [Result Codes](./carbon_core/text_encoding_conversion_manager.md#1664324).The function returns `paramErr` ifthe text encoding specification input parameter value is invalid. Thefunction returns a `kTECTableFormatErr `resultcode if the internal mapping tables used for translation are invalid.For a list of other possible result codes, see “Data Types”.

#### Discussion

If you have applications that use Mac OS Script Manager andFont Manager functions, you can use the `RevertTextEncodingToScriptInfo` functionto convert information in a text encoding specification into theappropriate Mac OS script code, language code, and font name, ifthey can be unambiguously derived. Your application can then usethis information to display text to a user on the screen. 

For more information see the  [`UpgradeScriptInfoToTextEncoding`](./api-1399625-upgradescriptinfototextencoding.md)  functionand  [`TextEncodingBase`](./textencodingbase.md). 

## Parameters

- `iEncoding`: The text encoding specification to be converted. 
- `oTextScriptID`:  A pointer to a value of type `ScriptCode`. On return, a Mac OS script code that corresponds to the text encoding specification you identified in the `iEncoding` parameter. If you do not pass a pointer for this parameter, the function returns a `paramErr` result code. 
- `oTextLanguageID`: A pointer to a value of type `LangCode`. On input, if you do not want the function to return the language code, specify `NULL` as the value of this parameter. On return, the appropriate language code, if the language can be unambiguously derived from the text encoding specification, for example, Japanese, and you did not set the parameter to `NULL`.

  If you do not specify `NULL` on input and the language is ambiguous—that is, the function cannot accurately derive it from the text encoding specification—the function returns a value of `kTextLanguageDontCare`.
- `oTextFontname`:  A Pascal string. On input, if you do not want the function to return the font name, specify `NULL` as the value of this parameter. On return, the name of the appropriate font if the font can be unambiguously derived from the text encoding specification, for example, Symbol, and you did not set the parameter to `NULL`. 

  If you do not specify `NULL` on input and the font is ambiguous—that is, the function cannot accurately derive it from the text encoding specification—the function returns a zero-length string.

## See Also

### Converting Between Script Manager Values and Text Encodings
- [UpgradeScriptInfoToTextEncoding](./api-1399625-upgradescriptinfototextencoding.md)
  Converts any combination of a Mac OS script code, a languagecode, a region code, and a font name to a text encoding.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1400023-reverttextencodingtoscriptinfo)*