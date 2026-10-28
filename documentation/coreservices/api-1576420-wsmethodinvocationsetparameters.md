# WSMethodInvocationSetParameters

**Framework**: Core Services  
**Kind**: func  
**Role**: Function

Set the parameter names, types, and order for a method invocation.

**Availability**:
- macOS 10.2+ - Deprecated in 10.8

## Declaration

```c
void WSMethodInvocationSetParameters(WSMethodInvocationRef invocation, CFDictionaryRef parameters, CFArrayRef parameterOrder);
```

## Discussion

Sets the parameters for a method invocation. The parameters dictionary should contain the names and types of the parameters. The parameter order array should contain the names of the parameters in the order they should be passed. The `parameterOrder` may be `NULL`, in which case the order of the parameters is undefined.  If the parameters dictionary contains more or fewer parameters than are specified by the order, the behavior is undefined.

## Parameters

- `invocation`: The invocation reference.
- `parameters`: A `CFDictionaryRef` of `CFString` keys and `CFTypeRef` values.
- `parameterOrder`: A `CFArrayRef` of `CFString` parameter names in order for XML-RPC.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1576420-wsmethodinvocationsetparameters)*