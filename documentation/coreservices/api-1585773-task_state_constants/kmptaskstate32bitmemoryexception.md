# kMPTaskState32BitMemoryException

**Framework**: Core Services  
**Kind**: econst  
**Role**: Enumeration Case

**Availability**:
- Mac Catalyst 13.1+ - Deprecated in 13.1
- macOS 10.0+ - Deprecated in 10.7

## Declaration

```c
kMPTaskState32BitMemoryException = 4
```

## Discussion

The task’s exception information for older 32-bit memory exceptions (that is, memory exceptions on 32-bit CPUs). The `MemoryExceptionInformation` structure in `MachineExceptions.h` defines the format of this information. This exception information is read-only. 


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1585773-task_state_constants/kmptaskstate32bitmemoryexception)*