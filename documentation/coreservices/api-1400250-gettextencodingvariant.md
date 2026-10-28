# GetTextEncodingVariant

**Framework**: Core Services  
**Kind**: func  
**Role**: Function

Returns the variant from the specified text encoding. 

**Availability**:
- macOS 10.0+

## Declaration

```c
TextEncodingVariant GetTextEncodingVariant(TextEncoding encoding);
```

## Return Value

The text encodingvariant portion of the specified text encoding. 

## Parameters

- `encoding`: A text encoding specification. 

## See Also

### Obtaining Information From a Text Encoding Specification
- [GetTextEncodingBase](./api-1399792-gettextencodingbase.md)
  Returns the base encoding of the specified text encoding. 
- [GetTextEncodingFormat](./api-1400318-gettextencodingformat.md)
  Returns the format value of the specified text encoding. 
- [GetTextEncodingName](./api-1399645-gettextencodingname.md)
  Returns the localized name for a specified text encoding. 
- [ResolveDefaultTextEncoding](./api-1400111-resolvedefaulttextencoding.md)
  Returns a text encoding specification in which any meta-valueshave been resolved to real values. Currently, this affects onlythe base encoding values packed into the text encoding specification. 


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1400250-gettextencodingvariant)*