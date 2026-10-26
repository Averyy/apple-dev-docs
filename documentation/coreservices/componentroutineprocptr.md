# ComponentRoutineProcPtr

**Framework**: Core Services  
**Kind**: tdef  
**Role**: Type Alias

Defines a pointer to your component callback function, which serves as the main entry point into your component and performs the component’s services. 

**Availability**:
- Mac Catalyst 17.0+
- macOS 10.0+

## Declaration

```c
typedef ComponentResult (*ComponentRoutineProcPtr)(ComponentParameters *cp, Handle componentStorage);
```

#### Return Value

Your component should return a value of type `ComponentResult`. If your component does not return error information as its function result, it should indicate errors using the [`SetComponentInstanceError`](./api-1516663-setcomponentinstanceerror.md) function. See the description of the `ComponentResult` data type.

#### Discussion

You pass a pointer to your component callback function to the Component Manager when you register your component. The Component Manager can then call your component when another application or component requests its services. When your component receives a request, it should perform the action specified in the `what` field of the component parameters structure.

The pointer which you pass to the Component Manager should be a universal procedure pointer (UPP). The definition of the UPP data type for your component function is as follows:

```occ
typedef (ComponentRoutineProcPtr) ComponentRoutineUPP;
```

Before using your component function, you must first create a UPP for your callback function, using the  [`NewComponentRoutineUPP`](./api-1516579-newcomponentroutineupp.md)  function, as shown here:

```occ
ComponentRoutineUPP MyComponentRoutineUPP;
MyComponentRoutineUPP =             NewComponentRoutineUPP(&MyComponentRoutineProc)
```

You then pass `MyComponentRoutineUPP` to the Component Manager when you register your component. The Component Manager will call your function each time your component receives a request. If you wish to call your component function yourself, you can use the  [`InvokeComponentRoutineUPP`](./api-1516654-invokecomponentroutineupp.md)  function.

```occ
result = InvokeComponentRoutineUPP &myParams, myStorage,              MyComponentRoutineUPP)
```

When you are finished with your component callback function, you should dispose of the universal procedure pointer associated with it, using the  [`DisposeComponentRoutineUPP`](./api-1516334-disposecomponentroutineupp.md)  function.

```occ
DisposeComponentRoutineUPP(MyComponentRoutineUPP);
```

To provide a component, you define a component function and supply the appropriate registration information. You store your component function in a code resource and typically store your component’s registration information as resources in a component file.  

## Parameters

- `cp`: A [`ComponentParameters`](./componentparameters.md) structure. The `what` field of the component parameters structure indicates the action your component should perform. The parameters that the client invoked your function with are contained in the `params` field of the component parameters structure. Your component can use the [`CallComponentFunction`](./api-1516603-callcomponentfunction.md) or [`CallComponentFunctionWithStorage`](./api-1516610-callcomponentfunctionwithstorage.md) function to extract the parameters from this structure. 
- `componentStorage`: A handle to any memory that your component has associated with the connection. Typically, upon receiving an open request, your component allocates memory and uses the [`SetComponentInstanceStorage`](./api-1516556-setcomponentinstancestorage.md) function to associate the allocated memory with the component connection. 

## See Also

### Callbacks
- [ComponentMPWorkFunctionProcPtr](./componentmpworkfunctionprocptr.md)
- [GetMissingComponentResourceProcPtr](./getmissingcomponentresourceprocptr.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/componentroutineprocptr)*