# CallComponentFunction

**Framework**: Core Services  
**Kind**: func  
**Role**: Function

Invokes the specified function of your component.

**Availability**:
- macOS 10.0+ - Deprecated in 10.8

## Declaration

```c
ComponentResult CallComponentFunction(ComponentParameters *params, ComponentFunctionUPP func);
```

#### Return Value

The value that is returned by the function referred to by the `func` parameter. Your component should use this value to set the current error for this connection. You can use the [`SetComponentInstanceError`](./api-1516663-setcomponentinstanceerror.md) function to set the current error. 

#### Discussion

When an application requests service from your component, your component receives a component parameters structure containing the parameters that the application provided when it called your component. Your component can use this structure to access the parameters directly. Alternatively, you can use either this function or  [`CallComponentFunctionWithStorage`](./api-1516610-callcomponentfunctionwithstorage.md)  to extract those parameters and pass them to a subroutine of your component. By taking advantage of these functions, you can simplify the structure of your component code. 

If your component subroutine does not need global data, your component should use this function. If your component subroutine requires memory in which to store global data for the component, your component must use `CallComponentFunctionWithStorage`. 

## Parameters

- `params`: A pointer to the [`ComponentDescription`](./componentdescription.md) structure that your component received from the Component Manager. These are the parameters originally provided by the application that called your component. 
- `func`: A universal procedure pointer to the component function that is to handle the request. The Component Manager calls the function referred to by the `func` parameter, using Pascal calling conventions, with the parameters that were originally provided by the application that called your component. The function referred to by this parameter must return a function result of type `ComponentResult` indicating the success or failure of the operation. See the [`ComponentRoutineProcPtr`](./componentroutineprocptr.md) callback for more information on component functions. 

## See Also

### Dispatching to Component Functions
- [CallComponentFunctionWithStorage](./api-1516610-callcomponentfunctionwithstorage.md)
  Invokes the specified function of your component. 
- [CallComponentFunctionWithStorageProcInfo](./api-1516344-callcomponentfunctionwithstorage.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1516603-callcomponentfunction)*