# WSClientContextRetainCallBackProcPtr

**Framework**: Core Services  
**Kind**: tdef  
**Role**: Type Alias

This is the callback that retains the information.

**Availability**:
- macOS 10.2+

## Declaration

```c
typedef void *(*WSClientContextRetainCallBackProcPtr)(void *info);
```

#### Discussion

If your callback is named MyInfoRetainCallback, declare it like this:

##### Discussion

Your callback is passed a  a pointer to private data for you to retain.

## Parameters

- `info`: Private callback data to be retained.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/wsclientcontextretaincallbackprocptr)*