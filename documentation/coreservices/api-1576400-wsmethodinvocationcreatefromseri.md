# WSMethodInvocationCreateFromSerialization

**Framework**: Core Services  
**Kind**: func  
**Role**: Function

Creates a method invocation object from an XML serialization.

**Availability**:
- macOS 10.2+ - Deprecated in 10.8

## Declaration

```c
WSMethodInvocationRef WSMethodInvocationCreateFromSerialization(CFDataRef contract);
```

## Return Value

A `WSMethodInvocationRef` object that can be passed to `WSMethodInvocationInvoke` or scheduled with a run loop.

## Discussion

Creates a web services method invocation object from a previously serialized contract. You can use this with a serialization returned from `WSMethodInvocationCopySerialization`.

## Parameters

- `contract`: The result of a previously serialized `WSMethodInvocationRef`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1576400-wsmethodinvocationcreatefromseri)*