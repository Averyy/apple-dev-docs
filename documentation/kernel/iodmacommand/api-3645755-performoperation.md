# PerformOperation

**Framework**: Kernel  
**Kind**: instm  
**Role**: Instance Method

**Availability**:
- macOS 11.0+

## Declaration

```c
kern_return_t PerformOperation(uint64_t options, uint64_t dmaOffset, uint64_t length, uint64_t dataOffset, IOMemoryDescriptor *data, OSDispatchMethod supermethod);
```

## See Also

### Callbacks
- [+ CompleteDMA_Invoke](./api-3645747-completedma_invoke.md)
- [+ Create](./api-3645748-create.md)
- [+ Create_Impl](./api-3645749-create_impl.md)
- [+ Create_Invoke](./api-3645750-create_invoke.md)
- [+ GetPreparation_Invoke](./api-3645754-getpreparation_invoke.md)
- [+ PerformOperation_Invoke](./api-3645757-performoperation_invoke.md)
- [+ PrepareForDMA_Invoke](./api-3645760-preparefordma_invoke.md)
- [- CompleteDMA](./api-3645745-completedma.md)
- [- CompleteDMA](../../DriverKit/iodmacommand/completedma.md)
- [- CompleteDMA_Impl](./api-3645746-completedma_impl.md)
- [- GetPreparation](./api-3645752-getpreparation.md)
- [- GetPreparation](../../DriverKit/iodmacommand/getpreparation.md)
- [- GetPreparation_Impl](./api-3645753-getpreparation_impl.md)
- [- PerformOperation](../../DriverKit/iodmacommand/performoperation.md)
- [- PerformOperation_Impl](./api-3645756-performoperation_impl.md)
- [- PrepareForDMA](./api-3645758-preparefordma.md)
- [- PrepareForDMA](../../DriverKit/iodmacommand/preparefordma.md)
- [- PrepareForDMA_Impl](./api-3645759-preparefordma_impl.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iodmacommand/3645755-performoperation)*