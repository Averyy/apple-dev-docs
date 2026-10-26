# SetComponentInstanceStorage

**Framework**: Core Services  
**Kind**: func  
**Role**: Function

Allows your component to associate memory with a connection. 

**Availability**:
- macOS 10.0+ - Deprecated in 10.8

## Declaration

```c
void SetComponentInstanceStorage(ComponentInstance aComponentInstance, Handle theStorage);
```

#### Discussion

When an application or component opens a connection to your component, the Component Manager sends your component an open request. In response to this open request, your component should set up an environment to service the connection. Typically, your component should allocate some memory for the connection. Your component can then use that memory to maintain state information appropriate to the connection.

Your component should dispose of any allocated memory for the connection only in response to the close request. Note that whenever an open request fails, the Component Manager always issues the close request. Furthermore, the value stored with this function is always passed to the close request, so it must be valid or `NULL`. If the open request tries to dispose of its allocated memory before returning, it should call this function again with a `NULL` handle to keep the Component Manager from passing an invalid handle to the close request. 

## Parameters

- `aComponentInstance`: The connection to associate with the allocated memory. The Component Manager provides a component instance to your component when the connection is opened. You can use a component identifier here, but you must coerce the data type appropriately. 
- `theStorage`: A handle to the memory that your component has allocated for the connection. Your component must allocate this memory in the current heap. The Component Manager saves this handle and provides it to your component, along with other parameters, in subsequent requests to this connection. 

## See Also

### Managing Component Connections
- [CountComponentInstances](./api-1516394-countcomponentinstances.md)
  Determines the number of open connections being managed by a specified component. 
- [GetComponentInstanceStorage](./api-1516517-getcomponentinstancestorage.md)
  Allows your component to retrieve a handle to the memory associated with a connection. 


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1516556-setcomponentinstancestorage)*