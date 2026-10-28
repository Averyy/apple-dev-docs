# WSProtocolHandlerCopyRequestDocument

**Framework**: Core Services  
**Kind**: func  
**Role**: Function

Creates an XML request for a given `WSProtocolHandler` and parameter list.

**Availability**:
- macOS 10.3+ - Deprecated in 10.8

## Declaration

```c
CFDataRef WSProtocolHandlerCopyRequestDocument(WSProtocolHandlerRef ref, CFStringRef methodName, CFDictionaryRef methodParams, CFArrayRef methodParamOrder, CFDictionaryRef methodExtras);
```

## Return Value

A `CFDataRef`.

## Discussion

This function creates an XML request for a given `WSProtocolHandler` and parameter list. This is the request sent to a server.

## Parameters

- `ref`: The `WSProtocolHandlerRef`.
- `methodName`: A `CFString` of the method name to call.
- `methodParams`: A `CFDictionary` containing the parameters to send.
- `methodParamOrder`: A `CFArray`, which, if not `NULL`, specifies the order of the parameters in the `CFDictionary`.
- `methodExtras`: A `CFDictionary`, which, if not `NULL`, contains additional information for the protocol (for example, `kWSSoapMessageHeaders`).


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1423437-wsprotocolhandlercopyrequestdocu)*