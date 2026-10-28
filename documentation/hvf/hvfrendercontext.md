# HVFRenderContext

**Framework**: hvf  
**Kind**: typealias  
**Role**: Type Alias

The type of the callback passed to `HVF_render_current_part()`.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS
- watchOS

## Declaration

```c
typedef enum HVFPartRenderAction (*)(enum HVFPartRenderInstruction, const union HVFPartRenderParameters *, void *) HVFRenderContext;
```

## Discussion

The scaler will call the supplied function to pass rendering instructions. The value of `caller_data` passed to `HVF_render_current_part()` will be passed to the callback via the last parameter.


---

*[View on Apple Developer](https://developer.apple.com/documentation/hvf/hvfrendercontext)*