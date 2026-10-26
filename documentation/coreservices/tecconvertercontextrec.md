# TECConverterContextRec

**Framework**: Core Services  
**Kind**: struct  
**Role**: Structure

Contains converter information used by a Text Encoding Converter plug-in.

**Availability**:
- Mac Catalyst 17.0+
- macOS 10.0+

## Declaration

```c
typedef struct TECConverterContextRec {
    ...
} TECConverterContextRec;
```

## Topics

### Instance Properties
- [bufferContext](./tecconvertercontextrec/api-1498350-buffercontext.md)
- [clearContextInfoProc](./tecconvertercontextrec/api-1498585-clearcontextinfoproc.md)
  A pointer to a callback for our clear procedure.
- [contextRefCon](./tecconvertercontextrec/api-1498533-contextrefcon.md)
  A 32-bit value containing or referring to plug-in-specific data.
- [conversionProc](./tecconvertercontextrec/api-1498409-conversionproc.md)
  A pointer to a callback for your conversion procedure.
- [destEncoding](./tecconvertercontextrec/api-1498400-destencoding.md)
  The text encoding specification for the destination text. 
- [flushProc](./tecconvertercontextrec/api-1498586-flushproc.md)
  A pointer to a callback for your reset procedure.
- [options1](./tecconvertercontextrec/api-1498561-options1.md)
  A 32-bit value that specfies options needed by your plug-in.
- [options2](./tecconvertercontextrec/api-1498421-options2.md)
  A 32-bit value that specfies options needed by your plug-in.
- [pluginRec](./tecconvertercontextrec/api-1498573-pluginrec.md)
- [pluginState](./tecconvertercontextrec/api-1498418-pluginstate.md)
- [reserved1](./tecconvertercontextrec/api-1498424-reserved1.md)
  Reserved.
- [reserved2](./tecconvertercontextrec/api-1498448-reserved2.md)
  Reserved.
- [sourceEncoding](./tecconvertercontextrec/api-1498368-sourceencoding.md)
  The text encoding specification for the source text. 


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/tecconvertercontextrec)*