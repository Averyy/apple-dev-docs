# WSMethodResultIsFault

**Framework**: Core Services  
**Kind**: func  
**Role**: Function

Tests a method result dictionary for a fault condition.

**Availability**:
- macOS 10.2+ - Deprecated in 10.8

## Declaration

```c
Boolean WSMethodResultIsFault(CFDictionaryRef methodResult);
```

## Return Value

A boolean TRUE if the result contains a fault condition.

## Discussion

If the result is a fault, look in the `kWSFaultCode`, `kWSFaultString`, and `kWSFaultExtra` fields of the dictionary.  If not a  fault, `kWSMethodInvocationResult` will contain the result of the execution. If debugging information was requested, it will be available in the dictionary as well.

## Parameters

- `methodResult`: A method result dictionary.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1576401-wsmethodresultisfault)*