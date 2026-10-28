# OpenComponent

**Framework**: Core Services  
**Kind**: func  
**Role**: Function

Opens a connection to the component with the component identifier specified by your application.

**Availability**:
- macOS 10.0+ - Deprecated in 10.8

## Declaration

```c
ComponentInstance OpenComponent(Component aComponent);
```

## Return Value

A component instance which identifies your application’s connection to the component. You must supply this component instance whenever you call the functions provided by the component. When you close the component, you must also supply this component instance to the [`CloseComponent`](./api-1516436-closecomponent.md) function.

If it cannot open the specified component, the function returns `NULL`.

See the description of the `ComponentInstance` data type.

## Discussion

Your application must open a component before it can call any component functions. To use this function, you must already have obtained a component identifier. Alternatively, you can use the  [`OpenDefaultComponent`](./api-1516523-opendefaultcomponent.md)  function to open a component without calling `FindNextComponent`. 

Note that your application may maintain several connections to a single component, or it may have connections to several components at the same time. 

## Parameters

- `aComponent`: The component you wish to open. Your application obtains this identifier from the [`FindNextComponent`](./api-1516552-findnextcomponent.md) function. If your application registers a component, it can also obtain a component identifier from the `RegisterComponent` function or the `RegisterComponentResource` function. 

## See Also

### Opening and Closing Components
- [OpenAComponent](./api-1516558-openacomponent.md)
- [OpenADefaultComponent](./api-1516360-openadefaultcomponent.md)
- [OpenDefaultComponent](./api-1516523-opendefaultcomponent.md)
  Opens a connection to a registered component of the component type and subtype specified by your application. 
- [CloseComponent](./api-1516436-closecomponent.md)
  Terminates your application’s connection to a component. 


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1516607-opencomponent)*