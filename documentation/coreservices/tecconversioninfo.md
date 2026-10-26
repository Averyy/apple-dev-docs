# TECConversionInfo

**Framework**: Core Services  
**Kind**: struct  
**Role**: Structure

Contains text encoding conversion information.

**Availability**:
- Mac Catalyst 17.0+
- macOS 10.0+

## Declaration

```c
typedef struct TECConversionInfo {
    ...
} TECConversionInfo;
```

#### Overview

When you call the function [`TECGetDirectTextEncodingConversions`](./api-1571834-tecgetdirecttextencodingconversi.md), you pass an array of text encoding conversion information structures. The function fills these structures with information about each type of supported conversion. 

## Topics

### Instance Properties
- [destinationEncoding](./tecconversioninfo/api-1571800-destinationencoding.md)
  The text encoding specification for the destination text.
- [reserved1](./tecconversioninfo/api-1571813-reserved1.md)
  Reserved.
- [reserved2](./tecconversioninfo/api-1571797-reserved2.md)
  Reserved.
- [sourceEncoding](./tecconversioninfo/api-1571810-sourceencoding.md)
  The text encoding specification for the source text. 


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/tecconversioninfo)*