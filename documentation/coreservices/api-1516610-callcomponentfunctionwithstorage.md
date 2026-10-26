# CallComponentFunctionWithStorage

**Framework**: Core Services  
**Kind**: func  
**Role**: Function

Invokes the specified function of your component. 

**Availability**:
- macOS 10.0+ - Deprecated in 10.8

## Declaration

```c
ComponentResult CallComponentFunctionWithStorage(Handle storage, ComponentParameters *params, ComponentFunctionUPP func);
```

#### Return Value

The value that is returned by the function referred to by the `func` parameter. Your component should use this value to set the current error for this connection. Use the [`SetComponentInstanceError`](./api-1516663-setcomponentinstanceerror.md) function to set the current error for a connection. 

#### Discussion

When an application requests service from your component, your component receives a component parameters structure containing the parameters that the application provided when it called your component. Your component can use this structure to access the parameters directly. Alternatively, you can use either the  [`CallComponentFunction`](./api-1516603-callcomponentfunction.md)  function or this function to extract those parameters and pass them to a subroutine of your component. By taking advantage of these functions, you can simplify the structure of your component code. 

If your component subroutine requires a handle to the memory associated with the connection, you must use this function. You allocate the memory for a given connection each time your component is opened. You inform the Component Manager that a connection has memory associated with it by calling the  [`SetComponentInstanceError`](./api-1516663-setcomponentinstanceerror.md)  function.

Subroutines of a component that don’t need global data should use `CallComponentFunction` instead. 

## Parameters

- `storage`: A handle to the memory associated with the current connection. The Component Manager provides this handle to your component along with the request. 
- `params`: A pointer to the [`ComponentParameters`](./componentparameters.md) structure that your component received from the Component Manager. These are the parameters originally provided by the application that called your component. 
- `func`: A universal procedure pointer to the component function that is to handle the request. The Component Manager calls the function referred to by the `func` parameter, using Pascal calling conventions, with the parameters that were originally provided by the application that called your component. These parameters are preceded by a handle to the memory associated with the current connection. The function referred to by the `func` parameter must return a function result of type `ComponentResult` indicating the success or failure of the operation. See the [`ComponentRoutineProcPtr`](./componentroutineprocptr.md) callback for more information on component functions. 

## See Also

### Dispatching to Component Functions
- [CallComponentFunction](./api-1516603-callcomponentfunction.md)
  Invokes the specified function of your component.
- [CallComponentFunctionWithStorageProcInfo](./api-1516344-callcomponentfunctionwithstorage.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1516610-callcomponentfunctionwithstorage)*