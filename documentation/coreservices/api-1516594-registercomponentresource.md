# RegisterComponentResource

**Framework**: Core Services  
**Kind**: func  
**Role**: Function

Registers a component stored in a resource file.

**Availability**:
- macOS 10.0+ - Deprecated in 10.8

## Declaration

```c
Component RegisterComponentResource(ComponentResourceHandle cr, SInt16 global);
```

## Return Value

The unique component identifier assigned to the component by the Component Manager, or `NULL `if the function could not register the component. See the description of the `Component` data type.

## Discussion

Before a component can be used by an application, the component must be registered with the Component Manager. Applications can then find and open the component using the standard Component Manager functions. 

If you want to register a component that is in memory, use the  [`RegisterComponent`](./api-1516537-registercomponent.md)  function.

This function does not actually load the code specified by the component resource into memory. Rather, the Component Manager loads the component code the first time an application opens the component. If the code is not in the same file as the component resource or if the Component Manager cannot find the file, the open request fails.

Note that a component registered locally by your application remains registered until your application unregisters it or quits. When an application quits, the Component Manager automatically closes any component connections to that application. In addition, if the application has registered components that reside in its heap space, the Component Manager automatically unregisters those components. A component registered globally by your application remains registered until your application unregisters it or until the computer is shut down. 

## Parameters

- `cr`: A handle to a component resource that describes the component to be registered. The component resource contains all the information required to register the component. Components you register with this function must be stored in a resource file as a component resource. The Component Manager automatically registers component resources stored in files with file types of `'thng'` that are stored in the Extensions folder. See “Resources” for more information on component resource files. 
- `global`: A set of flags that controls the scope of component registration. See [Register Component Resource flags](./api-1516405-register_component_resource_flag.md) for a description of the flags. 

## See Also

### Registering Components
- [RegisterComponent](./api-1516537-registercomponent.md)
  Registers a component stored in memory.
- [RegisterComponentResourceFile](./api-1516511-registercomponentresourcefile.md)
  Registers all component resources in the given resource file.
- [UnregisterComponent](./api-1516645-unregistercomponent.md)
  Removes a component from the Component Manager’s registration list.
- [RegisterComponentFileRef](./api-1516564-registercomponentfileref.md)
- [RegisterComponentFileRefEntries](./api-1516395-registercomponentfilerefentries.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1516594-registercomponentresource)*