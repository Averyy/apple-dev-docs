# WSProtocolHandlerCopyProperty

**Framework**: Core Services  
**Kind**: func  
**Role**: Function

Returns a copy of a property from a protocol handler reference.

**Availability**:
- macOS 10.3+ - Deprecated in 10.8

## Declaration

```c
CFTypeRef WSProtocolHandlerCopyProperty(WSProtocolHandlerRef ref, CFStringRef propertyName);
```

## Return Value

The `CFTypeRef` value of the property, or `NULL` if the specified property does not exist.

## Discussion

Returns a property from a protocol handler.  If the result is `NULL`, the property doesn't exist.  Since this is a Copy call, you must release the result.

## Parameters

- `ref`: A `WSProtocolHandlerRef`, as created by `WSProtocolHandlerCreate`.
- `propertyName`: The name of the property to copy.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1423436-wsprotocolhandlercopyproperty)*