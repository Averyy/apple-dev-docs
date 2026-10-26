# profileVersion

**Framework**: Application Services  
**Kind**: structp  
**Role**: Instance Property

The version of the profile format.

**Availability**:
- macOS 10.0+ - Deprecated in 10.6

## Declaration

```c
UInt32 profileVersion;
```

#### Discussion

 The first 8 bits indicate the major version number, followed by 8 bits indicating the minor version number. The following 2 bytes are reserved.

The profile version number is not tied to the version of the ColorSync Manager. Profile formats and their versions are defined by the ICC. For example, a major version change may indicate the addition of new required tags to the profile format; a minor version change may indicate the addition of new optional tags.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applicationservices/cm2header/1560432-profileversion)*