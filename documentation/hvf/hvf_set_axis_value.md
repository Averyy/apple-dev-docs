# HVF_set_axis_value

**Framework**: hvf  
**Kind**: func  
**Role**: Function

Set the axis value.

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
int HVF_set_axis_value(HVFPartRenderer *renderer, int axis, HVFAxisValue value);
```

#### Discussion

The value is in design space, [-1.0, 1.0]) for the indicated global axis, using the same axis numbering as would be in the `fvar` table.

The return value is 0 for success, nonzero for failure.


---

*[View on Apple Developer](https://developer.apple.com/documentation/hvf/hvf_set_axis_value)*