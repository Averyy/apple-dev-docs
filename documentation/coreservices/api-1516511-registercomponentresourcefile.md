# RegisterComponentResourceFile

**Framework**: Core Services  
**Kind**: func  
**Role**: Function

Registers all component resources in the given resource file.

**Availability**:
- macOS 10.0+ - Deprecated in 10.8

## Declaration

```c
SInt32 RegisterComponentResourceFile(SInt16 resRefNum, SInt16 global);
```

#### Return Value

The number of components registered, if all components in the specified resource file are successfully registered. If one or more of the components in the resource file could not be registered, or if the specified file reference number is invalid, a negative function result. 

#### Discussion

Before a component can be used by an application, the component must be registered with the Component Manager. The Component Manager automatically registers component resources stored in files with file types of `'thng'` that are stored in the Extensions folder. For a description of the format and content of component resources, see “Resources”.  

## Parameters

- `resRefNum`: The reference number of the resource file containing the components to register. 
- `global`: A set of flags that control the scope of the registration of the components in the resource file. See [Register Component Resource flags](./api-1516405-register_component_resource_flag.md) for a description of the flags.

## See Also

### Registering Components
- [RegisterComponent](./api-1516537-registercomponent.md)
  Registers a component stored in memory.
- [RegisterComponentResource](./api-1516594-registercomponentresource.md)
  Registers a component stored in a resource file.
- [UnregisterComponent](./api-1516645-unregistercomponent.md)
  Removes a component from the Component Manager’s registration list.
- [RegisterComponentFileRef](./api-1516564-registercomponentfileref.md)
- [RegisterComponentFileRefEntries](./api-1516395-registercomponentfilerefentries.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1516511-registercomponentresourcefile)*