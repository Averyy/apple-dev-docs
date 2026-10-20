# Invoke

**Framework**: Kernel  
**Kind**: instm  
**Role**: Instance Method

Runtime internals

**Availability**:
- DriverKit 19.0+
- macOS 15.4+

## Declaration

*DriverKit*

```c
kern_return_t Invoke(IORPC invoke);
```

*macOS*

```c
kern_return_t Invoke(const IORPC rpc);
```

## See Also

### Managing Runtime Internals
- [- Dispatch](./api-3181053-dispatch.md)
  Runtime internals


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/osmetaclassbase/3181056-invoke)*