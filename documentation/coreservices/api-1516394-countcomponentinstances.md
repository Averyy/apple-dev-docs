# CountComponentInstances

**Framework**: Core Services  
**Kind**: func  
**Role**: Function

Determines the number of open connections being managed by a specified component. 

**Availability**:
- macOS 10.0+ - Deprecated in 10.8

## Declaration

```c
long CountComponentInstances(Component aComponent);
```

#### Return Value

The number of open connections for the specified component. 

#### Discussion

This function can be useful if you want to restrict the number of connections for your component or if your component needs to perform special processing based on the number of open connections. 

## Parameters

- `aComponent`: The component for which you want a count of open connections. You can use a component instance here, but you must coerce the data type appropriately. 

## See Also

### Managing Component Connections
- [GetComponentInstanceStorage](./api-1516517-getcomponentinstancestorage.md)
  Allows your component to retrieve a handle to the memory associated with a connection. 
- [SetComponentInstanceStorage](./api-1516556-setcomponentinstancestorage.md)
  Allows your component to associate memory with a connection. 


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1516394-countcomponentinstances)*