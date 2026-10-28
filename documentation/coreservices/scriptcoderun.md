# ScriptCodeRun

**Framework**: Core Services  
**Kind**: struct  
**Role**: Structure

Contains script code information for a text run.

**Availability**:
- Mac Catalyst 17.0+
- macOS 10.0+

## Declaration

```c
typedef struct ScriptCodeRun {
    ...
} ScriptCodeRun;
```

## Overview

To return the result of a multiple encoding conversion, the [`ConvertFromUnicodeToScriptCodeRun`](./api-1433662-convertfromunicodetoscriptcoderu.md) function uses a script code run structure. 

The script code run structure uses an extended script code with values in the range 0–254, which are the text encoding base equivalents to Mac OS encodings. Values 0–32 correspond directly to traditional script codes. This allows a script code run to distinguish Icelandic, Turkish, Symbol, Zapf Dingbats, and so on. 

## Topics

### Instance Properties
- [offset](./scriptcoderun/api-1400334-offset.md)
  The beginning character position of a text run and its script code in the converted text.
- [script](./scriptcoderun/api-1400081-script.md)
  The script code for the text that begins at the position specified.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/scriptcoderun)*