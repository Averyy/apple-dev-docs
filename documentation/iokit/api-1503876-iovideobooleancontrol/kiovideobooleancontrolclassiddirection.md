# kIOVideoBooleanControlClassIDDirection

**Framework**: IOKit  
**Kind**: econst  
**Role**: Enumeration Case

**Availability**:
- Mac Catalyst 18.4+
- macOS 10.7+

## Declaration

```c
kIOVideoBooleanControlClassIDDirection = 'dire'
```

## Discussion

A IOVideoBooleanControl where a true value means the element is operating in input mode, and false means the element is operating in output mode. This control is only needed for devices which can do input and output, but not at the same time.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/1503876-iovideobooleancontrol/kiovideobooleancontrolclassiddirection)*