# RegisterComponent

**Framework**: Core Services  
**Kind**: func  
**Role**: Function

Registers a component stored in memory.

**Availability**:
- macOS 10.0+ - Deprecated in 10.8

## Declaration

```c
Component RegisterComponent(ComponentDescription *cd, ComponentRoutineUPP componentEntryPoint, SInt16 global, Handle componentName, Handle componentInfo, Handle componentIcon);
```

## Return Value

The unique component identifier assigned to the component by the Component Manager or, if it cannot register the component, `NULL`. See the description of the `Component` data type.

## Discussion

Before a component can be used by an application, the component must be registered with the Component Manager. Applications can then find and open the component using the standard Component Manager functions. 

Components you register with the `RegisterComponent` function must be in memory when you call this function. If you want to register a component that is stored in the resource fork of a file, use the  [`RegisterComponentResource`](./api-1516594-registercomponentresource.md)  function. Use the  [`RegisterComponentResourceFile`](./api-1516511-registercomponentresourcefile.md)  function to register all components in the resource fork of a file. The Component Manager automatically registers component resources stored in files with file types of `'thng'` that are stored in the Extensions folder. See “Resources” for more information on component resource files.

Note that a component residing in your application heap remains registered until your application unregisters it or quits. When an application quits, the Component Manager automatically closes any component connections to that application. In addition, if the application has registered components that reside in its heap space, the Component Manager automatically unregisters those components. A component residing in the system heap and registered by your application remains registered until your application unregisters it or until the computer is shut down. 

## Parameters

- `cd`: A pointer to a [`ComponentDescription`](./componentdescription.md) structure that describes the component to be registered. You must correctly fill in the fields of this structure before calling this function. When applications search for components using the [`FindNextComponent`](./api-1516552-findnextcomponent.md) function, the Component Manager compares the attributes you specify here with those specified by the application. If the attributes match, the Component Manager returns the component identifier to the application. 
- `componentEntryPoint`: A universal procedure pointer (UPP) to your component’s main entry point. The function referred to by this parameter receives all requests for the component. See the [`ComponentRoutineProcPtr`](./componentroutineprocptr.md) callback for more information on creating a component function. 
- `global`: A set of flags that control the scope of component registration. See [Register Component Resource flags](./api-1516405-register_component_resource_flag.md) for a description of the flags. 
- `componentName`: A handle to the component’s name. Set this parameter to `NULL` if you do not want to assign a name to the component. 
- `componentInfo`: A handle to the component’s information string. Set this parameter to `NULL` if you do not want to assign an information string to the component.
- `componentIcon`: A handle to the component’s icon (a 32-by-32 pixel black-and-white icon). Set this parameter to `NULL` if you do not want to supply an icon for this component. Note that this icon is not used by the Finder you supply an icon only so that other components or applications can display your component’s icon if needed.

## See Also

### Registering Components
- [RegisterComponentResource](./api-1516594-registercomponentresource.md)
  Registers a component stored in a resource file.
- [RegisterComponentResourceFile](./api-1516511-registercomponentresourcefile.md)
  Registers all component resources in the given resource file.
- [UnregisterComponent](./api-1516645-unregistercomponent.md)
  Removes a component from the Component Manager’s registration list.
- [RegisterComponentFileRef](./api-1516564-registercomponentfileref.md)
- [RegisterComponentFileRefEntries](./api-1516395-registercomponentfilerefentries.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1516537-registercomponent)*