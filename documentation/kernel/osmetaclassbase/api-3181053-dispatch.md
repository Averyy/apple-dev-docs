# Dispatch

**Framework**: Kernel  
**Kind**: instm  
**Role**: Instance Method

Runtime internals

**Availability**:
- DriverKit 19.0+
- macOS 15.4+

## Declaration

*DriverKit*

```cpp
virtual kern_return_t Dispatch(IORPC invoke);
```

*macOS*

```cpp
virtual kern_return_t Dispatch(const IORPC rpc);
```

## See Also

### Managing Runtime Internals
- [- Invoke](./api-3181056-invoke.md)
  Runtime internals


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/osmetaclassbase/3181053-dispatch)*