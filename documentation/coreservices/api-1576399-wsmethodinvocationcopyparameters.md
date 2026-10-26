# WSMethodInvocationCopyParameters

**Framework**: Core Services  
**Kind**: func  
**Role**: Function

Creates a copy of the parameters dictionary and sets the order in an array.

**Availability**:
- macOS 10.2+ - Deprecated in 10.8

## Declaration

```c
CFDictionaryRef WSMethodInvocationCopyParameters(WSMethodInvocationRef invocation, CFArrayRef *parameterOrder);
```

#### Return Value

a `CFDictionaryRef`

#### Discussion

Copies the parameters from the invocation. The resulting dictionary contains the parameter dictionary. The `parameterOrder` output parameter, if not `NULL`, will contain the order used to serialize the parameters.

## Parameters

- `invocation`: the invocation
- `parameterOrder`: a pointer to a `CFArray` which will will receive the names, in their specified order, of the input parameter values.  This parameter may be `NULL`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1576399-wsmethodinvocationcopyparameters)*