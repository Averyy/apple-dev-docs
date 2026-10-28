# UnregisterComponent

**Framework**: Core Services  
**Kind**: func  
**Role**: Function

Removes a component from the Component Manager’s registration list.

**Availability**:
- macOS 10.0+ - Deprecated in 10.8

## Declaration

```c
OSErr UnregisterComponent(Component aComponent);
```

## Return Value

A result code. See [Result Codes](./carbon_core/component_manager.md#1668759). If there are open connections to the component, returns a `validInstancesExist` error.

## Discussion

Most components are registered at startup and remain registered until the computer is shut down. However, you may want to provide some services temporarily. In that case you dispose of the component that provides the temporary service by using this function. 

## Parameters

- `aComponent`: The component to be removed. Applications that register components may obtain this identifier from the [`RegisterComponent`](./api-1516537-registercomponent.md) or [`RegisterComponentResource`](./api-1516594-registercomponentresource.md) functions. The component must not be in use by any applications or components. You can use a component instance here, but you must coerce the data type appropriately. 

## See Also

### Registering Components
- [RegisterComponent](./api-1516537-registercomponent.md)
  Registers a component stored in memory.
- [RegisterComponentResource](./api-1516594-registercomponentresource.md)
  Registers a component stored in a resource file.
- [RegisterComponentResourceFile](./api-1516511-registercomponentresourcefile.md)
  Registers all component resources in the given resource file.
- [RegisterComponentFileRef](./api-1516564-registercomponentfileref.md)
- [RegisterComponentFileRefEntries](./api-1516395-registercomponentfilerefentries.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1516645-unregistercomponent)*