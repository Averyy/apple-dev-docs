# CloseComponent

**Framework**: Core Services  
**Kind**: func  
**Role**: Function

Terminates your application’s connection to a component. 

**Availability**:
- macOS 10.0+ - Deprecated in 10.8

## Declaration

```c
OSErr CloseComponent(ComponentInstance aComponentInstance);
```

## Return Value

A result code. See [Result Codes](./carbon_core/component_manager.md#1668759).

## Discussion

This function closes only a single connection. If your application has several connections to a single component, you must call it once for each connection. 

## Parameters

- `aComponentInstance`: The connection you wish to close. Your application obtains the component instance from the [`OpenComponent`](./api-1516607-opencomponent.md) function or the [`OpenDefaultComponent`](./api-1516523-opendefaultcomponent.md) function. You can use a component identifier here, but you must coerce the data type appropriately. 

## See Also

### Opening and Closing Components
- [OpenAComponent](./api-1516558-openacomponent.md)
- [OpenADefaultComponent](./api-1516360-openadefaultcomponent.md)
- [OpenComponent](./api-1516607-opencomponent.md)
  Opens a connection to the component with the component identifier specified by your application.
- [OpenDefaultComponent](./api-1516523-opendefaultcomponent.md)
  Opens a connection to a registered component of the component type and subtype specified by your application. 


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1516436-closecomponent)*