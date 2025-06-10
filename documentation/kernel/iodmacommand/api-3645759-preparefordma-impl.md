# PrepareForDMA_Impl

**Framework**: Kernel  
**Kind**: instm

**Availability**:
- macOS 11.0+

## Declaration

```swift
kern_return_t PrepareForDMA_Impl(uint64_t options, IOMemoryDescriptor *memory, uint64_t offset, uint64_t length, uint64_t *flags, uint32_t *segmentsCount, IOAddressSegment *segments);
```

## See Also

- [+ CompleteDMA_Invoke](iodmacommand/3645747-completedma_invoke.md)
- [+ Create](iodmacommand/3645748-create.md)
- [+ Create_Impl](iodmacommand/3645749-create_impl.md)
- [+ Create_Invoke](iodmacommand/3645750-create_invoke.md)
- [+ GetPreparation_Invoke](iodmacommand/3645754-getpreparation_invoke.md)
- [+ PerformOperation_Invoke](iodmacommand/3645757-performoperation_invoke.md)
- [+ PrepareForDMA_Invoke](iodmacommand/3645760-preparefordma_invoke.md)
- [- CompleteDMA](iodmacommand/3645745-completedma.md)
- [- CompleteDMA](../driverkit/iodmacommand/3645792-completedma.md)
- [- CompleteDMA_Impl](iodmacommand/3645746-completedma_impl.md)
- [- GetPreparation](iodmacommand/3645752-getpreparation.md)
- [- GetPreparation](../driverkit/iodmacommand/3645793-getpreparation.md)
- [- GetPreparation_Impl](iodmacommand/3645753-getpreparation_impl.md)
- [- PerformOperation](iodmacommand/3645755-performoperation.md)
- [- PerformOperation](../driverkit/iodmacommand/3645794-performoperation.md)
- [- PerformOperation_Impl](iodmacommand/3645756-performoperation_impl.md)
- [- PrepareForDMA](iodmacommand/3645758-preparefordma.md)
- [- PrepareForDMA](../driverkit/iodmacommand/3645795-preparefordma.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iodmacommand/3645759-preparefordma_impl)*