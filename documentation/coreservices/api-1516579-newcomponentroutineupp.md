# NewComponentRoutineUPP

**Framework**: Core Services  
**Kind**: func  
**Role**: Function

Creates a new universal procedure pointer (UPP) to a component routine callback function.

**Availability**:
- macOS 10.0+ - Deprecated in 10.8

## Declaration

```c
ComponentRoutineUPP NewComponentRoutineUPP(ComponentRoutineProcPtr userRoutine);
```

#### Return Value

See the description of the `ComponentRoutineUPP` data type.

#### Discussion

See the  [`ComponentRoutineProcPtr`](./componentroutineprocptr.md)  callback for more information. 

## Parameters

- `userRoutine`: 

## See Also

### Creating and Managing Universal Procedure Pointers
- [InvokeComponentRoutineUPP](./api-1516654-invokecomponentroutineupp.md)
  Calls your component routine callback function
- [DisposeComponentRoutineUPP](./api-1516334-disposecomponentroutineupp.md)
  Disposes of the universal procedure pointer (UPP) to a component routine callback function.
- [NewComponentFunctionUPP](./api-1516583-newcomponentfunctionupp.md)
- [DisposeComponentFunctionUPP](./api-1516369-disposecomponentfunctionupp.md)
- [NewComponentMPWorkFunctionUPP](./api-1516448-newcomponentmpworkfunctionupp.md)
- [InvokeComponentMPWorkFunctionUPP](./api-1516356-invokecomponentmpworkfunctionupp.md)
- [DisposeComponentMPWorkFunctionUPP](./api-1516328-disposecomponentmpworkfunctionup.md)
- [NewGetMissingComponentResourceUPP](./api-1516619-newgetmissingcomponentresourceup.md)
- [InvokeGetMissingComponentResourceUPP](./api-1516491-invokegetmissingcomponentresourc.md)
- [DisposeGetMissingComponentResourceUPP](./api-1516414-disposegetmissingcomponentresour.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1516579-newcomponentroutineupp)*