# WSProtocolHandlerCopyReplyDictionary

**Framework**: Core Services  
**Kind**: func  
**Role**: Function

Parses an incoming XML document as if it were the reply of a method.

**Availability**:
- macOS 10.3+ - Deprecated in 10.8

## Declaration

```c
CFDictionaryRef WSProtocolHandlerCopyReplyDictionary(WSProtocolHandlerRef ref, CFStringRef methodName, CFDataRef data);
```

#### Return Value

A `CFDictionary`, as returned by `WSMethodInvocationInvoke`.

#### Discussion

Parse an incoming XML document as if it were the reply of a method.  The results are the same as the `WSMethodInvocationInvoke` response;  the reply could be a fault.  If there was a parse error, `NULL` is returned.  Protocol specific additions, such as `kWSSOAPMessageHeaders`, may also be present in the dictionary.  The caller must release the resulting dictionary.

## Parameters

- `ref`: A `WSProtocolHandlerRef`, as created by `WSProtocolHandlerCreate`.
- `methodName`: The method name to treat the XML file as a result of.
- `data`: A `CFDataRef` of the XML document to parse


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1423441-wsprotocolhandlercopyreplydictio)*