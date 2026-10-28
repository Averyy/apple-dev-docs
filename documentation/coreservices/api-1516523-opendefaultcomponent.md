# OpenDefaultComponent

**Framework**: Core Services  
**Kind**: func  
**Role**: Function

Opens a connection to a registered component of the component type and subtype specified by your application. 

**Availability**:
- macOS 10.0+ - Deprecated in 10.8

## Declaration

```c
ComponentInstance OpenDefaultComponent(OSType componentType, OSType componentSubType);
```

## Return Value

A component instance that identifies the connection opened to the component which matches your search criteria. You must supply this component instance whenever you call the functions provided by the component. When you close the component, you must also supply this component instance to the [`CloseComponent`](./api-1516436-closecomponent.md) function.

If more than one component in the list of registered components meets the search criteria, the function opens the first one that it finds in its list. If it cannot open the specified component, it returns `NULL`.

See the description of the `ComponentInstance` data type.

## Discussion

Your application must open a component before it can call any component functions. This function searches for a component by type and subtype. You do not have to supply a component description structure or call the  [`FindNextComponent`](./api-1516552-findnextcomponent.md)  function to use this function. If you want to exert more control over the selection process, you can use the `FindNextComponent` and  [`OpenComponent`](./api-1516607-opencomponent.md)  functions. 

## Parameters

- `componentType`: The type of the component. All components of a particular type support a common set of interface functions. Use this parameter to search for components of a given type. 
- `componentSubType`: The subtype of the component. Different subtypes of a component type may support additional features or provide interfaces that extend beyond the standard functions for a given component type. For example, the subtype of an image compressor component indicates the compression algorithm employed by the compressor.

  Your application can use the `componentSubType` parameter to perform a more specific lookup operation than is possible using only the `componentType` parameter. For example, you may want your application to use only components of a certain component type (`'draw'`) that also have a specific subtype (`'oval'`). Set this parameter to 0 to select a component with any subtype value.

## See Also

### Opening and Closing Components
- [OpenAComponent](./api-1516558-openacomponent.md)
- [OpenADefaultComponent](./api-1516360-openadefaultcomponent.md)
- [OpenComponent](./api-1516607-opencomponent.md)
  Opens a connection to the component with the component identifier specified by your application.
- [CloseComponent](./api-1516436-closecomponent.md)
  Terminates your application’s connection to a component. 


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1516523-opendefaultcomponent)*