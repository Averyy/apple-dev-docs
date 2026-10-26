# FindNextComponent

**Framework**: Core Services  
**Kind**: func  
**Role**: Function

Returns the component identifier for the next registered component that meets the selection criteria specified by your application. 

**Availability**:
- macOS 10.0+ - Deprecated in 10.8

## Declaration

```c
Component FindNextComponent(Component aComponent, ComponentDescription *looking);
```

#### Return Value

The component identifier of a component that meets the search criteria or 0 when there are no more matching components. Your application can use the component identifier returned by this function to get more information about the component, using `GetComponentInfo`, or to open the component, using either the [`OpenDefaultComponent`](./api-1516523-opendefaultcomponent.md) function or the [`OpenComponent`](./api-1516607-opencomponent.md) function. See the description of the `Component` data type.

## Parameters

- `aComponent`: The starting point for the search. Set this field to 0 to start the search at the beginning of the component list. If you are continuing a search, you can specify a component identifier previously returned by this function. The function then searches the remaining components. 
- `looking`: A pointer to a [`ComponentDescription`](./componentdescription.md) structure. Your application specifies the criteria for the component search in the fields of this structure.

  The Component Manager ignores fields in the component description structure that are set to 0. For example, if you set all the fields to 0, all components meet the search criteria. In this case, your application can retrieve information about all of the components that are registered in the system by repeatedly calling `FindNextComponent` and [`GetComponentInfo`](./api-1516438-getcomponentinfo.md) until the search is complete. Similarly, if you set all fields to 0 except for the `componentManufacturer` field, the Component Manager searches all registered components for a component supplied by the manufacturer you specify. Note that this function does not modify the contents of the component description structure you supply. To retrieve detailed information about a component, you need to use the [`GetComponentInfo`](./api-1516438-getcomponentinfo.md) function to get the component description structure for each returned component.

## See Also

### Finding Components
- [CountComponents](./api-1516515-countcomponents.md)
  Returns the number of registered components that meet the selection criteria specified by your application. 
- [GetComponentListModSeed](./api-1516399-getcomponentlistmodseed.md)
  Allows your application to determine if the list of registered components has changed. 
- [GetComponentTypeModSeed](./api-1516653-getcomponenttypemodseed.md)
- [ResolveComponentAlias](./api-1516484-resolvecomponentalias.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1516552-findnextcomponent)*