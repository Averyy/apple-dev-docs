# TruncateForUnicodeToText

**Framework**: Core Services  
**Kind**: func  
**Role**: Function

Identifies where your application can safely break a Unicodestring to be converted to any encoding so that the string is brokenin a way that preserves the text element integrity. 

**Availability**:
- macOS 10.0+

## Declaration

```c
OSStatus TruncateForUnicodeToText(ConstUnicodeToTextInfo iUnicodeToTextInfo, ByteCount iSourceLen, const UniChar iSourceStr[], OptionBits iControlFlags, ByteCount iMaxLen, ByteCount *oTruncatedLen);
```

#### Return Value

A resultcode. See [Result Codes](./carbon_core/text_encoding_conversion_manager.md#1664324).

#### Discussion

Your application can use this function to divide up a Unicodestring properly truncating each portion before you call `ConvertFromUnicodeToText` or `ConvertFromUnicodeToScriptCodeRun` toconvert the string. You can call this function repeatedly to properlytruncate a text segment, each time identifying the new beginningof the string, until the last portion of the text is less than orequal to the maximum allowable length. Each time you use the function,you get a properly terminated string within the allowable lengthrange. 

Because this function does not modify the contents of theUnicode converter object, you can call this function between conversioncalls.  

## Parameters

- `iUnicodeToTextInfo`: A Unicode converter object [`UnicodeToTextInfo`](./unicodetotextinfo.md) for the Unicode string to be divided up. The `TruncateForUnicodeToText` function does not modify the contents of this private structure. 
- `iSourceLen`: The length in bytes of the Unicode string to be divided up. 
- `iSourceStr`: A pointer to the Unicode string to be divided up. 
- `iControlFlags`: Truncation control flags. Specify the flag `kUnicodeStringUnterminatedMask` if truncating a buffer of text that belongs to a longer stream containing a subsequent buffer of text that could have characters belonging to a text element that begins at the end of the current buffer.  If you set this flag, typically you would set the `iMaxLen` parameter equal to `iSourceLen`. 
- `iMaxLen`: The maximum allowable length of the string to be truncated. This must be less than or equal to `iSourceLen`.
- `oTruncatedLen`: A pointer to a value of type `ByteCount`. On return, this value contains the length of the longest portion of the Unicode source string, pointed to by the `iSourceStr` parameter, that is less than or equal to the value of the `iMaxLen` parameter. This returned parameter identifies the byte after which you can truncate the string.

## See Also

### Truncating Strings Before Converting Them 
- [TruncateForTextToUnicode](./api-1433518-truncatefortexttounicode.md)
  Identifies where your application can safely break a multibytestring to be converted to Unicode so that the string is not brokenin the middle of a multibyte character. 


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1433649-truncateforunicodetotext)*