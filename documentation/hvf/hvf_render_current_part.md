# HVF_render_current_part

**Framework**: hvf  
**Kind**: func  
**Role**: Function

Render the current part using the supplied callback.

**Availability**:
- iOS 18.4+
- iPadOS 18.4+
- Mac Catalyst 18.4+
- macOS 15.4+
- tvOS 18.4+
- visionOS 2.4+
- watchOS 11.4+

## Declaration

```c
int HVF_render_current_part(HVFPartRenderer *renderer, HVFRenderContext context, void *caller_data);
```

## Discussion

The `caller_data` pointer is passed through to the callback.

The return value is 0 for success, nonzero for failure.


---

*[View on Apple Developer](https://developer.apple.com/documentation/hvf/hvf_render_current_part)*