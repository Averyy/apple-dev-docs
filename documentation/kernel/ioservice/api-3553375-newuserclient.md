# newUserClient

**Framework**: Kernel  
**Kind**: instm  
**Role**: Instance Method

**Availability**:
- macOS 11.0+

## Declaration

```c
IOReturn newUserClient(task_t owningTask, void *securityID, UInt32 type, OSSharedPtr<IOUserClient> & handler);
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/ioservice/3553375-newuserclient)*