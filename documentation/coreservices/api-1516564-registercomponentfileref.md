# RegisterComponentFileRef

**Framework**: Core Services  
**Kind**: func  
**Role**: Function

**Availability**:
- macOS 10.0+ - Deprecated in 10.8

## Declaration

```c
OSErr RegisterComponentFileRef(const FSRef *ref, SInt16 global);
```

#### Return Value

A result code. See [Result Codes](./carbon_core/component_manager.md#1668759).

## Parameters

- `ref`: 

## See Also

### Registering Components
- [RegisterComponent](./api-1516537-registercomponent.md)
  Registers a component stored in memory.
- [RegisterComponentResource](./api-1516594-registercomponentresource.md)
  Registers a component stored in a resource file.
- [RegisterComponentResourceFile](./api-1516511-registercomponentresourcefile.md)
  Registers all component resources in the given resource file.
- [UnregisterComponent](./api-1516645-unregistercomponent.md)
  Removes a component from the Component Manager’s registration list.
- [RegisterComponentFileRefEntries](./api-1516395-registercomponentfilerefentries.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1516564-registercomponentfileref)*