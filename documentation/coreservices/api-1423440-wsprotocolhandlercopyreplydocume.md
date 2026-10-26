# WSProtocolHandlerCopyReplyDocument

**Framework**: Core Services  
**Kind**: func  
**Role**: Function

Creates a Reply XML document for a given WS ProtocolHandler and context dictionary.

**Availability**:
- macOS 10.3+ - Deprecated in 10.8

## Declaration

```c
CFDataRef WSProtocolHandlerCopyReplyDocument(WSProtocolHandlerRef ref, CFDictionaryRef methodContext, CFTypeRef resultValue);
```

#### Return Value

A `CFDataRef` containing the XML response.

#### Discussion

This function creates a Reply XML document for a given `WSProtocolHandler` and context dictionary. Protocol specific addtions (for example, `kWSSOAPMessageHeaders`) may also be present in the dictionary.

## Parameters

- `ref`: The WSProtocolHandler to respond.
- `methodContext`: The `CFDictionary` containing the context for this method call, as returned by `WSProtocolHandlerParseRequest`.
- `resultValue`: A `CFTypeRef` representing the data to be serialized.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1423440-wsprotocolhandlercopyreplydocume)*