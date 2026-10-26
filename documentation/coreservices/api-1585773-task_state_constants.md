# Task State Constants

**Framework**: Core Services  
**Kind**: enum  
**Role**: Enumeration

Specify what states you want to set or obtain when calling the `MPExtractTaskState` or `MPSetTaskState` functions. 

**Availability**:
- Mac Catalyst 13.1+ - Deprecated in 13.1
- macOS 10.0+ - Deprecated in 10.7

## Declaration

```c
enum : unsigned int {
    ...
};
```

## Topics

### Constants
- [kMPTaskStateRegisters](./api-1585773-task_state_constants/kmptaskstateregisters.md)
  The task’s general-purpose (GP) registers. The `RegisterInformationPowerPC` structure in `MachineExceptions.h` defines the format of this information. 
- [kMPTaskStateFPU](./api-1585773-task_state_constants/kmptaskstatefpu.md)
  The task’s floating point registers. The `FPUInformationPowerPC` structure in `MachineExceptions.h` defines the format of this information.
- [kMPTaskStateVectors](./api-1585773-task_state_constants/kmptaskstatevectors.md)
  The task’s vector registers. The `VectorInformationPowerPC` structure in `MachineExceptions.h` defines the format of this information.
- [kMPTaskStateMachine](./api-1585773-task_state_constants/kmptaskstatemachine.md)
  The task’s machine registers. The `MachineInformationPowerPC` structure in `MachineExceptions.h` defines the format of this information. Note that the MSR, ExceptKind, DSISR, and DAR registers are read-only. 
- [kMPTaskState32BitMemoryException](./api-1585773-task_state_constants/kmptaskstate32bitmemoryexception.md)
- [kMPTaskStateTaskInfo](./api-1585773-task_state_constants/kmptaskstatetaskinfo.md)
  Static and dynamic information about the task, as described by the data structure [`MPTaskInfo`](./mptaskinfo.md). This task information is read-only. 


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1585773-task_state_constants)*