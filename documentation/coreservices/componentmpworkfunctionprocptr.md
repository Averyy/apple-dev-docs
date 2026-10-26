# ComponentMPWorkFunctionProcPtr

**Framework**: Core Services  
**Kind**: tdef  
**Role**: Type Alias

**Availability**:
- Mac Catalyst 17.0+
- macOS 10.0+

## Declaration

```c
typedef ComponentResult (*ComponentMPWorkFunctionProcPtr)(void *globalRefCon, ComponentMPWorkFunctionHeaderRecordPtr header);
```

#### Return Value

See the description of the `ComponentResult` data type.

## Parameters

- `header`: 

## See Also

### Callbacks
- [ComponentRoutineProcPtr](./componentroutineprocptr.md)
  Defines a pointer to your component callback function, which serves as the main entry point into your component and performs the component’s services. 
- [GetMissingComponentResourceProcPtr](./getmissingcomponentresourceprocptr.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/componentmpworkfunctionprocptr)*