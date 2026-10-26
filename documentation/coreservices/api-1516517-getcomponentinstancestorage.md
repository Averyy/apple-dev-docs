# GetComponentInstanceStorage

**Framework**: Core Services  
**Kind**: func  
**Role**: Function

Allows your component to retrieve a handle to the memory associated with a connection. 

**Availability**:
- macOS 10.0+ - Deprecated in 10.8

## Declaration

```c
Handle GetComponentInstanceStorage(ComponentInstance aComponentInstance);
```

#### Return Value

A handle to the memory associated with the specified connection. 

#### Discussion

Typically, your component does not need to use this function, because the Component Manager provides this handle to your component each time the client application requests service from this connection.

Your component tells the Component Manager about the memory associated with a connection by calling the  [`SetComponentInstanceStorage`](./api-1516556-setcomponentinstancestorage.md)  function.  

## Parameters

- `aComponentInstance`: The connection for which to retrieve the associated memory. The Component Manager provides a component instance to your component when the connection is opened. You can use a component identifier here, but you must coerce the data type appropriately. 

## See Also

### Managing Component Connections
- [CountComponentInstances](./api-1516394-countcomponentinstances.md)
  Determines the number of open connections being managed by a specified component. 
- [SetComponentInstanceStorage](./api-1516556-setcomponentinstancestorage.md)
  Allows your component to associate memory with a connection. 


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1516517-getcomponentinstancestorage)*