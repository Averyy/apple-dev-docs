# AsyncCompletion_Invoke

**Framework**: Kernel  
**Kind**: clm  
**Role**: Type Method

**Availability**:
- macOS 15.4+

## Declaration

```c
static kern_return_t AsyncCompletion_Invoke(const IORPC rpc, OSMetaClassBase *target, AsyncCompletion_Handler func, const OSMetaClass *targetActionClass);
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iouserclient/4520003-asynccompletion_invoke)*