# WSClientContextReleaseCallBackProcPtr

**Framework**: Core Services  
**Kind**: tdef  
**Role**: Type Alias

This is the callback that releases the information.

**Availability**:
- macOS 10.2+

## Declaration

```c
typedef void (*WSClientContextReleaseCallBackProcPtr)(void *info);
```

#### Discussion

If your callback is named MyInfoReleaseCallback, declare it like this:

##### Discussion

Your callback is passed a  a pointer to private data for you to release.

## Parameters

- `info`: Private callback data to be released.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/wsclientcontextreleasecallbackprocptr)*