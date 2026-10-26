# SetComponentInstanceError

**Framework**: Core Services  
**Kind**: func  
**Role**: Function

Passes error information to the Component Manager which sets the current error value for the appropriate connection.

**Availability**:
- macOS 10.0+ - Deprecated in 10.8

## Declaration

```c
void SetComponentInstanceError(ComponentInstance aComponentInstance, OSErr theError);
```

#### Discussion

In general, your component returns error information in its function result a nonzero function result indicates an error occurred, and a function result of 0 indicates the request was successful. However, some requests require that your component return other information as its function result. In these cases, your component can use this function to report its latest error state to the Component Manager. You can also use this function at any time during your component’s execution to report an error.

Applications retrieve this error information by calling the  [`GetComponentInstanceError`](./api-1516618-getcomponentinstanceerror.md)  function. The documentation for your component should specify how the component indicates errors. 

## Parameters

- `aComponentInstance`: The connection for which to set the error. The Component Manager provides a component instance to your component when the connection is opened. The Component Manager also provides a component instance to your component as the first parameter in the `params` field of the parameters structure. 
- `theError`: The new value for the current error. 


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1516663-setcomponentinstanceerror)*