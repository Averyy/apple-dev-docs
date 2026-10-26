# WSMethodInvocationInvoke

**Framework**: Core Services  
**Kind**: func  
**Role**: Function

Invokes an web services operation synchronously.

**Availability**:
- macOS 10.2+ - Deprecated in 10.8

## Declaration

```c
CFDictionaryRef WSMethodInvocationInvoke(WSMethodInvocationRef invocation);
```

#### Return Value

a `CFDictionaryRef` containing the result of the execution or a fault, and optional debug information.

#### Discussion

Executes the invocation synchronously. If the call was successful, the result contains the result of the invocation. If the invocation failed for any reason, including out of memory or invalid parameter errors, then the result contains a fault structure. You must release the result when you are done with it. To execute the invocation asynchronously (recommended), use WSMethodInvocationScheduleWithRunLoop.

## Parameters

- `invocation`: The method invocation reference.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1576428-wsmethodinvocationinvoke)*