# DebugAssertOutputHandlerProcPtr

**Framework**: Core Services  
**Kind**: tdef  
**Role**: Type Alias

**Availability**:
- Mac Catalyst 17.0+
- macOS 10.0+

## Declaration

```c
typedef void (*DebugAssertOutputHandlerProcPtr)(OSType componentSignature, UInt32 options, const char *assertionString, const char *exceptionLabelString, const char *errorString, const char *fileName, long lineNumber, void *value, ConstStr255Param outputMsg);
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/debugassertoutputhandlerprocptr)*