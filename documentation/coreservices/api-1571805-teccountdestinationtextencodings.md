# TECCountDestinationTextEncodings

**Framework**: Core Services  
**Kind**: func  
**Role**: Function

Counts and returns the number of destination encodingsto which a specified source encoding can be converted in one step.

**Availability**:
- macOS 10.0+

## Declaration

```c
OSStatus TECCountDestinationTextEncodings(TextEncoding inputEncoding, ItemCount *numberOfEncodings);
```

## Return Value

A resultcode. See [Result Codes](./carbon_core/text_encoding_conversion_manager.md#1664324).

## Discussion

This function counts every instance of an encoding. If differentconversion plug-ins support the same direct text encoding, the directtext encoding is counted more than once.

Since the `TECGetDestinationTextEncodings` functionignores duplicate text encoding specifications, `TECCountDestinationTextEncodings` mayreturn a number greater than the number of array elements neededfor the `destinationEncodings[]` parameter. 

## Parameters

- `inputEncoding`: The text encoding specification describing the source text. 
- `numberOfEncodings`: On return, a pointer to the number of text encodings to which the source encoding can be converted in one step. You should use this to determine how large to make the array you pass to the [`TECGetDestinationTextEncodings`](./api-1571808-tecgetdestinationtextencodings.md) function. 

## See Also

### Identifying Possible Destination Encodings
- [TECGetDestinationTextEncodings](./api-1571808-tecgetdestinationtextencodings.md)
  Returns the encoding specifications for all the destinationtext encodings to which the Text Encoding Converter can directlyconvert the specified source encoding.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1571805-teccountdestinationtextencodings)*