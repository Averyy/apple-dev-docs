# CountComponents

**Framework**: Core Services  
**Kind**: func  
**Role**: Function

Returns the number of registered components that meet the selection criteria specified by your application. 

**Availability**:
- macOS 10.0+ - Deprecated in 10.8

## Declaration

```c
long CountComponents(ComponentDescription *looking);
```

## Return Value

The number of components that meet the specified search criteria. 

## Parameters

- `looking`: A pointer to a [`ComponentDescription`](./componentdescription.md) structure. Your application specifies the criteria for the component search in the fields of this structure.

  The Component Manager ignores fields in the component description structure that are set to 0. For example, if you set all the fields to 0, the Component Manager returns the number of components registered in the system. Similarly, if you set all fields to 0 except for the `componentManufacturer` field, the Component Manager returns the number of registered components supplied by the manufacturer you specify.

## See Also

### Finding Components
- [FindNextComponent](./api-1516552-findnextcomponent.md)
  Returns the component identifier for the next registered component that meets the selection criteria specified by your application. 
- [GetComponentListModSeed](./api-1516399-getcomponentlistmodseed.md)
  Allows your application to determine if the list of registered components has changed. 
- [GetComponentTypeModSeed](./api-1516653-getcomponenttypemodseed.md)
- [ResolveComponentAlias](./api-1516484-resolvecomponentalias.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1516515-countcomponents)*