# WSProtocolHandlerCreate

**Framework**: Core Services  
**Kind**: func  
**Role**: Function

Creates a `WSProtocolHandlerRef` for use in translating an XML document.

**Availability**:
- macOS 10.3+ - Deprecated in 10.8

## Declaration

```c
WSProtocolHandlerRef WSProtocolHandlerCreate(CFAllocatorRef allocator, CFStringRef protocol);
```

#### Return Value

A `WSProtocolHandlerRef`; `NULL` if a parse error occurred.

#### Discussion

This function creates a `WSProtocolHandlerRef` for use in translating an XML document. A protocol handler translates dictionaries into web services requests. It is created with a string specifying the protocol (XML-RPC or SOAP) and can be modified by setting various properties. It should be noted that the parser can be re-used for multiple parses.

## Parameters

- `allocator`: A `CFAllocatorRef` used to allocate the protocol handler.
- `protocol`: A constant string, defined in `WSMethodInvocation.h`, that determines the type of implementation to create (XML-RPC vs. SOAP).


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1423434-wsprotocolhandlercreate)*