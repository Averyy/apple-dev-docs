# WSProtocolHandlerSetDeserializationOverride

**Framework**: Core Services  
**Kind**: func  
**Role**: Function

Specifies a callback to be made when parsing an XML method response.

**Availability**:
- macOS 10.3+ - Deprecated in 10.8

## Declaration

```c
void WSProtocolHandlerSetDeserializationOverride(WSProtocolHandlerRef protocol, CFStringRef typeNamespace, CFStringRef typeName, WSProtocolHandlerDeserializationProcPtr deserializationProc, WSClientContext *context);
```

#### Discussion

This function specifies a callback to be made when parsing an XML method response. The callback is passed a reference to the protocol element currently being executed, the root of the response parse tree, the current node being deserialized, and a pointer to private data. The return result should be a valid `CFTypeRef` object, which will be released by the caller. If the callback returns `NULL`, the default deserializer will be used.

## Parameters

- `protocol`: The `ProtocolHandlerRef`.
- `typeNamespace`: The fully resolved namespace for a specific type. If `NULL`, the default namespace will be used. For example, this field could be: `CFSTR("http://www.w3.org/2001/XMLSchema-instance")`.
- `typeName`: The non-qualified type name. This parameter must not be `NULL`.
- `deserializationProc`: A `ProcPtr` to be called to perform the deserialization.
- `context`: A pointer to a `WSClientContext`. The structure will be copied.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1423444-wsprotocolhandlersetdeserializat)*