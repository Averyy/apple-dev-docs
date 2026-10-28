# CMProfLoc

**Framework**: Application Services  
**Kind**: union  
**Role**: Union

Defines a union that identifies the location of a profile. 

**Availability**:
- macOS 10.0+ - Deprecated in 10.6

## Declaration

```c
typedef union CMProfLoc {
    ...
} CMProfLoc;
```

## Discussion

You use a union of type `CMProfLoc` to identify the location of a profile. You specify the union in the `u` field of the data type [`CMProfileLocation`](./cmprofilelocation.md). Your application passes a pointer to a `CMProfileLocation` structure when it calls the [CMOpenProfile](./colorsync_manager/api-1804853-cmopenprofile.md) function to identify the location of a profile or the [CMNewProfile](./colorsync_manager/api-1804911-cmnewprofile.md), [CMCopyProfile](./colorsync_manager/api-1804870-cmcopyprofile.md) , or [CWNewLinkProfile](./colorsync_manager/api-1804915-cwnewlinkprofile.md) functions to specify the location for a newly created profile.

You also pass a pointer to a `CMProfileLocation` structure to the [NCMGetProfileLocation](./colorsync_manager/api-1804889-ncmgetprofilelocation.md) and [CMGetProfileLocation](./colorsync_manager/api-1804885-cmgetprofilelocation.md) functions to get the location of an existing profile. The `NCMGetProfileLocation` function is available starting with ColorSync version 2.5. It differs from its predecessor, `CMGetProfileLocation`, in that the newer version has a parameter for the size of the location structure for the specified profile. 

## Topics

### Fields
- [handleLoc](./api-1560460-cmprofloc/api-1560221-handleloc.md)
  A data structure containing a handle that indicates the location of a profile in relocatable memory. 
- [pathLoc](./api-1560460-cmprofloc/api-1560356-pathloc.md)
- [bufferLoc](./api-1560460-cmprofloc/api-1560292-bufferloc.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/applicationservices/1560460-cmprofloc)*