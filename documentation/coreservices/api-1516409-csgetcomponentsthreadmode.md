# CSGetComponentsThreadMode

**Framework**: Core Services  
**Kind**: func  
**Role**: Function

Indicates whether using thread-unsafe components is allowed in the current thread. 

**Availability**:
- macOS 10.3+ - Deprecated in 10.8

## Declaration

```c
CSComponentsThreadMode CSGetComponentsThreadMode(void);
```

#### Return Value

A flag that indicates whether using thread-unsafe components is allowed in the current thread. 

## See Also

### Accessing the Thread Safety Mode
- [CSSetComponentsThreadMode](./api-1516422-cssetcomponentsthreadmode.md)
  Sets whether or not using thread-unsafe components is allowed in the current thread. 


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1516409-csgetcomponentsthreadmode)*