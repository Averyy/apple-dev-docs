# WSClientContextCopyDescriptionCallBackProcPtr

**Framework**: Core Services  
**Kind**: tdef  
**Role**: Type Alias

This is the callback that copies the information.

**Availability**:
- macOS 10.2+

## Declaration

```c
typedef CFStringRef (*WSClientContextCopyDescriptionCallBackProcPtr)(void *info);
```

## Return Value

A CFStringRef containing the client context information.

## Discussion

If your callback is named MyInfoCopyCallback, declare it like this:

### Discussion

Your callback is passed a  a pointer to private data for you to copy.

## Parameters

- `info`: Private callback data to be coped.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/wsclientcontextcopydescriptioncallbackprocptr)*