# TextEncodingRun

**Framework**: Core Services  
**Kind**: struct  
**Role**: Structure

Contains text encoding information for a text run.

**Availability**:
- Mac Catalyst 17.0+
- macOS 10.0+

## Declaration

```c
typedef struct TextEncodingRun {
    ...
} TextEncodingRun;
```

## Overview

It is not always possible to convert text expressed in Unicode to another single encoding because no other single encoding encompasses the Unicode character encoding range. To adjust for this, you can create a Unicode mapping structure array that specifies the target encodings the Unicode text should be converted to when multiple encodings must be used. 

If the `kUnicodeTextRunMask` flag is set, [`ConvertFromUnicodeToTextRun`](./api-1433511-convertfromunicodetotextrun.md) and [`ConvertFromUnicodeToScriptCodeRun`](./api-1433662-convertfromunicodetoscriptcoderu.md) may convert Unicode text to a string of text containing multiple text encoding runs. Each run contains text expressed in a different encoding from that of the preceding or following text segment. For each text encoding run in the string, a `TextEncodingRun` structure indicates the beginning offset and the text encoding for that run. 

Functions that convert text from Unicode to a text run return the converted text in an array of text encoding run structures. A text encoding run structure is defined by the `TextEncodingRun` data type.  

## Topics

### Instance Properties
- [offset](./textencodingrun/api-1400422-offset.md)
  The beginning character position of a run of text in the converted text string.
- [textEncoding](./textencodingrun/api-1399800-textencoding.md)
  The encoding of the text run that begins at the position specified. 


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/textencodingrun)*