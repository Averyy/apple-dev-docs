# Profile Location Type

**Framework**: Application Services

Defines profile location kinds.

#### Overview

Your application specifies the location for a profile using a profile location structure of type [`CMProfileLocation`](cmprofilelocation.md). A ColorSync profile that you open or create is typically stored in one of the following locations:

-  In a disk file. The `u` field (a union) of the profile location data structure contains a file specification for a profile that is disk-file based. This is the most common way to store a ColorSync profile. 
-  In relocatable memory. The `u` field of the profile location data structure contains a handle specification for a profile that is stored in a handle. 
-  In nonrelocatable memory. The `u` field of the profile location data structure contains a pointer specification for a profile that is pointer based. 
-  In an arbitrary location, accessed by a procedure you provide. The `u` field of the profile location data structure contains a universal procedure pointer to your access procedure, as well as a pointer that may point to data associated with your procedure. 

Additionally, your application can create a new or duplicate temporary profile. For example, you can use a temporary profile for a color-matching session and the profile is not saved after the session. For this case, the ColorSync Manager allows you to specify the profile location as having no specific location. 

You use a pointer to a data structure of type `CMProfileLocation` to identify a profile’s location when your application calls

-  the `CMOpenProfile` function to obtain a reference to a profile 
-  the `CMNewProfile`, `CWNewLinkProfile,` or `CMCopyProfile` functions to create a new profile 
-  the `CMGetProfileLocation` function to get the location of an existing profile 

Your application identifies the type of data the `CMProfileLocation ``u` field holds—a file specification, a handle, and so on—in the `CMProfileLocation` structure’s `locType` field. You use the constants defined by this enumeration to identify the location type.  

## Topics

### Constants
- [var cmNoProfileBase: Int](cmnoprofilebase.md)
  The profile is temporary. It will not persist in memory after its use for a color session. You can specify this type of profile location with the `CMNewProfile` and the `CMCopyProfile` functions.
- [var cmPathBasedProfile: Int](cmpathbasedprofile.md)
- [var cmBufferBasedProfile: Int](cmbufferbasedprofile.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1560599-profile_location_type)*