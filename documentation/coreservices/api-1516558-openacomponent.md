# OpenAComponent

**Framework**: Core Services  
**Kind**: func  
**Role**: Function

**Availability**:
- macOS 10.0+ - Deprecated in 10.8

## Declaration

```c
OSErr OpenAComponent(Component aComponent, ComponentInstance *ci);
```

#### Return Value

A result code. See [Result Codes](./carbon_core/component_manager.md#1668759).

## Parameters

- `aComponent`: 
- `ci`: 

## See Also

### Opening and Closing Components
- [OpenADefaultComponent](./api-1516360-openadefaultcomponent.md)
- [OpenComponent](./api-1516607-opencomponent.md)
  Opens a connection to the component with the component identifier specified by your application.
- [OpenDefaultComponent](./api-1516523-opendefaultcomponent.md)
  Opens a connection to a registered component of the component type and subtype specified by your application. 
- [CloseComponent](./api-1516436-closecomponent.md)
  Terminates your application’s connection to a component. 


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1516558-openacomponent)*