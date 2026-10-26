# WSProtocolHandlerCopyRequestDictionary

**Framework**: Core Services  
**Kind**: func  
**Role**: Function

Parses an incoming XML document for the method name and parameters.

**Availability**:
- macOS 10.3+ - Deprecated in 10.8

## Declaration

```c
CFDictionaryRef WSProtocolHandlerCopyRequestDictionary(WSProtocolHandlerRef ref, CFDataRef data);
```

#### Return Value

A `CFDictionary`.

#### Discussion

This function parses an incoming XML document for the method name and parameters. The results are in a dictionory as `kWSMethodName` (a `CFString`), `kWSMethodParameters` (a `CFDictionary`), and `kWSMethodParameterOrder` (a `CFArray`). If a parse error occurred, `NULL` is returned. Protocol specific additions (for example, `kWSSOAPMessageHeaders`) may also be present in the dictionary. The dictionary returned also represents the context with which XML reply documents are created (see `WSProtocolHandlerCreateReply`). The caller must release the resulting dictionary. Note that the returned dictionary should be used as an input parameter for other `WSProtocol` functions that require a context dictionary parameter.

## Parameters

- `ref`: The protocol handler to use.
- `data`: The XML document to parse.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1423451-wsprotocolhandlercopyrequestdict)*