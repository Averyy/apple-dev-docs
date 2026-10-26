# WSMethodInvocationCallBackProcPtr

**Framework**: Core Services  
**Kind**: tdef  
**Role**: Type Alias

This is the callback that handles method invocation completion when the method is invoked asynchronously.

**Availability**:
- macOS 10.2+ - Deprecated in 10.8

## Declaration

```c
typedef void (*WSMethodInvocationCallBackProcPtr)(WSMethodInvocationRef invocation, void *info, CFDictionaryRef outRef);
```

#### Discussion

If your callback is named MyCompletionCallback, declare it like this:

##### Discussion

Your callback is passed a reference to the invocation just completed, a pointer to private data, and a dictionary that contains the return value or falut for this invocation.  The  callback is responsible for releasing the dictionary when it is  no longer used.

## Parameters

- `invocation`: The method invocation for which this callback handles completion.
- `info`: Private callback data.
- `outRef`: A `CFDictionaryRef` containing the method invocation result or a fault structure, and optional debug information.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/wsmethodinvocationcallbackprocptr)*