# Quality Flag Values for Version 2.x Profiles

**Framework**: Application Services  
**Kind**: enum  
**Role**: Enumeration

Define the possible values for the quality bits in the `flags` field of the `CM2Header` structure. 

**Availability**:
- macOS 10.0+

## Declaration

```c
enum : unsigned int {
    ...
};
```

## Topics

### Constants
- [cmNormalMode](./api-1560115-x_profiles/cmnormalmode.md)
  This is the default setting. Normal mode indicates that the CMM should use its default method to compromise between performance and resource requirements.
- [cmDraftMode](./api-1560115-x_profiles/cmdraftmode.md)
  Draft mode indicates that the CMM should sacrifice quality, if necessary, to minimize resource requirements. Note that the default CMM currently produces the same results for both normal and draft mode.
- [cmBestMode](./api-1560115-x_profiles/cmbestmode.md)
  Best mode indicates that the CMM should maximize resource usage to ensure the highest possible quality.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applicationservices/1560115-x_profiles)*