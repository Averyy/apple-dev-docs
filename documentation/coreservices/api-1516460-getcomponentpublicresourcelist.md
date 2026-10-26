# GetComponentPublicResourceList

**Framework**: Core Services  
**Kind**: func  
**Role**: Function

**Availability**:
- macOS 10.0+ - Deprecated in 10.8

## Declaration

```c
OSErr GetComponentPublicResourceList(OSType resourceType, SInt16 resourceID, SInt32 flags, ComponentDescription *cd, GetMissingComponentResourceUPP missingProc, void *refCon, void *atomContainerPtr);
```

#### Return Value

A result code. See [Result Codes](./carbon_core/component_manager.md#1668759).

## Parameters

- `resourceType`: 
- `cd`: 
- `missingProc`: 

## See Also

### Getting Information About Components
- [GetComponentInfo](./api-1516438-getcomponentinfo.md)
  Returns to your application the registration information for a component. 
- [GetComponentPublicIndString](./api-1516516-getcomponentpublicindstring.md)
- [GetComponentPublicResource](./api-1516336-getcomponentpublicresource.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1516460-getcomponentpublicresourcelist)*