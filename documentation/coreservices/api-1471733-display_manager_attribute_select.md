# Display Manager Attribute Selectors

**Framework**: Core Services  
**Kind**: enum  
**Role**: Enumeration

Specify feature availability for the Display Manager.

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
- [gestaltDisplayMgrAttr](./api-1471733-display_manager_attribute_select/gestaltdisplaymgrattr.md)
  The `Gestalt` selector you pass to determine which Display Manager attributes are present.
- [gestaltDisplayMgrPresent](./api-1471733-display_manager_attribute_select/gestaltdisplaymgrpresent.md)
  If `true`, the Display Manager is present.
- [gestaltDisplayMgrCanSwitchMirrored](./api-1471733-display_manager_attribute_select/gestaltdisplaymgrcanswitchmirrored.md)
  If `true`, the Display Manager can switch modes on mirrored displays.
- [gestaltDisplayMgrSetDepthNotifies](./api-1471733-display_manager_attribute_select/gestaltdisplaymgrsetdepthnotifies.md)
  If `true`, and you have registered for notification and you will be notified of depth mode changes.
- [gestaltDisplayMgrCanConfirm](./api-1471733-display_manager_attribute_select/gestaltdisplaymgrcanconfirm.md)
  Not yet supported. Most commonly comes up for display modes that are not marked `kModeSafe`. There is currently no system support for trying an unsafe mode and then restoring if the user does not confirm. When this is supported, this bit will be set.
- [gestaltDisplayMgrColorSyncAware](./api-1471733-display_manager_attribute_select/gestaltdisplaymgrcolorsyncaware.md)
  If `true`, Display Manager supports profiles for displays. 
- [gestaltDisplayMgrGeneratesProfiles](./api-1471733-display_manager_attribute_select/gestaltdisplaymgrgeneratesprofiles.md)
- [gestaltDisplayMgrSleepNotifies](./api-1471733-display_manager_attribute_select/gestaltdisplaymgrsleepnotifies.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1471733-display_manager_attribute_select)*