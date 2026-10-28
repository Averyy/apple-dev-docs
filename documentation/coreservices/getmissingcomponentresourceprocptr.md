# GetMissingComponentResourceProcPtr

**Framework**: Core Services  
**Kind**: tdef  
**Role**: Type Alias

**Availability**:
- Mac Catalyst 17.0+
- macOS 10.0+

## Declaration

```c
typedef OSErr (*GetMissingComponentResourceProcPtr)(Component c, OSType resType, SInt16 resID, void *refCon, Handle *resource);
```

## Return Value

A result code. See [Result Codes](./carbon_core/component_manager.md#1668759).

## Parameters

- `c`: 
- `resType`: 
- `resource`: 

## See Also

### Callbacks
- [ComponentMPWorkFunctionProcPtr](./componentmpworkfunctionprocptr.md)
- [ComponentRoutineProcPtr](./componentroutineprocptr.md)
  Defines a pointer to your component callback function, which serves as the main entry point into your component and performs the component’s services. 


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/getmissingcomponentresourceprocptr)*