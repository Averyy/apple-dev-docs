# CreateTextEncoding

**Framework**: Core Services  
**Kind**: func  
**Role**: Function

Creates and returns a text encoding specification.

**Availability**:
- macOS 10.0+

## Declaration

```c
TextEncoding CreateTextEncoding(TextEncodingBase encodingBase, TextEncodingVariant encodingVariant, TextEncodingFormat encodingFormat);
```

## Return Value

The text encodingspecification that the function creates from the values you passit.

## Discussion

When you create a text encoding specification, the three valuesthat you specify are packed into an unsigned integer, which youcan then pass by value to the functions that use text encodings.See the data type  [`TextEncodingRun`](./textencodingrun.md). 

## Parameters

- `encodingBase`: A base text encoding.
- `encodingVariant`: A variant of the base text encoding. To specify the default variant for the base encoding given in the `encodingBase` parameter, you can use the `kTextEncodingDefaultVariant` constant. 
- `encodingFormat`: A format for the base text encoding. To specify the default format for the base encoding, you can use the `kTextEncodingDefaultFormat` constant. If you want to obtain a  `TextEncoding` value that references  UTF-16 or UTF-8, pass `kUnicode16BitFormat` or `kUnicodeUTF8Format` . 


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1399639-createtextencoding)*