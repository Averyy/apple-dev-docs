# SetComponentRefcon

**Framework**: Core Services  
**Kind**: func  
**Role**: Function

Sets the reference constant for your component.

**Availability**:
- macOS 10.0+ - Deprecated in 10.8

## Declaration

```c
void SetComponentRefcon(Component aComponent, long theRefcon);
```

## Discussion

There is one reference constant for each component, regardless of the number of connections to that component. When your component is registered, the Component Manager sets this reference constant to 0.

The reference constant is a 4-byte value that your component can use in any way you decide. For example, you might use the reference constant to store the address of a data structure that is shared by all connections maintained by your component. You should allocate shared structures in the system heap. Your component should deallocate the structure when its last connection is closed or when it is unregistered. 

## Parameters

- `aComponent`: The component whose reference constant you wish to set. You can use a component instance here, but you must coerce the data type appropriately. 
- `theRefcon`: The reference constant value that you want to set for your component. Your component can retrieve the reference constant using the [`GetComponentRefcon`](./api-1516331-getcomponentrefcon.md) function. 

## See Also

### Working With Component Reference Constants
- [GetComponentRefcon](./api-1516331-getcomponentrefcon.md)
  Retrieves the value of the reference constant for your component. 


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1516562-setcomponentrefcon)*