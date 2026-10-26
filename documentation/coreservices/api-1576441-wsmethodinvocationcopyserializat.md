# WSMethodInvocationCopySerialization

**Framework**: Core Services  
**Kind**: func  
**Role**: Function

Creates an XML serialization of a method invocation.

**Availability**:
- macOS 10.2+ - Deprecated in 10.8

## Declaration

```c
CFDataRef WSMethodInvocationCopySerialization(WSMethodInvocationRef invocation);
```

#### Return Value

A `CFDataRef` of the serialized XML method invocation.

#### Discussion

Creates a serialized version of the method invocation which can be used at a later time.

## Parameters

- `invocation`: The invocation to serialize.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1576441-wsmethodinvocationcopyserializat)*