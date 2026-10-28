# WSProtocolHandlerCopyFaultDocument

**Framework**: Core Services  
**Kind**: func  
**Role**: Function

Creates a Fault XML response for a given WSProtocolHandler and fault details dictionary.

**Availability**:
- macOS 10.3+ - Deprecated in 10.8

## Declaration

```c
CFDataRef WSProtocolHandlerCopyFaultDocument(WSProtocolHandlerRef ref, CFDictionaryRef methodContext, CFDictionaryRef faultDict);
```

## Return Value

A `CFDataRef` containing the XML fault.

## Discussion

This function creates a Fault XML response for a given `WSProtocolHandlerRef` and fault details dictionary. The fault dictionary contains one or more of `kWSFaultString`, `kWSFaultCode` or `kWSFaultExtra`, as per WSMethodInvocation.h.

## Parameters

- `ref`: A `WSProtocolHandlerRef`, as created by `WSProtocolHandlerCreate`.
- `methodContext`: The CFDictionary containing the context for this method call, as returned by `WSProtocolHandlerParseRequest`.
- `faultDict`: A `CFDictionary` containing the fault information. See `WSMethodInvocation.h` for valid keys.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1423449-wsprotocolhandlercopyfaultdocume)*