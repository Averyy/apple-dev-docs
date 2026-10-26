# GetComponentListModSeed

**Framework**: Core Services  
**Kind**: func  
**Role**: Function

Allows your application to determine if the list of registered components has changed. 

**Availability**:
- macOS 10.0+ - Deprecated in 10.8

## Declaration

```c
SInt32 GetComponentListModSeed(void);
```

#### Return Value

The component registration seed number. Each time the Component Manager registers or unregisters a component it generates a new, unique seed number. By comparing the return value to values previously returned by this function, you can determine whether the list has changed. Your application may use this information to rebuild its internal component lists or to trigger other activity that is necessary whenever new components are available. 

## See Also

### Finding Components
- [CountComponents](./api-1516515-countcomponents.md)
  Returns the number of registered components that meet the selection criteria specified by your application. 
- [FindNextComponent](./api-1516552-findnextcomponent.md)
  Returns the component identifier for the next registered component that meets the selection criteria specified by your application. 
- [GetComponentTypeModSeed](./api-1516653-getcomponenttypemodseed.md)
- [ResolveComponentAlias](./api-1516484-resolvecomponentalias.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1516399-getcomponentlistmodseed)*