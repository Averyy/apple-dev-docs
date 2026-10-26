# HVF_set_render_part

**Framework**: hvf  
**Kind**: func  
**Role**: Function

Set the renderer to render the part indicated by the part index.

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
int HVF_set_render_part(HVFPartRenderer *renderer, HVFPartIndex partIndex);
```

#### Discussion

This call resets the axis values to the default value of 0.0.

The return value is 0 for success, nonzero for failure.


---

*[View on Apple Developer](https://developer.apple.com/documentation/hvf/hvf_set_render_part)*