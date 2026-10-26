# GetTextEncodingName

**Framework**: Core Services  
**Kind**: func  
**Role**: Function

Returns the localized name for a specified text encoding. 

**Availability**:
- macOS 10.0+

## Declaration

```c
OSStatus GetTextEncodingName(TextEncoding iEncoding, TextEncodingNameSelector iNamePartSelector, RegionCode iPreferredRegion, TextEncoding iPreferredEncoding, ByteCount iOutputBufLen, ByteCount *oNameLength, RegionCode *oActualRegion, TextEncoding *oActualEncoding, TextPtr oEncodingName);
```

#### Return Value

A resultcode. See [Result Codes](./carbon_core/text_encoding_conversion_manager.md#1664324).

#### Discussion

Names returned by `GetTextEncodingName ` (in the buffer referred to by `oEncodingName`)can contain parentheses and other menu item meta characters, andso cannot be used with `AppendMenu` or `InsertMenuItem`.You can use them with `SetMenuItemText`.

This function can return resources and memory errors, andthe following result codes:

- `kTextUnsupportedEncodingErr`,which indicates that the encoding whose name you want to obtainis not supported. 
- `kTECMissingTableErr`,which indicates the name resource associated with the encoding ismissing.  
- `kTECTableFormatErr` or `kTECTableCheckSumErr`,which indicates that the name resource associated with that encodingis invalid.  

## Parameters

- `iEncoding`: A text encoding specification whose name you want to obtain. 
- `iNamePartSelector`: The portion of the encoding name you want to obtain. See [`TextEncodingNameSelector`](./textencodingnameselector.md) for a list of possible values. 
- `iPreferredRegion`: The preferred region to use for the name. You can specify a Mac OS region code (which also implies a language)for this parameter. If the function cannot return the name for the preferred region, it returns the name using a region code with the same language or in a default language (for example, English). 
- `iPreferredEncoding`: The preferred encoding to use for the name. For example, ASCII, Mac OS Roman, or Shift-JIS. If the function cannot return the name using the preferred encoding, it returns the name using another encoding, such as Unicode or ASCII.
- `iOutputBufLen`: The length in bytes of the output buffer that your application provides for the returned encoding name. 
- `oNameLength`: A pointer to a value of type `ByteCount`. On return, this parameter holds the actual length, in bytes, of the text encoding name. The value represents the full length of the name, which might be greater than the size of the output buffer, specified by the `iOutputBufLen` parameter. The length of the portion of the name actually contained in the output buffer is the smaller of `oNameLength` and `iOutputBufLen`.
- `oActualRegion`: A pointer to a value of type `RegionCode`. On return, this parameter holds the actual region associated with the returned encoding name.
- `oActualEncoding`: A pointer to a value of type `TextEncoding`. On return, this parameter holds the actual encoding associated with the returned encoding name.
- `oEncodingName`:  A pointer to a buffer you provide. On return, this parameter holds the text encoding name. 

## See Also

### Obtaining Information From a Text Encoding Specification
- [GetTextEncodingBase](./api-1399792-gettextencodingbase.md)
  Returns the base encoding of the specified text encoding. 
- [GetTextEncodingFormat](./api-1400318-gettextencodingformat.md)
  Returns the format value of the specified text encoding. 
- [GetTextEncodingVariant](./api-1400250-gettextencodingvariant.md)
  Returns the variant from the specified text encoding. 
- [ResolveDefaultTextEncoding](./api-1400111-resolvedefaulttextencoding.md)
  Returns a text encoding specification in which any meta-valueshave been resolved to real values. Currently, this affects onlythe base encoding values packed into the text encoding specification. 


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1399645-gettextencodingname)*