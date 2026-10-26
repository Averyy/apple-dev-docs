# kWSFaultString

**Framework**: Core Services  
**Kind**: data  
**Role**: Global Variable

If the result is a fault, this key returns a CFString with the fault type. If the fault type is `kWSNetworkStreamFaultString`, then the fault is a network error. In the case of a network error, `kWSFaultCode` should be ignored, and `kWSFaultExtra` returns a dictionary indicating the network error.

**Availability**:
- macOS 10.2+ - Deprecated in 10.8

## Declaration

```c
CFStringRef kWSFaultString;
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/kwsfaultstring)*