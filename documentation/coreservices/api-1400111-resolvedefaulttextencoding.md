# ResolveDefaultTextEncoding

**Framework**: Core Services  
**Kind**: func  
**Role**: Function

Returns a text encoding specification in which any meta-valueshave been resolved to real values. Currently, this affects onlythe base encoding values packed into the text encoding specification. 

**Availability**:
- macOS 10.0+

## Declaration

```c
TextEncoding ResolveDefaultTextEncoding(TextEncoding encoding);
```

#### Return Value

A text encoding specificationcontaining only real base encoding values. 

#### Discussion

This function is useful for application developers who areproviding APIs that take text encoding specifications as parameters.All APIs in the Unicode Converter and Text Encoding Converter performthis translation automatically.  

## Parameters

- `encoding`: A text encoding specification possibly containing meta-values that you want to resolve to a text encoding specification containing only real values. 

## See Also

### Obtaining Information From a Text Encoding Specification
- [GetTextEncodingBase](./api-1399792-gettextencodingbase.md)
  Returns the base encoding of the specified text encoding. 
- [GetTextEncodingFormat](./api-1400318-gettextencodingformat.md)
  Returns the format value of the specified text encoding. 
- [GetTextEncodingName](./api-1399645-gettextencodingname.md)
  Returns the localized name for a specified text encoding. 
- [GetTextEncodingVariant](./api-1400250-gettextencodingvariant.md)
  Returns the variant from the specified text encoding. 


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1400111-resolvedefaulttextencoding)*