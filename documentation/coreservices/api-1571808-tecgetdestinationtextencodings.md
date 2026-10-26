# TECGetDestinationTextEncodings

**Framework**: Core Services  
**Kind**: func  
**Role**: Function

Returns the encoding specifications for all the destinationtext encodings to which the Text Encoding Converter can directlyconvert the specified source encoding.

**Availability**:
- macOS 10.0+

## Declaration

```c
OSStatus TECGetDestinationTextEncodings(TextEncoding inputEncoding, TextEncoding destinationEncodings[], ItemCount maxDestinationEncodings, ItemCount *actualDestinationEncodings);
```

#### Return Value

A resultcode. See [Result Codes](./carbon_core/text_encoding_conversion_manager.md#1664324).

#### Discussion

This function ignores duplicate direct text encoding specifications.If you used the  [`TECCountDestinationTextEncodings`](./api-1571805-teccountdestinationtextencodings.md) function to determine the size of the `destinationEncodings[]` array,the number of available encodings may be fewer than the number ofarray elements, because `TECCountDestinationTextEncodings` includesduplicates in its count.

You can display the names of these destination encodings tothe user. 

## Parameters

- `inputEncoding`: The text encoding specification describing the source text. 
- `destinationEncodings`: On return, an array of specifications for the destination encodings to which the converter can directly convert the source encoding. You should use the [`TECCountDestinationTextEncodings`](./api-1571805-teccountdestinationtextencodings.md) function to determine how large an array to allocate.
- `maxDestinationEncodings`: The maximum number of destination text encodings that the array can contain. 
- `actualDestinationEncodings`: On return, a pointer to the number of text encoding specifications in the destination encodings array.

## See Also

### Identifying Possible Destination Encodings
- [TECCountDestinationTextEncodings](./api-1571805-teccountdestinationtextencodings.md)
  Counts and returns the number of destination encodingsto which a specified source encoding can be converted in one step.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1571808-tecgetdestinationtextencodings)*