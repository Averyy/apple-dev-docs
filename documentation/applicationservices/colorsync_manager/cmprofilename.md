# CMProfileName

**Framework**: Application Services  
**Kind**: tdef

Contains profile name and length.

## Declaration

```c
struct CMProfileName {
   UniCharCount profileNameLength;
   UniChar profileName[256];
};
typedef struct CMProfileName CMProfileName;
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/applicationservices/colorsync_manager/cmprofilename)*