# Admin Attribute Selectors

**Framework**: Core Services  
**Kind**: enum  
**Role**: Enumeration

Specify feature availability for Macintosh Manager administration software. 

**Availability**:
- Mac Catalyst 17.0+
- macOS 10.0+

## Declaration

```c
enum : unsigned int {
    ...
};
```

## Topics

### Constants
- [gestaltAdminFeaturesFlagsAttr](./api-1472053-admin_attribute_selectors/gestaltadminfeaturesflagsattr.md)
  The `Gestalt` selector you pass to determine the admin features that are present. This selector is typically used by the system.
- [gestaltFinderUsesSpecialOpenFoldersFile](./api-1472053-admin_attribute_selectors/gestaltfinderusesspecialopenfoldersfile.md)
  Specifies that the Finder uses a special file to store the list of open folders.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1472053-admin_attribute_selectors)*