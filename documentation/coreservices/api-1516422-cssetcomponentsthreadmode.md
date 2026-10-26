# CSSetComponentsThreadMode

**Framework**: Core Services  
**Kind**: func  
**Role**: Function

Sets whether or not using thread-unsafe components is allowed in the current thread. 

**Availability**:
- macOS 10.3+ - Deprecated in 10.8

## Declaration

```c
void CSSetComponentsThreadMode(CSComponentsThreadMode mode);
```

#### Discussion

Core Services maintains a component thread-mode flag for each thread in the current process. The default value of this flag is `kCSAcceptAllComponentsMode`, which means the thread can call any component regardless of whether the component is thread-safe. Applications and other high-level code that call component-based APIs (such as QuickTime) from preemptive threads should call this function from their thread beforehand and pass in the value `kCSAcceptThreadSafeComponentsOnlyMode`. 

A thread’s component thread-mode flag can safely retain its default value only if the thread is the main thread or if it participates in cooperative locking, such as Carbon Thread Manager-style cooperative threads and application threads that perform their own private locking.

## Parameters

- `mode`: A flag that determines whether the current thread is restricted to calling components that are thread-safe. You should set this flag to `kCSAcceptThreadSafeComponentsOnlyMode` whenever you want the current thread to call only components that are thread-safe. 

## See Also

### Accessing the Thread Safety Mode
- [CSGetComponentsThreadMode](./api-1516409-csgetcomponentsthreadmode.md)
  Indicates whether using thread-unsafe components is allowed in the current thread. 


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1516422-cssetcomponentsthreadmode)*