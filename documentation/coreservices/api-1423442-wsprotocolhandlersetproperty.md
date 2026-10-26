# WSProtocolHandlerSetProperty

**Framework**: Core Services  
**Kind**: func  
**Role**: Function

Sets a property in a specified protocol handler.

**Availability**:
- macOS 10.3+ - Deprecated in 10.8

## Declaration

```c
void WSProtocolHandlerSetProperty(WSProtocolHandlerRef ref, CFStringRef propertyName, CFTypeRef propertyValue);
```

#### Discussion

This function sets the value of a named property in a method implementation.

## Parameters

- `ref`: The protocol handler.
- `propertyName`: The name of the property to set.
- `propertyValue`: The value of the property to set.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1423442-wsprotocolhandlersetproperty)*