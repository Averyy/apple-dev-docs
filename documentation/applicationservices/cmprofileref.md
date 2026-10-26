# CMProfileRef

**Framework**: Application Services  
**Kind**: tdef  
**Role**: Type Alias

Defines a reference to an opaque data type that specifies profile information.

**Availability**:
- macOS 10.0+ - Deprecated in 10.6

## Declaration

```c
typedef struct OpaqueCMProfileRef *CMProfileRef;
```

#### Discussion

A profile reference is the means by which your application gains access to a profile. Several ColorSync Manager functions return a profile reference to your application. Your application then passes it as a parameter on subsequent calls to other ColorSync Manager functions that use profiles.

The ColorSync Manager returns a unique profile reference in response to each individual call to the [CMOpenProfile](./colorsync_manager/api-1804853-cmopenprofile.md), [CMCopyProfile](./colorsync_manager/api-1804870-cmcopyprofile.md) , and [CMNewProfile](./colorsync_manager/api-1804911-cmnewprofile.md) functions. This allows multiple applications concurrent access to a profile. The ColorSync Manager defines an abstract private data structure of type `OpaqueCMProfileRef` for the profile reference. 


---

*[View on Apple Developer](https://developer.apple.com/documentation/applicationservices/cmprofileref)*