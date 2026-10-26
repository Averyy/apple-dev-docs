# MMU Type Selectors

**Framework**: Core Services  
**Kind**: enum  
**Role**: Enumeration

Specify information about the type of MMU installed.

**Availability**:
- Mac Catalyst 17.0+
- macOS 10.0+

## Declaration

```c
enum : unsigned int {
    ...
};
```

## Topics

### Constants
- [gestaltMMUType](./api-1472336-mmu_type_selectors/gestaltmmutype.md)
  The selector you pass to the `Gestalt` function to determine the  type of MMU currently installed.
- [gestaltNoMMU](./api-1472336-mmu_type_selectors/gestaltnommu.md)
- [gestaltAMU](./api-1472336-mmu_type_selectors/gestaltamu.md)
- [gestalt68851](./api-1472336-mmu_type_selectors/gestalt68851.md)
- [gestalt68030MMU](./api-1472336-mmu_type_selectors/gestalt68030mmu.md)
- [gestalt68040MMU](./api-1472336-mmu_type_selectors/gestalt68040mmu.md)
- [gestaltEMMU1](./api-1472336-mmu_type_selectors/gestaltemmu1.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1472336-mmu_type_selectors)*